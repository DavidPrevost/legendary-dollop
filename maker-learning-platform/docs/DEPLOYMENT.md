# Maker Learning Platform - Deployment Instructions

## Prerequisites

- Python 3.10 or higher
- pip (Python package manager)

## Installation

### 1. Clone or Download

```bash
git clone <repository-url>
cd maker-learning-platform
```

Or download and extract the ZIP file.

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

Required packages:
- `click` - CLI framework
- `rich` - Terminal formatting

### 3. Verify Installation

```bash
python -m platform.cli.main --version
```

Should display: `Maker Learning Platform, version 0.1.0`

## Usage

### Check System Capabilities

```bash
python -m platform.cli.main check
```

Shows your installed tools and what projects you can work on.

### View Available Subjects

```bash
python -m platform.cli.main subjects
```

Lists subjects with level counts and time estimates.

### Take Placement Assessment

```bash
python -m platform.cli.main assess project-foundations
```

Answer questions to find your starting level.

### Check Progress

```bash
python -m platform.cli.main status
```

Shows your overall progress and subject completion.

### Explore Learning Paths

```bash
python -m platform.cli.main explore
```

Browse available tracks and projects.

## Available Subjects

### Project Foundations (Complete)

Documentation and planning skills for all makers.

- **Levels**: 5 (Curious → Maker)
- **Time**: 15-23 hours
- **Concepts**: 255

Content location: `content/topics/project-foundations/`

**Includes:**
- 11 tutorial modules
- 5 milestone projects
- Placement assessment (14 questions)
- Project validation system
- Progress tracking

## Data Storage

User progress is stored locally in `.maker-data/progress.json`.

This file tracks:
- Subject progress
- Completed projects
- Assessment results
- Time spent

## Directory Structure

```
maker-learning-platform/
├── core/                    # Core functionality
│   ├── capability_checker/  # System detection
│   ├── progress_tracker/    # Progress & assessments
│   └── project_validator/   # Project validation
├── content/                 # Learning content
│   └── topics/
│       └── project-foundations/
│           ├── tutorials/   # 11 modules
│           └── projects/    # 5 project YAMLs
├── platform/
│   └── cli/                 # Command-line interface
└── docs/                    # Documentation
```

## Offline Usage

The platform works completely offline. All content is included locally.

For offline distribution:
1. Package the entire `maker-learning-platform` directory
2. Include Python installer for target OS
3. User runs installation steps above

## Troubleshooting

### Import Errors

Ensure you run commands from the `maker-learning-platform` directory:

```bash
cd maker-learning-platform
python -m platform.cli.main check
```

### Missing Dependencies

```bash
pip install click rich
```

### Python Version

Check your Python version:

```bash
python --version
```

Requires 3.10+. On some systems, use `python3` instead of `python`.

## Development

### Running Tests

```bash
python -m pytest tests/
```

### Validating Code

```bash
python -m py_compile core/project_validator/validator.py
python -m py_compile core/progress_tracker/tracker.py
python -m py_compile core/progress_tracker/assessments.py
python -m py_compile platform/cli/main.py
```

### Adding New Subjects

1. Create content in `content/topics/<subject-name>/`
2. Add tutorials, projects, and validation rules
3. Register in CLI's `subjects` command
4. Add assessment questions to `assessments.py`

## Version

Current version: 0.1.0

Subject 1 (Project Foundations) complete.
