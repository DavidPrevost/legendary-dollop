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
Accepted

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

## Future Decisions to Document

- [ ] Database choice for progress storage (SQLite vs JSON files)
- [ ] Plugin system design for community content
- [ ] Hardware detection strategy
- [ ] Project validation approach
- [ ] Web UI technology stack (when Phase 3 begins)

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
