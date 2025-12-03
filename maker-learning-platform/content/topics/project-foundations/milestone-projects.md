# Project Foundations - Milestone Projects

Detailed design for each level's milestone project.

---

## Level 0: Platform Explorer

### Overview
A guided introduction to the Maker Learning Platform that ensures users understand how to use the platform while reflecting on their goals.

### What You'll Create
1. **Completed platform tour** - Navigate through all major platform features
2. **Maker profile** - Your goals, available hardware, and interests
3. **Reflection document** - Why you want to learn, what you hope to build

### Detailed Requirements

#### Part 1: Platform Tour (Guided)
- [ ] Launch the platform and view the main menu
- [ ] Browse the Subject catalog
- [ ] View your progress dashboard
- [ ] Explore at least 3 different subjects
- [ ] Understand how levels and bands work
- [ ] Check your capability detection results
- [ ] Learn how to start and complete projects

#### Part 2: Maker Profile Setup
- [ ] Set your display name
- [ ] Choose primary interests (select from: home automation, web development, data projects, hardware tinkering, self-hosting, mobile apps, other)
- [ ] Run capability detection or manually input your hardware/software
- [ ] Set 1-3 learning goals
- [ ] Choose your learning pace preference

#### Part 3: Reflection Document
Write 200-500 words covering:
- [ ] Why you want to learn to build things (personal motivation)
- [ ] What kind of projects interest you most
- [ ] One specific problem you'd like to solve with technology
- [ ] What "success" looks like for you on this platform

### Success Criteria
- All platform tour checkpoints completed
- Maker profile fully configured
- Reflection document meets word count and covers all prompts
- Reflection saved to your projects folder

### Skills Demonstrated
- Platform navigation
- Self-reflection on goals
- Basic writing/documentation

### Life Value
You now have a clear vision for your learning journey and know how to use the platform effectively. The reflection document becomes a touchstone you can return to when you need motivation.

### Time Estimate
1-2 hours

### Notes
- This is the only "guided tour" style project; all others are more hands-on
- Reflection document can be in plain text or Markdown (teaches Markdown organically)
- Profile information is used to personalize recommendations

---

## Level 1: Personal README

### Overview
Create a comprehensive personal README that introduces yourself, similar to GitHub profile READMEs. This applies Markdown skills to a real, useful document.

### What You'll Create
A single Markdown file (`PERSONAL_README.md`) that serves as your maker introduction.

### Detailed Requirements

#### Required Sections
- [ ] **Header** - Your name/handle and a one-line description
- [ ] **About Me** - 2-3 paragraphs introducing yourself
- [ ] **Current Learning** - What you're learning now (as a list)
- [ ] **Interests** - Your maker/tech interests
- [ ] **Goals** - What you want to build (numbered list)
- [ ] **Hardware/Setup** - What tools you have (table format)
- [ ] **Contact/Links** - How to reach you (can be placeholder)

#### Required Markdown Elements
- [ ] At least 3 heading levels
- [ ] Bold and italic text
- [ ] Unordered list
- [ ] Ordered list
- [ ] At least one table
- [ ] At least one link
- [ ] At least one code block (can be example of favorite command/code)
- [ ] Horizontal rule to separate sections

#### Quality Requirements
- [ ] Consistent heading hierarchy
- [ ] Proper spacing between sections
- [ ] No broken Markdown syntax
- [ ] Readable and well-organized

### Success Criteria
- All required sections present
- All required Markdown elements used correctly
- Document renders properly (no syntax errors)
- Content is genuine and thoughtful (not placeholder text)
- File saved as `PERSONAL_README.md`

### Skills Demonstrated
- All Markdown fundamentals
- Document structure
- Writing for an audience
- Self-presentation

### Life Value
You now have a personal introduction document you can use on GitHub, in project submissions, or anywhere you need to introduce yourself as a maker. This is a genuinely useful artifact.

### Time Estimate
2-3 hours

