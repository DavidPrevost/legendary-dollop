# Subject Template

Use this template when adding a new Language or Topic to the platform. Copy this file and fill in all sections.

---

## Metadata

```yaml
subject:
  id: ""                    # Unique identifier (e.g., "python", "git", "home-automation")
  name: ""                  # Display name (e.g., "Python", "Git", "Home Automation")
  category: ""              # "language" or "topic"
  tier: 1                   # 1 (Foundation), 2 (Expand), or 3 (Specialized)

  description:
    short: ""               # One sentence (for lists)
    full: ""                # 2-3 sentences (for subject page)

  # Why should a maker learn this?
  value_proposition: ""

  # What can you build with this?
  enables:
    - ""
    - ""
```

---

## Leveling Structure

```yaml
leveling:
  total_levels: 0           # How many levels for this subject (3-7 typical)

  levels:
    - number: 0
      name: ""              # e.g., "Curious"
      description: ""       # What can someone at this level do?
      time_estimate: ""     # e.g., "2-4 hours"

    - number: 1
      name: ""              # e.g., "Explorer"
      description: ""
      time_estimate: ""

    # Continue for all levels...
```

---

## Prerequisites and Relationships

```yaml
dependencies:
  # Soft prerequisites - recommended but not required
  recommended:
    - subject_id: ""
      min_level: 0
      reason: ""            # Why this helps

  # What this subject commonly integrates with
  integrates_with:
    - subject_id: ""
      integration_projects:
        - ""                # Project IDs that combine these subjects

  # Subjects that are enhanced by this one
  enhances:
    - ""
```

---

## Platform Compatibility

```yaml
platforms:
  windows: true             # Works on Windows
  macos: true               # Works on macOS
  linux: true               # Works on Linux
  browser_only: false       # Can be done entirely in browser

  notes: ""                 # Any platform-specific considerations
```

---

## Hardware Requirements

```yaml
hardware:
  # Minimum to start learning
  minimum:
    - "Computer with internet access"

  # Unlocks additional projects
  optional:
    - item: ""
      unlocks:
        - ""                # Project IDs this hardware enables
      estimated_cost: ""    # e.g., "$35-50"
```

---

## Milestone Projects

Define at least one project per level. Projects should be practical and produce something useful.

```yaml
projects:
  - id: ""                  # Unique project ID
    name: ""                # Display name
    level: 0                # Which level this project belongs to

    description:
      short: ""             # One sentence
      full: ""              # Full description

    # What the user will have when done
    outcome: ""

    # How this improves daily life
    life_value: ""

    # Time to complete
    time_estimate: ""

    # Other subjects involved (for integration projects)
    integrations:
      - subject_id: ""
        min_level: 0

    # Hardware needed beyond minimum
    hardware_required: []
    hardware_optional: []

    # Legal or ethical considerations
    safety_notes: ""

    # Platform-specific variants
    variants:
      windows: null         # Different approach for Windows
      macos: null
      linux: null
```

---

## Assessment Criteria

For placement testing - how do we know someone is at each level?

```yaml
assessments:
  placement_test:
    available: true         # Can users test into this subject?
    estimated_time: ""      # e.g., "10-15 minutes"

  level_criteria:
    - level: 0
      can_do:
        - ""                # Observable skills at this level
        - ""
      cannot_yet:
        - ""                # What they'll learn at next level

    - level: 1
      can_do:
        - ""
      cannot_yet:
        - ""

    # Continue for all levels...
```

---

## Content Outline

High-level outline of what's taught at each level. Detailed content lives in `/content/`.

```yaml
curriculum:
  - level: 0
    topics:
      - ""
      - ""
    key_concepts:
      - ""

  - level: 1
    topics:
      - ""
    key_concepts:
      - ""

  # Continue for all levels...
```

---

## Example Subjects

See these completed subject definitions for reference:
- `/content/languages/python/subject.yaml`
- `/content/topics/git/subject.yaml`
- `/content/topics/docker/subject.yaml`

---

## Checklist Before Submitting

- [ ] All metadata fields completed
- [ ] Level names are descriptive and consistent with platform tone
- [ ] At least one project per level defined
- [ ] Time estimates are realistic
- [ ] Prerequisites clearly explained (not just listed)
- [ ] Platform compatibility verified
- [ ] Hardware requirements include cost estimates
- [ ] Assessment criteria are observable/testable
- [ ] Life value is clear for each project
- [ ] Integration opportunities identified
