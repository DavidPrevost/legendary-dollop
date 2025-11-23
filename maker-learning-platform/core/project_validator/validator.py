"""Project validation for the Maker Learning Platform.

This module provides validation functions to check if projects
meet their completion criteria.
"""

import os
import re
from pathlib import Path
from typing import Optional


class ValidationResult:
    """Result of a validation check."""

    def __init__(self, passed: bool, message: str, details: Optional[str] = None):
        self.passed = passed
        self.message = message
        self.details = details

    def __repr__(self):
        status = "✓" if self.passed else "✗"
        return f"{status} {self.message}"


class ProjectValidator:
    """Validates project completion for Project Foundations subject."""

    def __init__(self, project_path: str):
        self.project_path = Path(project_path)

    def file_exists(self, filename: str) -> ValidationResult:
        """Check if a file exists in the project."""
        file_path = self.project_path / filename
        if file_path.exists():
            return ValidationResult(True, f"File exists: {filename}")
        return ValidationResult(False, f"File not found: {filename}")

    def dir_exists(self, dirname: str) -> ValidationResult:
        """Check if a directory exists in the project."""
        dir_path = self.project_path / dirname
        if dir_path.is_dir():
            return ValidationResult(True, f"Directory exists: {dirname}")
        return ValidationResult(False, f"Directory not found: {dirname}")

    def word_count(self, filename: str, min_words: int) -> ValidationResult:
        """Check if a file has at least min_words words."""
        file_path = self.project_path / filename
        if not file_path.exists():
            return ValidationResult(False, f"File not found: {filename}")

        try:
            content = file_path.read_text(encoding="utf-8")
            words = len(content.split())
            if words >= min_words:
                return ValidationResult(
                    True,
                    f"Word count OK: {words} words (min: {min_words})"
                )
            return ValidationResult(
                False,
                f"Word count too low: {words} words (min: {min_words})"
            )
        except Exception as e:
            return ValidationResult(False, f"Error reading file: {e}")

    def has_heading_levels(self, filename: str, min_levels: int) -> ValidationResult:
        """Check if Markdown file uses at least min_levels heading levels."""
        file_path = self.project_path / filename
        if not file_path.exists():
            return ValidationResult(False, f"File not found: {filename}")

        try:
            content = file_path.read_text(encoding="utf-8")
            levels_found = set()
            for line in content.split("\n"):
                if line.startswith("#"):
                    level = len(line) - len(line.lstrip("#"))
                    if 1 <= level <= 6:
                        levels_found.add(level)

            if len(levels_found) >= min_levels:
                return ValidationResult(
                    True,
                    f"Heading levels OK: {len(levels_found)} levels found"
                )
            return ValidationResult(
                False,
                f"Not enough heading levels: {len(levels_found)} (min: {min_levels})"
            )
        except Exception as e:
            return ValidationResult(False, f"Error reading file: {e}")

    def has_element(self, filename: str, element: str) -> ValidationResult:
        """Check if Markdown file contains a specific element type."""
        file_path = self.project_path / filename
        if not file_path.exists():
            return ValidationResult(False, f"File not found: {filename}")

        try:
            content = file_path.read_text(encoding="utf-8")

            patterns = {
                "unordered_list": r"^[\s]*[-*+]\s+\S",
                "ordered_list": r"^[\s]*\d+\.\s+\S",
                "table": r"\|.*\|.*\|",
                "code_block": r"```",
                "link": r"\[.+\]\(.+\)",
                "image": r"!\[.+\]\(.+\)",
                "bold": r"\*\*[^*]+\*\*",
                "italic": r"(?<!\*)\*[^*]+\*(?!\*)",
                "task_list": r"^[\s]*-\s+\[[x ]\]",
            }

            if element not in patterns:
                return ValidationResult(
                    False,
                    f"Unknown element type: {element}"
                )

            pattern = patterns[element]
            if re.search(pattern, content, re.MULTILINE):
                return ValidationResult(
                    True,
                    f"Element found: {element}"
                )
            return ValidationResult(
                False,
                f"Element not found: {element}"
            )
        except Exception as e:
            return ValidationResult(False, f"Error reading file: {e}")

    def has_section(self, filename: str, section_name: str) -> ValidationResult:
        """Check if Markdown file has a section with given name."""
        file_path = self.project_path / filename
        if not file_path.exists():
            return ValidationResult(False, f"File not found: {filename}")

        try:
            content = file_path.read_text(encoding="utf-8").lower()
            section_lower = section_name.lower()

            # Look for heading with section name
            pattern = rf"^#+\s+.*{section_lower}"
            if re.search(pattern, content, re.MULTILINE):
                return ValidationResult(
                    True,
                    f"Section found: {section_name}"
                )
            return ValidationResult(
                False,
                f"Section not found: {section_name}"
            )
        except Exception as e:
            return ValidationResult(False, f"Error reading file: {e}")

    def markdown_valid(self, filename: str) -> ValidationResult:
        """Basic check that Markdown syntax is valid."""
        file_path = self.project_path / filename
        if not file_path.exists():
            return ValidationResult(False, f"File not found: {filename}")

        try:
            content = file_path.read_text(encoding="utf-8")
            issues = []

            # Check for unclosed code blocks
            code_blocks = content.count("```")
            if code_blocks % 2 != 0:
                issues.append("Unclosed code block")

            # Check for unclosed bold
            bold_count = len(re.findall(r"\*\*", content))
            if bold_count % 2 != 0:
                issues.append("Unclosed bold formatting")

            if issues:
                return ValidationResult(
                    False,
                    "Markdown syntax issues found",
                    details=", ".join(issues)
                )
            return ValidationResult(True, "Markdown syntax OK")
        except Exception as e:
            return ValidationResult(False, f"Error reading file: {e}")

    def license_valid(self, filename: str = "LICENSE") -> ValidationResult:
        """Check if LICENSE file contains a valid license."""
        file_path = self.project_path / filename
        if not file_path.exists():
            return ValidationResult(False, f"File not found: {filename}")

        try:
            content = file_path.read_text(encoding="utf-8").lower()
            known_licenses = [
                "mit license",
                "apache license",
                "gnu general public license",
                "bsd license",
                "mozilla public license",
                "unlicense",
                "creative commons",
            ]

            for license_text in known_licenses:
                if license_text in content:
                    return ValidationResult(
                        True,
                        "Valid license found"
                    )

            return ValidationResult(
                False,
                "No recognized license found"
            )
        except Exception as e:
            return ValidationResult(False, f"Error reading file: {e}")

    def changelog_format(self, filename: str = "CHANGELOG.md") -> ValidationResult:
        """Check if CHANGELOG follows Keep a Changelog format."""
        file_path = self.project_path / filename
        if not file_path.exists():
            return ValidationResult(False, f"File not found: {filename}")

        try:
            content = file_path.read_text(encoding="utf-8")

            # Check for required elements
            checks = [
                ("# Changelog" in content or "# CHANGELOG" in content, "Has title"),
                ("[Unreleased]" in content or "[unreleased]" in content, "Has Unreleased section"),
                (bool(re.search(r"\[[\d.]+\]", content)), "Has version section"),
            ]

            failed = [msg for passed, msg in checks if not passed]
            if failed:
                return ValidationResult(
                    False,
                    "Changelog format issues",
                    details=f"Missing: {', '.join(failed)}"
                )
            return ValidationResult(True, "Changelog format OK")
        except Exception as e:
            return ValidationResult(False, f"Error reading file: {e}")

    def adr_format(self, filename: str) -> ValidationResult:
        """Check if file follows ADR format."""
        file_path = self.project_path / filename
        if not file_path.exists():
            return ValidationResult(False, f"File not found: {filename}")

        try:
            content = file_path.read_text(encoding="utf-8").lower()
            required_sections = ["status", "context", "decision"]
            optional_sections = ["rationale", "consequences"]

            missing = []
            for section in required_sections:
                if section not in content:
                    missing.append(section)

            if missing:
                return ValidationResult(
                    False,
                    "ADR format issues",
                    details=f"Missing sections: {', '.join(missing)}"
                )
            return ValidationResult(True, "ADR format OK")
        except Exception as e:
            return ValidationResult(False, f"Error reading file: {e}")

    def no_placeholder_text(self, filename: str) -> ValidationResult:
        """Check that file doesn't contain common placeholder text."""
        file_path = self.project_path / filename
        if not file_path.exists():
            return ValidationResult(False, f"File not found: {filename}")

        try:
            content = file_path.read_text(encoding="utf-8").lower()
            placeholders = [
                "todo",
                "tbd",
                "lorem ipsum",
                "example.com",
                "your name here",
                "placeholder",
                "fill this in",
            ]

            found = []
            for placeholder in placeholders:
                if placeholder in content:
                    found.append(placeholder)

            if found:
                return ValidationResult(
                    False,
                    "Placeholder text found",
                    details=f"Found: {', '.join(found)}"
                )
            return ValidationResult(True, "No placeholder text found")
        except Exception as e:
            return ValidationResult(False, f"Error reading file: {e}")

    def count_pattern(self, filename: str, pattern: str, min_count: int) -> ValidationResult:
        """Count occurrences of a regex pattern in file."""
        file_path = self.project_path / filename
        if not file_path.exists():
            return ValidationResult(False, f"File not found: {filename}")

        try:
            content = file_path.read_text(encoding="utf-8")
            matches = re.findall(pattern, content, re.IGNORECASE | re.MULTILINE)
            count = len(matches)

            if count >= min_count:
                return ValidationResult(
                    True,
                    f"Pattern count OK: {count} (min: {min_count})"
                )
            return ValidationResult(
                False,
                f"Pattern count too low: {count} (min: {min_count})"
            )
        except Exception as e:
            return ValidationResult(False, f"Error reading file: {e}")


