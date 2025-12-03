# Architecture Decision Records

This document captures significant technical decisions with their context and rationale. Each decision references the Core Principles it supports.

---

## ADR-001: Modular Architecture

### Status
Accepted

### Context
The platform needs to support both broad skill exploration (hobbyist) and deep skill mastery (professional) without requiring architectural rewrites.

### Decision
Use a modular architecture where each component (capability checker, progress tracker, skill tree, etc.) is independent and communicates through well-defined interfaces.

### Rationale
- **Supports Principle 7 (Scalable Architecture)**: Modules can be enhanced independently
- **Supports Principle 8 (Progressive Complexity)**: Depth features can be added to modules without affecting breadth features
- **Supports Principle 3 (Flexible Paths)**: Different user paths can use different module combinations

### Consequences
- More initial setup complexity
- Clear boundaries enable parallel development
- Easier to test components in isolation
- Future depth features won't require core rewrites

---

## ADR-002: CLI-First Approach

### Status
Accepted

### Context
Need to choose primary interface for MVP. Options: CLI, Web UI, Desktop App.

### Decision
Build CLI as the primary interface for Phase 1. Web UI will come in later phases.

### Rationale
- **Supports Principle 5 (Accessibility First)**: CLI works everywhere, no browser requirements
- **Supports Principle 2 (Practical Over Perfect)**: Faster to build, ship sooner
- **Supports learning goals**: Users learning Bash benefit from CLI familiarity
- Cross-platform by default (Windows, macOS, Linux)
- No server infrastructure needed initially

### Consequences
- Steeper initial learning curve for non-technical users
- Rich visualizations limited until Web UI phase
- Skills like data visualization harder to demonstrate
- Sets up natural progression: CLI mastery → web development

---

## ADR-003: Local-First with Optional Cloud

### Status
Accepted

### Context
User data (progress, preferences, projects) needs to be stored somewhere.

### Decision
All data stored locally by default. Cloud sync is optional and user-controlled.

### Rationale
- **Supports Principle 5 (Accessibility First)**: No accounts required to start
- **Supports Principle 6 (User Agency)**: Users control their data
- Aligns with maker/homelab ethos of self-hosting
- No ongoing infrastructure costs for MVP
- Privacy-respecting by default

### Consequences
- Multi-device sync requires user action
- No community features without cloud component
- Users responsible for their own backups
- Future cloud features need careful privacy design

---

## ADR-004: Python as Primary Implementation Language

### Status
Accepted

### Context
Need to choose implementation language for platform core.

### Decision
Implement core platform in Python.

### Rationale
- **Supports Principle 5 (Accessibility First)**: Python available on all platforms
- **Supports platform goals**: Python is one of the three core taught languages
- Rich ecosystem for CLI tools (Click, Rich, etc.)
- Easy for users to understand and modify (hackable platform)
- Good cross-platform support

