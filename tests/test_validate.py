#!/usr/bin/env python3
"""Unit tests for scripts/validate.py."""
from __future__ import annotations

import importlib.util
import io
import json
import subprocess
import sys
import unittest
from contextlib import redirect_stdout
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VALIDATE_PATH = ROOT / "scripts" / "validate.py"


def load_validate_module():
    module_name = "agency_validate"
    spec = importlib.util.spec_from_file_location(module_name, VALIDATE_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {VALIDATE_PATH}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module


validate = load_validate_module()


class ParseFrontmatterTests(unittest.TestCase):
    def setUp(self) -> None:
        self.validator = validate.Validator("pretty", strict=False, skip_drift=True)

    def test_parses_scalar_fields(self) -> None:
        text = "---\nname: example\ndescription: An example skill.\n---\n\n## When to use\n"
        frontmatter, body, errors = self.validator.parse_frontmatter(text)
        self.assertEqual(errors, [])
        self.assertIsNotNone(frontmatter)
        assert frontmatter is not None
        self.assertEqual(frontmatter["name"], "example")
        self.assertEqual(frontmatter["description"], "An example skill.")
        self.assertIn("## When to use", body)

    def test_reports_missing_delimiters(self) -> None:
        frontmatter, _, errors = self.validator.parse_frontmatter("# No frontmatter\n")
        self.assertIsNone(frontmatter)
        self.assertTrue(any("missing YAML frontmatter" in err for err in errors))

    def test_parses_allowed_tools_list(self) -> None:
        text = (
            "---\n"
            "name: tools\ndescription: Tool list.\n"
            "allowed-tools:\n"
            "  - Read\n"
            "  - Write\n"
            "---\n"
        )
        frontmatter, _, errors = self.validator.parse_frontmatter(text)
        self.assertEqual(errors, [])
        assert frontmatter is not None
        self.assertEqual(frontmatter["allowed-tools"], ["Read", "Write"])


class StripScalarTests(unittest.TestCase):
    def setUp(self) -> None:
        self.validator = validate.Validator("pretty", strict=False, skip_drift=True)

    def test_strips_quoted_strings(self) -> None:
        self.assertEqual(self.validator.strip_scalar('"hello"'), "hello")
        self.assertEqual(self.validator.strip_scalar("'world'"), "world")

    def test_preserves_block_indicators(self) -> None:
        self.assertEqual(self.validator.strip_scalar("|"), "|")
        self.assertEqual(self.validator.strip_scalar(">"), ">")


class MainTests(unittest.TestCase):
    def test_help_exits_zero(self) -> None:
        result = subprocess.run(
            [sys.executable, str(VALIDATE_PATH), "--help"],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0)
        self.assertIn("validate.py", result.stdout)

    def test_repo_validation_passes(self) -> None:
        result = subprocess.run(
            [sys.executable, str(VALIDATE_PATH)],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(
            result.returncode,
            0,
            msg=result.stderr or result.stdout,
        )

    def test_json_format_emits_parseable_report(self) -> None:
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            validator = validate.Validator("json", strict=False, skip_drift=False)
            exit_code = validator.run()
        self.assertEqual(exit_code, 0)
        report = json.loads(buffer.getvalue())
        self.assertEqual(report["version"], 1)
        self.assertIn("summary", report)
        self.assertIn("check_results", report)
        self.assertEqual(report["summary"]["errors"], 0)


if __name__ == "__main__":
    unittest.main()
