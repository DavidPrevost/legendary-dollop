# Platform Terminology

Consistent terminology for the Maker Learning Platform. Use these terms in code, documentation, and UI.

---

## Core Concepts

### Subject
An umbrella term for anything a user can learn on the platform. Subjects are divided into two categories:

- **Language**: A programming, markup, or configuration language (Python, HTML, YAML)
- **Topic**: Technical knowledge that isn't a language (Git, Networking, Home Automation)

**Usage**: "Python is a Subject" / "The user has completed 5 Subjects"

### Level
A measure of proficiency within a single Subject. Levels are numbered (0, 1, 2...) and named (Curious, Explorer, Tinkerer...).

- **Level Number**: The numeric value (0-6 typical, varies by Subject)
- **Level Name**: The human-readable name (e.g., "Builder")
- **Band**: A grouping of levels for cross-Subject comparison (Novice, Competent, Proficient, Expert)

**Usage**: "You're at Python Level 3 (Builder)" / "You're in the Proficient band"

### Project
A practical exercise that teaches skills and produces something useful. Projects belong to Subjects at specific Levels.

- **Milestone Project**: A project that marks completion of a Level
- **Integration Project**: A project that requires multiple Subjects
- **Extension**: An optional enhancement to a completed project

**Usage**: "Complete the File Organizer project to reach Level 2"

---

## User Journey Terms

### Track
The path a user takes through a Subject. Currently two tracks exist:

- **Hobbyist Track**: Tinkerer → Builder → Maker (breadth-focused, practical)
- **Professional Track**: Extends beyond Maker with specializations (future)

**Usage**: "You're on the Hobbyist Track for Python"

### Path
A curated sequence of Subjects and Projects for a specific goal.

**Usage**: "The Homelab Journey path" / "The Automation Master path"

### Capability
A hardware or software resource available to the user.

**Usage**: "Your capabilities include Docker and a Raspberry Pi"

### Progress
The user's advancement through Subjects, Levels, and Projects.

**Usage**: "Your progress shows 3 completed Subjects"

---

## Level Names by Band

These are the default level names. Subjects may customize names while staying within bands.

| Band | Typical Levels | Default Names | Description |
|------|----------------|---------------|-------------|
| **Novice** | 0-1 | Curious, Explorer | Following tutorials, basic syntax |
| **Competent** | 2-3 | Tinkerer, Builder | Modifying code, building from scratch |
| **Proficient** | 4-5 | Maker, Architect | Complex projects, system design |
| **Expert** | 6+ | Mentor | Teaching, contributing |

---

## Technical Terms

### Dependency
A relationship between Subjects.

- **Hard Dependency**: Required to function (rare, mostly for integrations)
- **Soft Dependency**: Recommended for easier learning
- **Enhancement**: Makes something better but isn't needed

### Placement Assessment
A test that allows users to skip Levels they already know.

### Capability Detection
Automatic discovery of user's hardware and software.

### Shopping List
A list of hardware/software needed for selected Projects, minus what the user already has.

---

## UI/UX Terms

### Dashboard
The main user interface showing progress, recommendations, and quick actions.

### Skill Tree
Visual representation of Subjects and their relationships.

### Project Card
A summary view of a Project showing key details.

### Progress Bar
Visual indicator of advancement within a Level or Subject.

---

## Content Terms

### Curriculum
The structured content for a Subject across all Levels.

### Tutorial
Step-by-step instructions for completing a Project.

### Reference
Documentation for looking up syntax, commands, or concepts.

### Hint
Progressive help for stuck users (Level 1 = gentle, Level 3 = nearly the answer).

---

## Anti-Patterns (Don't Use)

| Don't Say | Say Instead | Why |
|-----------|-------------|-----|
| "Skill" (as a Subject) | "Subject" or "Topic" | Confusing - skills are what you gain |
| "Course" | "Subject" or "Path" | We're not a course platform |
| "Lesson" | "Project" or "Tutorial" | Too passive, we're project-based |
| "Student" | "User" or "Maker" | Aligns with our identity |
| "Test" | "Assessment" or "Validation" | Less academic connotation |
| "Fail" | "Not yet complete" | Growth mindset |
| "Beginner" (as level name) | "Curious" or "Explorer" | More inviting |

---

## Code Naming Conventions

Use these in code for consistency:

```python
# Models
Subject          # Not "Skill" or "Course"
Level            # Not "Stage" or "Tier"
Project          # Not "Exercise" or "Lesson"
Capability       # Not "Resource" or "Asset"

# Enums
SubjectCategory  # LANGUAGE, TOPIC
DependencyType   # HARD, SOFT, ENHANCES
Band             # NOVICE, COMPETENT, PROFICIENT, EXPERT

# Functions
detect_capabilities()      # Not "check_system()"
get_user_progress()        # Not "get_user_skills()"
validate_project()         # Not "test_project()"
```

---

## Adding New Terms

When introducing new terminology:

1. Check this document first - we may already have a term
2. Prefer plain English over jargon
3. Consider how it sounds to a "Curious" level user
4. Add it to this document with definition and usage example
5. Update code naming conventions if applicable
