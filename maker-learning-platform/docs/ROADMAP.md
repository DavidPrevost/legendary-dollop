# Development Roadmap

This roadmap outlines the phased development of the Maker Learning Platform. Each phase builds on the previous while maintaining alignment with our Core Principles.

---

## Phase 1: Foundation (Current)

### Goal
Deliver a working CLI tool that demonstrates core concepts and produces genuine value for users.

### Deliverables

#### Core Infrastructure
- [x] Project structure and foundational documents
- [ ] Python package setup with venv isolation
- [ ] Basic CLI framework (using Click)
- [ ] Local data storage (JSON-based initially)

#### Capability Checker
- [ ] System capability detection (OS, Python version, installed tools)
- [ ] Hardware inventory (available ports, memory, storage)
- [ ] Software inventory (Git, Docker, databases, etc.)
- [ ] Capability profile export/import

#### Progress Tracker (Breadth)
- [ ] Skill level tracking (Tinkerer → Builder → Maker)
- [ ] Project completion records
- [ ] Time investment tracking
- [ ] Simple progress visualization (ASCII-based)

#### Initial Content
- [ ] Python: Tinkerer Level 1-3 projects
  - File organizer script
  - Simple automation task
  - Basic web scraper
- [ ] Bash: Tinkerer Level 1-3 projects
  - System info script
  - Backup automation
  - Environment setup
- [ ] HTML/CSS: Tinkerer Level 1-3 projects
  - Personal dashboard (local)
  - Project documentation page
  - Simple status display

#### First Integration Milestone
- [ ] "Morning Dashboard" project combining:
  - Python (data gathering)
  - HTML/CSS (display)
  - Bash (automation/scheduling)

### Success Criteria
- User can install and run with just Python 3.8+
- Complete capability check in under 30 seconds
- Finish first project within 1 hour
- All projects produce files/tools user will actually use

### Principles in Focus
- Principle 5: Accessibility First (laptop-only start)
- Principle 2: Practical Over Perfect (ship fast, iterate)
- Principle 1: Breadth Over Depth (three languages, light depth)

---

## Phase 2: Skill Tree Visualizer

### Goal
Help users see their progress, find connections, and discover new paths.

### Deliverables

#### Skill Tree Engine
- [ ] Skill relationship mapping
- [ ] Prerequisite recommendations (not requirements)
- [ ] Integration point highlighting
- [ ] Path suggestions based on interests/hardware

#### Visualization
- [ ] ASCII skill tree for CLI
- [ ] Export to SVG/PNG for sharing
- [ ] Interactive terminal UI (using Rich or similar)

#### Enhanced Progress Tracking
- [ ] Skill connections earned
- [ ] Integration badges
- [ ] Learning velocity metrics

### Success Criteria
- Users can visualize their entire skill landscape
- Clear paths visible from current position
- Integration opportunities highlighted

### Principles in Focus
- Principle 4: Integration Focus (visible connections)
- Principle 3: Flexible Paths (multiple routes shown)
- Principle 6: User Agency (exploration, not prescription)

---

## Phase 3: Hardware Awareness

### Goal
Personalize recommendations based on user's actual hardware capabilities.

### Deliverables

#### Hardware Detection
- [ ] Raspberry Pi detection and model identification
- [ ] Arduino/microcontroller detection
- [ ] Network device discovery
- [ ] Sensor/peripheral inventory

#### Content Unlocking
- [ ] Hardware-specific project recommendations
- [ ] Simulator fallbacks for missing hardware
- [ ] Hardware wishlist with project unlocks
- [ ] Cost-benefit analysis for hardware purchases

#### Hardware Projects
- [ ] Raspberry Pi starter projects
- [ ] Arduino integration projects
- [ ] Network/homelab projects

### Success Criteria
- Accurate hardware detection
- Relevant project recommendations
- Clear upgrade paths for interested users

### Principles in Focus
- Principle 5: Accessibility First (simulators for missing hardware)
- Principle 3: Flexible Paths (hardware-aware recommendations)
- Principle 2: Practical Over Perfect (detection > perfection)

---

## Phase 4: Integration Projects

### Goal
Deliver complex, multi-skill projects that showcase the power of breadth.

### Deliverables

#### Project Framework
- [ ] Multi-skill project templates
- [ ] Integration validation system
- [ ] Project showcase/portfolio generator

#### Flagship Integration Projects
- [ ] Home automation dashboard
- [ ] Personal data analytics pipeline
- [ ] Self-hosted service stack
- [ ] IoT sensor network

#### Community Foundations
- [ ] Project sharing format
- [ ] Import community projects
- [ ] Difficulty/quality ratings

### Success Criteria
- 5+ complex integration projects available
- Users completing projects they're proud to share
- Clear value demonstration for skill breadth

### Principles in Focus
- Principle 4: Integration Focus (primary focus of phase)
- Principle 2: Practical Over Perfect (useful > impressive)
- Principle 1: Breadth Over Depth (reward for breadth)

---

## Phase 5: Depth Expansion

### Goal
Add professional-level tracks for users who want career-applicable depth.

### Deliverables

#### Professional Track Infrastructure
- [ ] Specialization paths (DevOps, Data Engineering, Web Dev, etc.)
- [ ] Depth level tracking (extends beyond Maker level)
- [ ] Professional project standards
- [ ] Best practices curriculum

#### Initial Professional Tracks
- [ ] Python: Web Development Specialization
- [ ] Python: Data Engineering Specialization
- [ ] DevOps: Infrastructure Automation

#### Certification Preparation (Optional)
- [ ] Study guides for relevant certifications
- [ ] Practice assessments
- [ ] Skill mapping to certification requirements

### Success Criteria
- Seamless transition from hobbyist to professional track
- Professional content doesn't dilute hobbyist experience
- Clear value proposition for depth investment

### Principles in Focus
- Principle 8: Progressive Complexity (depth as option)
- Principle 7: Scalable Architecture (no rewrites needed)
- Principle 6: User Agency (depth is choice, not requirement)

---

## Future Phases (Tentative)

### Phase 6: Web UI
- Modern web interface option
- Rich visualizations
- Mobile-friendly access
- Maintains CLI as first-class citizen

### Phase 7: Community Features
- Project sharing and discovery
- User-created content
- Mentorship matching
- Local maker group integration

### Phase 8: Hardware Playground
- Virtual hardware simulators
- Cloud-based hardware access
- Hardware lending library integration

### Phase 9: Enterprise/Education
- Classroom management
- Curriculum alignment
- Progress reporting
- Team features

---

## Development Principles

### Each Phase Must:
1. **Deliver standalone value** - Useful even if later phases never ship
2. **Maintain backward compatibility** - Don't break existing users
3. **Stay true to principles** - Especially Accessibility and User Agency
4. **Support future phases** - Architecture enables, doesn't limit

### Versioning Strategy
- Phase completion = major version (1.0, 2.0, etc.)
- Features within phase = minor version (1.1, 1.2, etc.)
- Bug fixes = patch version (1.1.1, 1.1.2, etc.)

### Timeline Philosophy
We don't estimate timelines. We ship when it's ready and useful. Quality and principle alignment matter more than speed.

---

## How to Use This Roadmap

1. **Current contributors**: Focus on current phase deliverables
2. **Feature requests**: Map to appropriate phase
3. **Architecture decisions**: Consider future phase requirements
4. **Principle conflicts**: Always resolve in favor of current phase's focus principles
