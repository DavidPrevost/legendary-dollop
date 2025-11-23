# Module 11: Planning Your First Project

Time to apply everything you've learned. This module guides you through planning and setting up a real project.

---

## 11.1 Applying What You've Learned

### Choosing a Project Idea

Pick something:
- **Useful**: Solves a real problem you have
- **Scoped**: Can complete in days, not months
- **Interesting**: You actually want to build it

Good first projects:
- File organizer script
- Daily journal/note system
- Personal dashboard
- Bookmark manager
- Configuration backup tool

### Scoping for Success

First projects should be small:
- 1-2 weeks of work maximum
- Clear finish line
- Working result you'll actually use

Resist feature creep. You can always add more later.

### Creating Your Project README

Start with documentation:

```markdown
# [Project Name]

[One sentence description]

## Problem

[What problem does this solve?]

## Goals

- [Primary goal]
- [Secondary goal]

## Status

🚧 Under development

## Getting Started

_Coming soon_
```

This forces clarity before coding.

### Setting Up Project Structure

Create your scaffold:

```
my-project/
├── README.md
├── LICENSE
├── .gitignore
├── src/
├── tests/
└── docs/
```

Use what you learned in Module 5.

### Breaking Down Into Tasks

Create your task list:

```markdown
## Tasks

### Phase 1: Core
- [ ] Set up project structure
- [ ] Implement basic functionality
- [ ] Add command-line interface

### Phase 2: Polish
- [ ] Add error handling
- [ ] Write tests
- [ ] Document usage

### Phase 3: Release
- [ ] Test on fresh system
- [ ] Write release notes
- [ ] Tag version 1.0
```

### Creating a Simple Roadmap

Define milestones:

```markdown
## Roadmap

### v0.1 - Proof of Concept
- Basic functionality works
- Manual testing

### v0.5 - Beta
- Error handling
- Configuration file
- README with instructions

### v1.0 - Release
- Automated tests
- Full documentation
- Ready to share
```

---

## 11.2 Project Kickoff

### Initial Commit

Make your first commit count:

```bash
git init
git add .
git commit -m "Initial project structure

- README with project description and goals
- Basic directory structure
- MIT license
- Gitignore for Python"
```

You now have a starting point.

### First Milestone Definition

Define your first milestone clearly:

```markdown
## Milestone 1: Proof of Concept

**Goal**: Demonstrate the core idea works

**Definition of Done**:
- [ ] Can run script from command line
- [ ] Performs basic functionality
- [ ] Outputs result
- [ ] Works on my machine

**Not included**:
- Error handling
- Tests
- Documentation
```

Keep it small and achievable.

### Tracking Progress

Update your task list as you work:

```markdown
- [x] Set up project structure ✓
- [x] Create main script ✓
- [ ] Add command-line parsing ← current
- [ ] Implement core logic
- [ ] Test manually
```

Visual progress is motivating.

### Adapting Plans as You Learn

Your initial plan will be wrong:
- Some tasks will be easier than expected
- Some will be harder
- You'll discover new requirements

That's fine. Update your plan. Planning is valuable even when plans change.

---

## 11.3 Reflection and Iteration

### Reviewing What Worked

After reaching a milestone, reflect:
- What went smoothly?
- What was harder than expected?
- What would you do differently?

Write this down. It improves future projects.

### Identifying Improvements

Note improvements for next time:
- "Estimate setup time higher"
- "Define acceptance criteria more clearly"
- "Test on Windows earlier"

### Updating Templates and Processes

Incorporate learnings:
- Update your README template
- Refine your task breakdown process
- Adjust your estimation approach

Each project should be better than the last.

### Building Your Personal System

Over time, you'll develop:
- Your preferred project structure
- Your documentation style
- Your planning approach
- Your estimation method

This is your personal maker system. It evolves with experience.

---

## Concepts Covered

This module covered concepts 242-255:

242-247: Applying what you've learned (choosing ideas, scoping, README, structure, tasks, roadmap)
248-251: Project kickoff (initial commit, first milestone, tracking, adapting)
252-255: Reflection and iteration (reviewing, identifying improvements, updating processes, personal system)

---

## Check Your Understanding

You should be able to:

- [ ] Choose and scope an appropriate first project
- [ ] Create a project README before writing code
- [ ] Set up proper project structure
- [ ] Break a project into milestones and tasks
- [ ] Reflect on a project and improve your process

---

## Complete the Subject

You've now covered all concepts in **Project Foundations**!

**To complete this subject**, finish the milestone project for your current level:

- **Level 0**: Platform Explorer
- **Level 1**: Personal README
- **Level 2**: Project Scaffold
- **Level 3**: Project Planner
- **Level 4**: Documentation Suite

---

## What's Next

With Project Foundations complete, you're ready for:

- **Command Line Mastery** - Become comfortable in the terminal
- **Python** - Start automating with code
- **Git/GitHub** - Version control your projects

The documentation and planning skills you've learned will be used in every other subject.

---

## Congratulations!

You now have professional-grade documentation and planning skills. These are foundational abilities that will make you more effective in everything you build.

Remember the core principles:
- **Plan before you build** (but don't over-plan)
- **Document for future-you**
- **Start small and iterate**
- **Learn from each project**

Now go build something useful!