### Example Structure
```markdown
# Jane Doe - Aspiring Maker

> Automating my home, one script at a time

## About Me
[2-3 paragraphs]

## 🌱 Currently Learning
- Python basics
- Home automation with Home Assistant
- Docker fundamentals

## 🔧 Interests
[Description of interests]

## 🎯 Goals
1. Automate my morning routine
2. Build a personal dashboard
3. Self-host my own cloud storage

## 💻 My Setup
| Item | Details |
|------|---------|
| Computer | Windows 11 laptop |
| Single Board | Raspberry Pi 4 |
| Smart Home | Home Assistant |

---

## 📫 Contact
[Links or contact info]
```

---

## Level 2: Project Scaffold

### Overview
Create a complete project scaffold for a real project idea. This applies README and project structure skills to create something you'll actually use.

### What You'll Create
A complete project folder structure with all standard files, ready for development.

### Detailed Requirements

#### Project Choice
Choose one of these starter projects (or propose your own):
- **File Organizer** - A script to sort files by type/date
- **Daily Logger** - A tool to log daily notes/activities
- **Config Backup** - A tool to backup dotfiles/configs
- **Bookmark Manager** - A tool to organize and export bookmarks

#### Required Files
- [ ] `README.md` - Comprehensive project README
- [ ] `LICENSE` - Appropriate open source license
- [ ] `.gitignore` - Proper ignores for your language
- [ ] `CONTRIBUTING.md` - How others can contribute
- [ ] `CHANGELOG.md` - Started with [Unreleased] section

#### Required Directory Structure
```
project-name/
├── README.md
├── LICENSE
├── .gitignore
├── CONTRIBUTING.md
├── CHANGELOG.md
├── src/           # Source code (empty placeholder file ok)
├── tests/         # Test files (empty placeholder file ok)
├── docs/          # Additional documentation
└── examples/      # Usage examples
```

#### README Requirements
Must include these sections with real content:
- [ ] Project title and badges (can use placeholder badges)
- [ ] Description (what it does and why)
- [ ] Features (planned features list)
- [ ] Installation (step-by-step, even if hypothetical)
- [ ] Usage (with code examples)
- [ ] Configuration (any config options)
- [ ] Contributing (link to CONTRIBUTING.md)
- [ ] License (link to LICENSE)

#### Quality Requirements
- [ ] README installation instructions are specific and testable
- [ ] Usage examples are realistic
- [ ] .gitignore is appropriate for chosen language
- [ ] LICENSE is a real license (MIT, Apache, etc.)
- [ ] CONTRIBUTING.md has meaningful content
- [ ] Folder names follow conventions

### Success Criteria
- All required files present
- All required directories present
- README has all required sections with real content
- No placeholder text like "TODO" or "Lorem ipsum"
- Structure follows conventions for chosen language
- Someone could understand the project from README alone

### Skills Demonstrated
- README writing with all sections
- Project structure organization
- Naming conventions
- License selection
- Thinking about contributors

### Life Value
You now have a project scaffold you can actually use for your first real project. This structure will serve as your template for future projects.

### Time Estimate
2-4 hours

---

## Level 3: Project Planner

### Overview
Take a project idea and create a comprehensive plan without writing any code. This is pure planning and documentation.

### What You'll Create
A complete project plan document covering all aspects of project planning.

### Detailed Requirements

#### Project Choice
Choose one of these project ideas (or propose your own):
- **Home Dashboard** - A local webpage showing weather, calendar, tasks
- **Expense Tracker** - A tool to log and categorize expenses
- **Recipe Manager** - A tool to store and search recipes
- **Habit Tracker** - A tool to track daily habits and streaks

#### Required Sections

##### 1. Problem Statement
- [ ] What problem does this solve?
- [ ] Who has this problem?
- [ ] How are they solving it now?
- [ ] Why is a new solution needed?