### Consequences
- Performance limitations for compute-heavy features
- Dependency management complexity (mitigated by venv)
- Users need Python installed (but they're learning it anyway)

---

## ADR-005: Virtual Environment Isolation

### Status
Accepted

### Context
Need to isolate platform dependencies from system Python and user projects.

### Decision
Use Python venv for dependency isolation. Provide clear setup instructions for Windows/macOS/Linux.

### Rationale
- **Supports Principle 5 (Accessibility First)**: venv is built into Python, no extra tools
- Simpler than Docker for this use case
- Works consistently across Windows 11, macOS, Linux
- Users learn venv as a transferable skill

### Consequences
- Less isolation than Docker (no system-level containment)
- Users must activate venv manually
- Cross-platform activation commands differ

---

## ADR-006: Skill Level Scaling Strategy

### Status
Superseded by ADR-009

### Context
Skills need to support both hobbyist exploration and professional mastery. How do we represent this?

### Decision
Use a two-dimensional skill tracking system:
- **Track**: Hobbyist (Tinkerer → Builder → Maker) or Professional (specializations)
- **Level**: Numeric progression within track (1.0 → 10.0)

Example: `Python: Hobbyist/Builder/2.3` or `Python: Professional/WebDev/4.1`

### Rationale
- **Supports Principle 7 (Scalable Architecture)**: Same system handles both paths
- **Supports Principle 8 (Progressive Complexity)**: Clear progression within and across tracks
- **Supports Principle 6 (User Agency)**: Users choose their track
- Allows comparison without judgment (hobbyist level 3 ≠ worse than professional level 3)

### Consequences
- More complex data model
- UI needs to handle track switching gracefully
- Professional tracks can be added incrementally

---

## ADR-007: Project-Based Content Structure

### Status
Accepted

### Context
How should learning content be organized?

### Decision
Organize content around projects, not concepts. Each project:
- Solves a real problem
- Lists required skills
- Declares hardware requirements
- Produces usable output

### Rationale
- **Supports Principle 2 (Practical Over Perfect)**: Every piece of content produces something useful
- **Supports Principle 4 (Integration Focus)**: Projects naturally combine skills
- **Supports Principle 1 (Breadth Over Depth)**: Users encounter multiple skills per project

### Consequences
- Pure concept teaching needs creative framing
- Projects need careful skill tagging
- Prerequisite system must be flexible

---

## ADR-008: Cross-Platform Command Strategy

### Status
Accepted

### Context
Platform will be used on Windows 11, macOS, and Linux. Commands and paths must work everywhere.

### Decision
- Use forward slashes in all paths (works on Windows in Python)
- Provide platform-specific instructions where commands differ
- Use Python's `pathlib` for path manipulation
- Test all features on Windows explicitly

### Rationale
- **Supports Principle 5 (Accessibility First)**: Works on user's actual machine
- Primary development environment is Windows 11 with VS Code
- Many makers use Windows

### Consequences
- Some Unix-specific content needs Windows alternatives
- Testing matrix is larger
- Documentation must cover multiple platforms

---

## ADR-009: Variable Levels Per Subject

### Status
Accepted (supersedes ADR-006)

### Context
Different Subjects have different natural depths. Python has far more depth than Markdown. Forcing uniform level counts either inflates simple Subjects or compresses complex ones.

### Decision
Allow each Subject to define its own number of levels (typically 3-7) with custom level names. Use "bands" for cross-Subject comparison:
- **Novice** (levels 0-1): Following tutorials, basic syntax
- **Competent** (levels 2-3): Modifying code, building from scratch
- **Proficient** (levels 4-5): Complex projects, system design
- **Expert** (levels 6+): Teaching, contributing

Examples:
- Python: 7 levels (Curious → Explorer → Tinkerer → Builder → Maker → Architect → Mentor)
- Markdown: 3 levels (Curious → Competent → Fluent)
- Docker: 5 levels (Curious → User → Composer → Orchestrator → Platform Engineer)

### Rationale
- **Supports Principle 8 (Progressive Complexity)**: Honest representation of Subject depth
- **Supports Principle 6 (User Agency)**: Users see realistic progression
- Bands enable comparison without false equivalence
- Reduces content burden for simpler Subjects

### Consequences
- More complex data model (level count varies)
- UI must handle variable level counts
- Subject definitions require more thought
- Band mapping needed for cross-Subject features

---

## ADR-010: Subject/Language/Topic Terminology

### Status
Accepted

### Context
Using "Skill" as both a category and a thing you gain caused confusion. Need clear terminology.

### Decision
Adopt the following hierarchy:
- **Subject**: Umbrella term for anything learnable
  - **Language**: Programming/markup/config languages (Python, HTML, YAML)
  - **Topic**: Technical knowledge that isn't a language (Git, Networking, Security)

Avoid "Skill" as a category name; use it only to describe what users gain.

### Rationale
- **Supports clarity**: No ambiguity between categories and outcomes
- Aligns with educational terminology
- Scales to future content types

### Consequences
- Codebase uses Subject/Language/Topic consistently
- Documentation updated to match
- UI labels reflect new terminology

---

## ADR-011: Placement Assessments

### Status
Accepted

### Context
Users may already know a Subject. Making them complete all early projects wastes time and is demotivating.

### Decision
Offer optional placement assessments (5-15 minutes) that allow users to demonstrate existing knowledge and skip levels they've mastered. Assessments:
- Are always optional (Principle 6)
- Test observable skills, not trivia
- Can be retaken
- Unlock appropriate starting level

### Rationale
- **Supports Principle 6 (User Agency)**: Users choose to skip or learn
- **Supports Principle 5 (Accessibility First)**: Respects users' existing knowledge
- Reduces friction for experienced makers
- Enables integration project access without completing all prerequisites

### Consequences
- Assessment content needed per Subject
- Must prevent gaming (randomized questions)
- Results stored in progress data
- Clear UI for "test out" vs "learn from start"

---

## ADR-012: Hardware Shopping List

### Status
Accepted

### Context
Users need to know what hardware projects require. Static cost estimates become outdated quickly.

### Decision
Instead of embedding costs, provide a dynamic "Shopping List" feature:
- Projects declare hardware requirements
- User marks what they already have (via capability detection or manual input)
- Shopping List shows only what's missing
- Links to current product pages where possible (not prices)

### Rationale
- **Supports Principle 5 (Accessibility First)**: Clear visibility of requirements
- **Supports Principle 6 (User Agency)**: Users make informed decisions
- Avoids stale price information
- Encourages users to inventory their capabilities

### Consequences
- Hardware items need stable identifiers
- Regional availability varies (some items unavailable globally)
- Links need periodic validation
- User capability data must be editable

---

## ADR-013: Time Estimates in Projects

### Status
Accepted (with reassessment planned)

### Context
Users want to know how long projects take for planning purposes.

### Decision
Include time estimates in all projects. Estimates should:
- Use ranges (e.g., "2-4 hours")
- Assume the user is at the minimum required level
- Be validated during testing phase

Plan to reassess accuracy during late testing and consider removal if estimates prove unreliable.

### Rationale
- **Supports planning**: Users can fit learning into their schedules
- Provides expectations management
- Useful for comparing project scope

### Consequences
- Estimates require validation
- Individual variance is high
- May need "your mileage may vary" disclaimer
- Potential for user frustration if estimates are wrong

---

## ADR-014: GUI as Target Interface

### Status
Accepted

### Context
CLI is appropriate for Phase 1 and developer-focused users, but "Curious" level users need a more approachable interface.

### Decision
Plan for GUI as the primary interface for general users. CLI remains:
- The MVP interface (ship fast)
- A first-class citizen (not deprecated)
- The interface for power users and automation

Web-based GUI is planned for Phase 6 but should influence architecture decisions now.

### Rationale
- **Supports Principle 5 (Accessibility First)**: GUI is more approachable
- CLI-first enables faster shipping
- Parallel support serves different user preferences
- Architecture should not assume CLI-only

### Consequences
- Core logic must be UI-agnostic
- Data models should support both interfaces
- CLI commands map to GUI actions
- Web development is on the roadmap

---

## ADR-015: Offline-First with Physical Media Support

### Status
Accepted

### Context
Platform should work without internet. In extreme cases, should be distributable on physical media to air-gapped systems.

### Decision
Design for full offline functionality:
- All content bundled with installation
- Progress stored locally
- No features require network for core learning
- Support distribution via USB/disc for air-gapped systems

Network-dependent content (e.g., "Using GitHub") clearly marked. Updates fetched when online but not required.

### Rationale
- **Supports Principle 5 (Accessibility First)**: Works anywhere, any connection
- Aligns with maker/self-sufficiency ethos
- Enables use in schools, libraries, remote areas
- Privacy-respecting (no telemetry required)

### Consequences
- Content bundled increases install size
- Update mechanism needed but not required
- Some Subjects inherently need network (clearly marked)
- Sync conflicts possible if user has multiple installations

---

## Future Decisions to Document

- [ ] Database choice for progress storage (SQLite vs JSON files)
- [ ] Plugin system design for community content
- [ ] Hardware detection strategy
- [ ] Project validation approach
- [ ] Web UI technology stack (when Phase 6 begins)
- [ ] Assessment question format and randomization
- [ ] Shopping list link management

---

## Decision Template

```markdown
## ADR-XXX: [Title]

### Status
[Proposed | Accepted | Deprecated | Superseded]

### Context
[What is the issue we're addressing?]

### Decision
[What did we decide to do?]

### Rationale
[Why did we make this decision? Which principles does it support?]

### Consequences
[What are the results of this decision?]
```
