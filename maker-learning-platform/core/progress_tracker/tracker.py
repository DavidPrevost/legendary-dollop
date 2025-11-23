"""Progress tracking for the Maker Learning Platform.

This module manages user progress through subjects and projects,
storing data locally as JSON.
"""

import json
from dataclasses import dataclass, asdict
from datetime import datetime
from pathlib import Path
from typing import Optional


@dataclass
class ProjectCompletion:
    """Record of a completed project."""
    project_id: str
    completed_at: str
    time_spent_minutes: Optional[int] = None
    notes: Optional[str] = None


@dataclass
class SubjectProgress:
    """Progress within a single subject."""
    subject_id: str
    current_level: int
    level_name: str
    started_at: str
    last_activity: str
    completed_projects: list[str]
    concepts_completed: list[int]
    assessment_taken: bool = False
    assessment_level: Optional[int] = None


@dataclass
class UserProgress:
    """Complete progress for a user."""
    user_id: str
    created_at: str
    last_updated: str
    subjects: dict[str, SubjectProgress]
    completed_projects: list[ProjectCompletion]
    total_time_minutes: int = 0


class ProgressTracker:
    """Tracks user progress through the Maker Learning Platform."""

    def __init__(self, data_dir: str = ".maker-data"):
        self.data_dir = Path(data_dir)
        self.data_dir.mkdir(exist_ok=True)
        self.progress_file = self.data_dir / "progress.json"
        self.progress: Optional[UserProgress] = None
        self._load_progress()

    def _load_progress(self):
        """Load progress from file or create new."""
        if self.progress_file.exists():
            try:
                data = json.loads(self.progress_file.read_text())
                self.progress = self._dict_to_progress(data)
            except Exception as e:
                print(f"Error loading progress: {e}")
                self.progress = None

        if not self.progress:
            self.progress = UserProgress(
                user_id="default",
                created_at=datetime.now().isoformat(),
                last_updated=datetime.now().isoformat(),
                subjects={},
                completed_projects=[],
            )
            self._save_progress()

    def _dict_to_progress(self, data: dict) -> UserProgress:
        """Convert dictionary to UserProgress object."""
        subjects = {}
        for sid, sdata in data.get("subjects", {}).items():
            subjects[sid] = SubjectProgress(**sdata)

        projects = []
        for pdata in data.get("completed_projects", []):
            projects.append(ProjectCompletion(**pdata))

        return UserProgress(
            user_id=data.get("user_id", "default"),
            created_at=data.get("created_at", datetime.now().isoformat()),
            last_updated=data.get("last_updated", datetime.now().isoformat()),
            subjects=subjects,
            completed_projects=projects,
            total_time_minutes=data.get("total_time_minutes", 0),
        )

    def _save_progress(self):
        """Save progress to file."""
        if not self.progress:
            return

        data = {
            "user_id": self.progress.user_id,
            "created_at": self.progress.created_at,
            "last_updated": datetime.now().isoformat(),
            "subjects": {
                sid: asdict(sp) for sid, sp in self.progress.subjects.items()
            },
            "completed_projects": [
                asdict(pc) for pc in self.progress.completed_projects
            ],
            "total_time_minutes": self.progress.total_time_minutes,
        }

        self.progress_file.write_text(json.dumps(data, indent=2))

    def start_subject(self, subject_id: str, level_names: dict[int, str]) -> SubjectProgress:
        """Start tracking a new subject.

        Args:
            subject_id: ID of the subject
            level_names: Mapping of level numbers to names

        Returns:
            SubjectProgress for the subject
        """
        if subject_id not in self.progress.subjects:
            now = datetime.now().isoformat()
            self.progress.subjects[subject_id] = SubjectProgress(
                subject_id=subject_id,
                current_level=0,
                level_name=level_names.get(0, "Curious"),
                started_at=now,
                last_activity=now,
                completed_projects=[],
                concepts_completed=[],
            )
            self._save_progress()

        return self.progress.subjects[subject_id]

    def get_subject_progress(self, subject_id: str) -> Optional[SubjectProgress]:
        """Get progress for a specific subject."""
        return self.progress.subjects.get(subject_id)

    def complete_concept(self, subject_id: str, concept_id: int):
        """Mark a concept as completed.

        Args:
            subject_id: ID of the subject
            concept_id: ID of the concept
        """
        if subject_id in self.progress.subjects:
            subject = self.progress.subjects[subject_id]
            if concept_id not in subject.concepts_completed:
                subject.concepts_completed.append(concept_id)
                subject.last_activity = datetime.now().isoformat()
                self._save_progress()

    def complete_project(
        self,
        subject_id: str,
        project_id: str,
        level_names: dict[int, str],
        new_level: Optional[int] = None,
        time_spent: Optional[int] = None,
        notes: Optional[str] = None,
    ):
        """Record project completion.

        Args:
            subject_id: ID of the subject
            project_id: ID of the completed project
            level_names: Mapping of level numbers to names
            new_level: New level after completion (if leveling up)
            time_spent: Time spent in minutes
            notes: Optional notes about the project
        """
        if subject_id not in self.progress.subjects:
            return

        subject = self.progress.subjects[subject_id]
        now = datetime.now().isoformat()

        # Record the completion
        if project_id not in subject.completed_projects:
            subject.completed_projects.append(project_id)

        completion = ProjectCompletion(
            project_id=project_id,
            completed_at=now,
            time_spent_minutes=time_spent,
            notes=notes,
        )
        self.progress.completed_projects.append(completion)

        if time_spent:
            self.progress.total_time_minutes += time_spent

        # Level up if specified
        if new_level is not None and new_level > subject.current_level:
            subject.current_level = new_level
            subject.level_name = level_names.get(new_level, f"Level {new_level}")

        subject.last_activity = now
        self._save_progress()

    def record_assessment(
        self,
        subject_id: str,
        assessed_level: int,
        level_names: dict[int, str],
    ):
        """Record placement assessment result.

        Args:
            subject_id: ID of the subject
            assessed_level: Level determined by assessment
            level_names: Mapping of level numbers to names
        """
        if subject_id in self.progress.subjects:
            subject = self.progress.subjects[subject_id]
            subject.assessment_taken = True
            subject.assessment_level = assessed_level

            # Set current level to assessed level if higher
            if assessed_level > subject.current_level:
                subject.current_level = assessed_level
                subject.level_name = level_names.get(
                    assessed_level, f"Level {assessed_level}"
                )

            self._save_progress()

    def get_summary(self) -> dict:
        """Get a summary of overall progress.

        Returns:
            Dictionary with progress summary
        """
        subjects_started = len(self.progress.subjects)
        total_projects = len(self.progress.completed_projects)
        total_concepts = sum(
            len(s.concepts_completed)
            for s in self.progress.subjects.values()
        )

        # Count by band
        bands = {"Novice": 0, "Competent": 0, "Proficient": 0, "Expert": 0}
        for subject in self.progress.subjects.values():
            level = subject.current_level
            if level <= 1:
                bands["Novice"] += 1
            elif level <= 3:
                bands["Competent"] += 1
            elif level <= 5:
                bands["Proficient"] += 1
            else:
                bands["Expert"] += 1

        return {
            "subjects_started": subjects_started,
            "total_projects_completed": total_projects,
            "total_concepts_learned": total_concepts,
            "total_time_hours": round(self.progress.total_time_minutes / 60, 1),
            "bands": bands,
            "last_activity": self.progress.last_updated,
        }

    def get_subject_list(self) -> list[dict]:
        """Get list of all subjects with progress.

        Returns:
            List of subject progress summaries
        """
        return [
            {
                "subject_id": s.subject_id,
                "current_level": s.current_level,
                "level_name": s.level_name,
                "projects_completed": len(s.completed_projects),
                "concepts_completed": len(s.concepts_completed),
                "last_activity": s.last_activity,
            }
            for s in self.progress.subjects.values()
        ]