def validate_project(project_path: str, checks: list[dict]) -> list[ValidationResult]:
    """Run a list of validation checks on a project.

    Args:
        project_path: Path to the project directory
        checks: List of check configurations, each with:
            - check: Name of validation method
            - args: Arguments for the method
            - error_message: Custom error message (optional)

    Returns:
        List of ValidationResult objects
    """
    validator = ProjectValidator(project_path)
    results = []

    for check_config in checks:
        check_name = check_config.get("check", "")
        args = check_config.get("args", [])

        # Parse check string like "file_exists('README.md')"
        if "(" in check_name:
            match = re.match(r"(\w+)\((.*)\)", check_name)
            if match:
                method_name = match.group(1)
                args_str = match.group(2)
                # Parse arguments
                args = [
                    arg.strip().strip("'\"")
                    for arg in args_str.split(",")
                    if arg.strip()
                ]

                if hasattr(validator, method_name):
                    method = getattr(validator, method_name)
                    # Convert numeric arguments
                    converted_args = []
                    for arg in args:
                        try:
                            converted_args.append(int(arg))
                        except ValueError:
                            converted_args.append(arg)

                    try:
                        result = method(*converted_args)
                        results.append(result)
                    except Exception as e:
                        results.append(
                            ValidationResult(False, f"Check failed: {e}")
                        )
                else:
                    results.append(
                        ValidationResult(False, f"Unknown check: {method_name}")
                    )

    return results
