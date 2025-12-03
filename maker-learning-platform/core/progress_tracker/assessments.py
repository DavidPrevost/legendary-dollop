"""Assessment tools for the Maker Learning Platform.

This module provides placement assessments that allow users to
demonstrate existing knowledge and skip levels.
"""

import random
from dataclasses import dataclass
from typing import Optional


@dataclass
class Question:
    """A single assessment question."""
    id: str
    text: str
    options: list[str]
    correct_index: int
    level: int
    concept: str
    explanation: str


@dataclass
class AssessmentResult:
    """Result of a completed assessment."""
    total_questions: int
    correct_answers: int
    percentage: float
    recommended_level: int
    level_name: str
    details: dict


class PlacementAssessment:
    """Placement assessment for Project Foundations subject."""

    def __init__(self):
        self.questions = self._load_questions()
        self.level_names = {
            0: "Curious",
            1: "Explorer",
            2: "Tinkerer",
            3: "Builder",
            4: "Maker",
        }

    def _load_questions(self) -> list[Question]:
        """Load assessment questions for Project Foundations."""
        return [
            # Level 0 questions (Platform basics)
            Question(
                id="pf-0-1",
                text="What is the difference between a 'Language' and a 'Topic' in this platform?",
                options=[
                    "Languages are harder than Topics",
                    "Languages are programming languages, Topics are other technical knowledge",
                    "Topics take longer to learn",
                    "There is no difference",
                ],
                correct_index=1,
                level=0,
                concept="Languages vs Topics distinction",
                explanation="Languages refer to programming/markup languages like Python or HTML, while Topics are other technical knowledge areas like Git or Networking."
            ),
            Question(
                id="pf-0-2",
                text="What is 'minimum viable documentation'?",
                options=[
                    "The longest possible documentation",
                    "Documentation that only developers can read",
                    "The essential docs needed to understand and use a project",
                    "Documentation written in Markdown only",
                ],
                correct_index=2,
                level=0,
                concept="Minimum viable documentation",
                explanation="Minimum viable documentation includes: what it does, how to run it, requirements, and configuration options."
            ),

            # Level 1 questions (Markdown)
            Question(
                id="pf-1-1",
                text="Which Markdown syntax creates a code block with syntax highlighting for Python?",
                options=[
                    "```python",
                    "[python]",
                    "<code python>",
                    "{{python}}",
                ],
                correct_index=0,
                level=1,
                concept="Syntax highlighting",
                explanation="Use triple backticks followed by the language name: ```python"
            ),
            Question(
                id="pf-1-2",
                text="How do you create a task list item in GitHub-flavored Markdown?",
                options=[
                    "[ ] Task",
                    "- [ ] Task",
                    "* Task []",
                    "<task> Task",
                ],
                correct_index=1,
                level=1,
                concept="Task lists",
                explanation="Task lists use - [ ] for incomplete and - [x] for complete items."
            ),
            Question(
                id="pf-1-3",
                text="What is the correct Markdown for a table?",
                options=[
                    "| Col1 | Col2 |\\n|---|---|\\n| A | B |",
                    "<table><tr><td>A</td></tr></table>",
                    "[table: Col1, Col2]",
                    "{{Col1, Col2}, {A, B}}",
                ],
                correct_index=0,
                level=1,
                concept="Tables",
                explanation="Tables use pipes (|) to separate columns and hyphens (-) for the header separator."
            ),

            # Level 2 questions (README & Structure)
            Question(
                id="pf-2-1",
                text="Which section should come first in a project README?",
                options=[
                    "Contributing guidelines",
                    "License information",
                    "Project title and description",
                    "Changelog",
                ],
                correct_index=2,
                level=2,
                concept="README structure",
                explanation="Start with the project name and a clear description of what it does and why."
            ),
            Question(
                id="pf-2-2",
                text="Where should configuration files typically be placed?",
                options=[
                    "In a config/ subdirectory",
                    "At the project root",
                    "In the docs/ directory",
                    "In the src/ directory",
                ],
                correct_index=1,
                level=2,
                concept="Project structure",
                explanation="Configuration files live at the project root for easy discovery."
            ),
            Question(
                id="pf-2-3",
                text="What does a .gitignore file do?",
                options=[
                    "Lists contributors to ignore",
                    "Specifies files that Git should not track",
                    "Ignores certain Git commands",
                    "Hides the .git directory",
                ],
                correct_index=1,
                level=2,
                concept=".gitignore",
                explanation=".gitignore tells Git which files/folders to exclude from version control."
            ),

            # Level 3 questions (Planning)
            Question(
                id="pf-3-1",
                text="What does 'MoSCoW' stand for in prioritization?",
                options=[
                    "Most Optimal Solution, Correct Order, Winning",
                    "Must have, Should have, Could have, Won't have",
                    "Minimum Output, Standard Count, Optional Work",
                    "Major, Secondary, Component, Worker",
                ],
                correct_index=1,
                level=3,
                concept="MoSCoW prioritization",
                explanation="MoSCoW categorizes requirements: Must, Should, Could, Won't have."
            ),
            Question(
                id="pf-3-2",
                text="What is a 'walking skeleton' approach?",
                options=[
                    "Writing documentation first",
                    "Building minimal end-to-end functionality first",
                    "Creating a project outline",
                    "Testing on Halloween",
                ],
                correct_index=1,
                level=3,
                concept="Walking skeleton",
                explanation="A walking skeleton is a minimal implementation that connects all components end-to-end."
            ),
            Question(
                id="pf-3-3",
                text="What should user story acceptance criteria be?",
                options=[
                    "Vague and flexible",
                    "As long as possible",
                    "Testable and specific",
                    "Written in code",
                ],
                correct_index=2,
                level=3,
                concept="Acceptance criteria",
                explanation="Acceptance criteria must be specific and testable so you know when the story is done."
            ),

            # Level 4 questions (Technical Documentation)
            Question(
                id="pf-4-1",
                text="What sections must an Architecture Decision Record (ADR) contain?",
                options=[
                    "Title, Author, Date",
                    "Status, Context, Decision",
                    "Summary, Details, References",
                    "Problem, Solution, Result",
                ],
                correct_index=1,
                level=4,
                concept="ADR format",
                explanation="ADRs must have: Status, Context, Decision. Rationale and Consequences are recommended."
            ),
            Question(
                id="pf-4-2",
                text="What does 'MAJOR' version bump mean in semantic versioning?",
                options=[
                    "Bug fixes only",
                    "New features, backward compatible",
                    "Breaking changes",
                    "Documentation updates",
                ],
                correct_index=2,
                level=4,
                concept="Semantic versioning",
                explanation="MAJOR version bumps indicate breaking, backward-incompatible changes."
            ),
            Question(
                id="pf-4-3",
                text="What's the main benefit of 'docs as code'?",
                options=[
                    "Docs load faster",
                    "Docs are reviewed and versioned like code",
                    "Docs can be written in any language",
                    "Docs don't need updating",
                ],
                correct_index=1,
                level=4,
                concept="Documentation as code",
                explanation="Treating docs as code means they're version controlled, reviewed in PRs, and kept with the codebase."
            ),
        ]

    def get_assessment_questions(self, num_questions: int = 10) -> list[Question]:
        """Get a randomized set of questions across all levels.

        Args:
            num_questions: Number of questions to include

        Returns:
            List of Question objects
        """
        # Ensure we have questions from each level
        questions_by_level: dict[int, list[Question]] = {}
        for q in self.questions:
            if q.level not in questions_by_level:
                questions_by_level[q.level] = []
            questions_by_level[q.level].append(q)

        selected = []

        # Select roughly equal questions from each level
        per_level = max(1, num_questions // len(questions_by_level))
        for level in sorted(questions_by_level.keys()):
            level_questions = questions_by_level[level]
            count = min(per_level, len(level_questions))
            selected.extend(random.sample(level_questions, count))

        # Fill remaining slots randomly
        while len(selected) < num_questions and len(selected) < len(self.questions):
            remaining = [q for q in self.questions if q not in selected]
            if remaining:
                selected.append(random.choice(remaining))

        random.shuffle(selected)
        return selected[:num_questions]

    def evaluate_assessment(
        self, answers: dict[str, int]
    ) -> AssessmentResult:
        """Evaluate assessment answers and determine recommended level.

        Args:
            answers: Dict mapping question_id to selected option index

        Returns:
            AssessmentResult with score and recommended level
        """
        correct = 0
        level_scores: dict[int, dict] = {
            i: {"correct": 0, "total": 0} for i in range(5)
        }

        for question in self.questions:
            if question.id in answers:
                level_scores[question.level]["total"] += 1
                if answers[question.id] == question.correct_index:
                    correct += 1
                    level_scores[question.level]["correct"] += 1

        total = len(answers)
        percentage = (correct / total * 100) if total > 0 else 0

        # Determine recommended level based on performance
        recommended_level = 0
        for level in range(5):
            scores = level_scores[level]
            if scores["total"] > 0:
                level_pct = scores["correct"] / scores["total"]
                if level_pct >= 0.7:  # 70% threshold to pass a level
                    recommended_level = level + 1
                else:
                    break

        # Cap at max level
        recommended_level = min(recommended_level, 4)

        return AssessmentResult(
            total_questions=total,
            correct_answers=correct,
            percentage=percentage,
            recommended_level=recommended_level,
            level_name=self.level_names[recommended_level],
            details={
                "level_scores": {
                    self.level_names[k]: v for k, v in level_scores.items()
                }
            }
        )


class CommandLineAssessment:
    """Placement assessment for Command Line Mastery subject."""

    def __init__(self):
        self.questions = self._load_questions()
        self.level_names = {
            0: "Curious",
            1: "Explorer",
            2: "Tinkerer",
            3: "Builder",
            4: "Maker",
        }

    def _load_questions(self) -> list[Question]:
        """Load assessment questions for Command Line Mastery."""
        return [
            # Level 0 questions (Terminal basics)
            Question(
                id="cli-0-1",
                text="What command shows your current directory?",
                options=["pwd", "cd", "ls", "dir"],
                correct_index=0,
                level=0,
                concept="Print working directory",
                explanation="pwd (print working directory) shows your current location in the file system."
            ),
            Question(
                id="cli-0-2",
                text="What does the ~ symbol represent in a path?",
                options=[
                    "Root directory",
                    "Previous directory",
                    "Home directory",
                    "Temporary directory",
                ],
                correct_index=2,
                level=0,
                concept="Home directory shortcut",
                explanation="The tilde (~) is a shortcut for your home directory."
            ),
            Question(
                id="cli-0-3",
                text="How do you go up one directory level?",
                options=["cd ..", "cd /", "cd ~", "cd -"],
                correct_index=0,
                level=0,
                concept="Parent directory",
                explanation="cd .. moves up to the parent directory."
            ),

            # Level 1 questions (File operations)
            Question(
                id="cli-1-1",
                text="What does 'chmod 755 script.sh' do?",
                options=[
                    "Deletes the file",
                    "Makes it executable for all, writable only for owner",
                    "Makes it read-only",
                    "Hides the file",
                ],
                correct_index=1,
                level=1,
                concept="File permissions",
                explanation="755 = rwxr-xr-x: owner can read/write/execute, others can read/execute."
            ),
            Question(
                id="cli-1-2",
                text="What flag makes 'cp' copy directories recursively?",
                options=["-r", "-f", "-a", "-v"],
                correct_index=0,
                level=1,
                concept="Recursive copy",
                explanation="cp -r copies directories and their contents recursively."
            ),
            Question(
                id="cli-1-3",
                text="Which command shows the last 10 lines of a file?",
                options=["head", "tail", "less", "cat"],
                correct_index=1,
                level=1,
                concept="Viewing file end",
                explanation="tail shows the last lines of a file (default 10)."
            ),

            # Level 2 questions (Search and text processing)
            Question(
                id="cli-2-1",
                text="What does 'grep -r' do?",
                options=[
                    "Reverse the output",
                    "Search recursively in directories",
                    "Use regular expressions",
                    "Show only count",
                ],
                correct_index=1,
                level=2,
                concept="Recursive grep",
                explanation="grep -r searches through all files in a directory recursively."
            ),
            Question(
                id="cli-2-2",
                text="What must you do before using 'uniq' effectively?",
                options=[
                    "Make the file executable",
                    "Sort the input",
                    "Convert to lowercase",
                    "Remove blank lines",
                ],
                correct_index=1,
                level=2,
                concept="Uniq prerequisites",
                explanation="uniq only removes consecutive duplicates, so sort first."
            ),
            Question(
                id="cli-2-3",
                text="What regex matches lines starting with 'Error'?",
                options=["Error$", "^Error", "*Error", "Error*"],
                correct_index=1,
                level=2,
                concept="Regex anchors",
                explanation="^ anchors to the start of line, so ^Error matches lines beginning with Error."
            ),

            # Level 3 questions (Pipes and environment)
            Question(
                id="cli-3-1",
                text="What does '2>&1' do in a command?",
                options=[
                    "Runs the command twice",
                    "Redirects stderr to stdout",
                    "Creates two output files",
                    "Waits 2 seconds then runs",
                ],
                correct_index=1,
                level=3,
                concept="Stream redirection",
                explanation="2>&1 redirects stderr (2) to the same place as stdout (1)."
            ),
            Question(
                id="cli-3-2",
                text="Where do you put persistent aliases?",
                options=[
                    "/etc/aliases",
                    "~/.bashrc or ~/.zshrc",
                    "~/.profile.d",
                    "/usr/local/aliases",
                ],
                correct_index=1,
                level=3,
                concept="Shell configuration",
                explanation="Aliases go in your shell config file (.bashrc for bash, .zshrc for zsh)."
            ),
            Question(
                id="cli-3-3",
                text="What signal does 'kill -9' send?",
                options=["SIGTERM", "SIGHUP", "SIGKILL", "SIGINT"],
                correct_index=2,
                level=3,
                concept="Kill signals",
                explanation="kill -9 sends SIGKILL, which forcefully terminates a process."
            ),

            # Level 4 questions (Scripting and networking)
            Question(
                id="cli-4-1",
                text="What does 'set -e' do in a bash script?",
                options=[
                    "Enables echo mode",
                    "Exits on first error",
                    "Exports all variables",
                    "Enables extended globbing",
                ],
                correct_index=1,
                level=4,
                concept="Script error handling",
                explanation="set -e makes the script exit immediately if any command fails."
            ),
            Question(
                id="cli-4-2",
                text="How do you send a POST request with curl?",
                options=[
                    "curl --post",
                    "curl -X POST",
                    "curl -P",
                    "curl -post-data",
                ],
                correct_index=1,
                level=4,
                concept="HTTP methods with curl",
                explanation="curl -X POST specifies the HTTP method as POST."
            ),
            Question(
                id="cli-4-3",
                text="What does '$!' represent in bash?",
                options=[
                    "Last exit code",
                    "PID of last background process",
                    "Current script name",
                    "Number of arguments",
                ],
                correct_index=1,
                level=4,
                concept="Special variables",
                explanation="$! contains the PID of the most recent background process."
            ),
        ]

    def calculate_level(self, correct: int, total: int) -> AssessmentResult:
        """Calculate recommended level based on score."""
        percentage = (correct / total * 100) if total > 0 else 0

        if percentage >= 90:
            level = 4
        elif percentage >= 75:
            level = 3
        elif percentage >= 60:
            level = 2
        elif percentage >= 40:
            level = 1
        else:
            level = 0

        return AssessmentResult(
            total_questions=total,
            correct_answers=correct,
            percentage=percentage,
            recommended_level=level,
            level_name=self.level_names[level],
            details={"score": correct, "total": total}
        )


def run_placement_assessment() -> AssessmentResult:
    """Run an interactive placement assessment.

    This is a simple implementation for CLI use.
    """
    assessment = PlacementAssessment()
    questions = assessment.get_assessment_questions(10)

    print("\n=== Project Foundations Placement Assessment ===\n")
    print("Answer the following questions to determine your starting level.")
    print("This should take about 5-10 minutes.\n")

    answers = {}

    for i, question in enumerate(questions, 1):
        print(f"\nQuestion {i}/{len(questions)}")
        print(f"{question.text}\n")

        for j, option in enumerate(question.options):
            print(f"  {j + 1}. {option}")

        while True:
            try:
                choice = input("\nYour answer (1-4): ").strip()
                choice_int = int(choice) - 1
                if 0 <= choice_int <= 3:
                    answers[question.id] = choice_int
                    break
                print("Please enter a number between 1 and 4.")
            except ValueError:
                print("Please enter a valid number.")

    result = assessment.evaluate_assessment(answers)

    print("\n=== Assessment Results ===\n")
    print(f"Score: {result.correct_answers}/{result.total_questions} ({result.percentage:.0f}%)")
    print(f"Recommended starting level: {result.level_name} (Level {result.recommended_level})")

    return result