##### 2. Project Goals
- [ ] Primary goal (the main thing it must do)
- [ ] Secondary goals (nice to haves)
- [ ] Non-goals (explicitly out of scope)
- [ ] Success criteria (how you know it's done)

##### 3. User Stories (at least 5)
Format: "As a [user], I want [action] so that [benefit]"
- [ ] Each story has acceptance criteria
- [ ] Stories are prioritized (Must/Should/Could/Won't)

##### 4. Task Breakdown
- [ ] Break the project into phases
- [ ] Break each phase into tasks
- [ ] Identify dependencies between tasks
- [ ] Mark which tasks are blockers

##### 5. Time Estimates
- [ ] Estimate each task (use ranges)
- [ ] Sum up for phase estimates
- [ ] Sum up for project estimate
- [ ] Add buffer for unknowns (suggest 20-50%)

##### 6. Milestone Plan
- [ ] Define 3-5 milestones
- [ ] Each milestone has specific deliverables
- [ ] Milestones are in logical order

##### 7. Risks and Mitigations
- [ ] Identify at least 3 risks
- [ ] Each risk has a mitigation strategy

##### 8. Tech Stack Decisions
- [ ] What language/framework will you use?
- [ ] Why this choice?
- [ ] What alternatives did you consider?

### Success Criteria
- All sections completed with thoughtful content
- User stories follow correct format
- Acceptance criteria are testable
- Task breakdown is granular enough to be actionable
- Time estimates are realistic (not wildly optimistic)
- Milestones tell a coherent story
- Risks are genuine concerns (not made up)

### Skills Demonstrated
- Problem definition
- Requirements gathering
- Task decomposition
- Estimation
- Risk identification
- Technical decision making

### Life Value
You can now plan any project before diving into code. This prevents wasted effort and scope creep. The plan document can be shared with collaborators or used as your personal roadmap.

### Time Estimate
3-5 hours

---

## Level 4: Documentation Suite

### Overview
Create a professional-grade documentation package for a project. This demonstrates mastery of technical documentation.

### What You'll Create
A complete documentation set that would satisfy a professional project.

### Detailed Requirements

#### Project Choice
Use the project from Level 2 (Project Scaffold) or Level 3 (Project Planner), or choose:
- A project you've actually built
- A well-known open source project (document as if you built it)

#### Required Documents

##### 1. Architecture Overview (`docs/ARCHITECTURE.md`)
- [ ] System context (what it interacts with)
- [ ] Component breakdown
- [ ] Data flow description
- [ ] At least one diagram (ASCII or image)

##### 2. Architecture Decision Records (at least 2)
`docs/adr/` folder with:
- [ ] ADR-001: [Significant decision]
- [ ] ADR-002: [Another significant decision]
- [ ] Each follows ADR format (Context, Decision, Rationale, Consequences)

##### 3. API Documentation (`docs/API.md`)
Document at least 3 endpoints/functions:
- [ ] Endpoint/function signature
- [ ] Description
- [ ] Parameters with types
- [ ] Return value
- [ ] Example request/response or usage
- [ ] Possible errors

##### 4. Configuration Documentation (`docs/CONFIGURATION.md`)
- [ ] All configuration options
- [ ] Default values
- [ ] Required vs optional
- [ ] Environment variables
- [ ] Example configuration file

##### 5. Changelog (`CHANGELOG.md`)
- [ ] Follows Keep a Changelog format
- [ ] Has [Unreleased] section
- [ ] Has at least one version (can be 0.1.0)
- [ ] Entries categorized (Added, Changed, Fixed, etc.)

##### 6. Workflow Reflection (`docs/WORKFLOW.md`)
- [ ] Your personal documentation workflow
- [ ] What works well for you
- [ ] What you want to improve
- [ ] Tools you prefer

### Success Criteria
- All documents present and complete
- Architecture diagram is clear and informative
- ADRs follow proper format with genuine decisions
- API docs are detailed enough to use without seeing code
- Configuration docs are comprehensive
- Changelog follows standard format
- Workflow reflection shows genuine self-awareness

### Skills Demonstrated
- Architecture documentation
- Decision recording
- API documentation
- Configuration documentation
- Changelog maintenance
- Process reflection

### Life Value
You can now document projects at a professional level. This skill set is directly transferable to work environments and makes your personal projects maintainable long-term.

### Time Estimate
4-6 hours

---

## Project Progression

| Level | Project | Key Artifact | Builds On |
|-------|---------|--------------|-----------|
| 0 | Platform Explorer | Reflection document | Nothing (entry point) |
| 1 | Personal README | Markdown document | Level 0 (basic writing) |
| 2 | Project Scaffold | Project folder | Level 1 (Markdown skills) |
| 3 | Project Planner | Planning document | Level 2 (project thinking) |
| 4 | Documentation Suite | Doc package | All previous levels |

Each project builds on the previous, creating a coherent progression from platform introduction to professional documentation.
