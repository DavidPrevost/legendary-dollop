# Project Template

Use this template when adding a new project to the platform. Projects are the primary way users learn and demonstrate skills.

---

## Metadata

```yaml
project:
  id: ""                    # Unique identifier (e.g., "python-file-organizer")
  name: ""                  # Display name (e.g., "File Organizer")

  # Primary subject and level
  subject_id: ""            # e.g., "python"
  level: 0                  # Level this project belongs to

  description:
    short: ""               # One sentence (for lists)
    full: ""                # 2-3 paragraphs (for project page)

  # What they'll have when done
  outcome: ""               # e.g., "A script that sorts your Downloads folder by file type"
```

---

## Value Proposition

```yaml
value:
  # How does this improve daily life?
  life_improvement: ""      # Be specific and practical

  # Why this project at this level?
  learning_goals:
    - ""                    # What concepts/skills does this teach?
    - ""

  # What can they do after this that they couldn't before?
  unlocks:
    - ""
```

---

## Requirements

```yaml
requirements:
  # Primary subject/level
  primary:
    subject_id: ""
    min_level: 0            # Minimum level to attempt

  # Other subjects needed (for integration projects)
  integrations:
    - subject_id: ""
      min_level: 0
      usage: ""             # How this subject is used in the project

  # Soft prerequisites - helpful but not required
  recommended:
    - subject_id: ""
      reason: ""
```

---

## Hardware and Software

```yaml
environment:
  # Platform support
  platforms:
    windows: true
    macos: true
    linux: true

  # Platform-specific variants (if approach differs)
  variants:
    windows: null           # Describe Windows-specific approach
    macos: null
    linux: null

  # Required software (beyond standard dev setup)
  software_required:
    - name: ""
      install_notes: ""

  # Hardware requirements
  hardware_required: []     # Empty = laptop only

  # Optional hardware that enhances the project
  hardware_optional:
    - item: ""
      enhancement: ""       # What it adds to the project
      estimated_cost: ""
```

---

## Time and Difficulty

```yaml
estimates:
  time: ""                  # e.g., "2-4 hours"

  difficulty:
    overall: ""             # "beginner", "intermediate", "advanced"

    # Specific difficulty areas
    concepts: ""            # How hard are the concepts?
    implementation: ""      # How hard is the coding?
    debugging: ""           # How hard is troubleshooting?
```

---

## Safety and Legal

```yaml
safety:
  # Any legal/ethical considerations
  legal_notes: ""           # e.g., "Only scrape sites that permit it"

  # Security considerations
  security_notes: ""        # e.g., "Never commit API keys"

  # Things that could go wrong
  warnings:
    - ""
```

---

## Project Structure

```yaml
structure:
  # Files the user will create
  files:
    - path: ""              # e.g., "organizer.py"
      purpose: ""           # What this file does

  # Suggested folder structure
  directories:
    - path: ""
      purpose: ""

  # What the finished project looks like
  final_structure: |
    project-name/
    ├── file1.py
    └── README.md
```

---

## Success Criteria

How do we know the project is complete and working?

```yaml
validation:
  # Automated checks (for project validator)
  automated:
    - check: ""             # e.g., "file_exists('organizer.py')"
      error_message: ""

  # Manual verification
  manual:
    - ""                    # e.g., "Run the script and verify files are sorted"
    - ""

  # What "done" looks like
  definition_of_done: ""
```

---

## Hints and Common Issues

```yaml
support:
  # Common mistakes
  pitfalls:
    - issue: ""
      solution: ""

  # Hints for stuck users (progressive disclosure)
  hints:
    - level: 1              # Gentle nudge
      hint: ""
    - level: 2              # More specific
      hint: ""
    - level: 3              # Nearly the answer
      hint: ""
```

---

## Extensions

Optional enhancements for users who want to go further.

```yaml
extensions:
  - name: ""
    description: ""
    difficulty: ""          # Relative to base project
    skills_practiced:
      - ""
```

---

## Content Location

```yaml
content:
  # Where project files live
  template_path: ""         # e.g., "/content/languages/python/projects/file-organizer/"

  # Supplementary materials
  resources:
    - type: ""              # "tutorial", "reference", "video"
      title: ""
      location: ""
```

---

## Checklist Before Submitting

- [ ] Project produces something genuinely useful
- [ ] Life improvement is specific and believable
- [ ] Time estimate is realistic (test it!)
- [ ] All platforms tested or clearly marked unsupported
- [ ] Prerequisites are accurate
- [ ] Success criteria are testable
- [ ] Common pitfalls documented
- [ ] Extensions provide meaningful growth
- [ ] Safety/legal notes included if applicable
