# Module 7: Planning Tools and Techniques

Now that you understand planning concepts, let's learn the tools and techniques to put them into practice.

---

## 7.1 Simple Planning Tools

### Todo Lists (Plain Text)

The simplest planning tool:

```markdown
## Backup Tool Tasks

- [ ] Research existing solutions
- [ ] Design config format
- [ ] Implement file listing
- [ ] Implement compression
- [ ] Add scheduling
- [ ] Test on real data
- [ ] Write documentation
```

Works in any text editor. Version control friendly.

### Checklists for Processes

Reusable checklists for repeated tasks:

```markdown
## Project Kickoff Checklist
- [ ] Create repository
- [ ] Add README with project description
- [ ] Add LICENSE
- [ ] Add .gitignore
- [ ] Create directory structure
- [ ] Set up dev environment
- [ ] Create first milestone
```

Use the same checklist for every project.

### Markdown Task Lists

GitHub renders `- [ ]` as checkboxes:

```markdown
## Sprint 1
- [x] User authentication
- [x] Database setup
- [ ] API endpoints
- [ ] Frontend forms
```

Track progress visually.

### Priority Markers

Simple priority system:

```markdown
## Tasks
- [!!!] Fix critical bug (high)
- [!!] Add validation (medium)
- [!] Improve logging (low)
```

Or use labels:
```markdown
- [P1] Critical
- [P2] Important
- [P3] Nice to have
```

### Due Dates and Deadlines

Add dates for time-sensitive tasks:

```markdown
- [ ] Submit proposal (2024-01-20)
- [ ] Review feedback (2024-01-25)
- [ ] Final submission (2024-01-31)
```

---

## 7.2 Visual Planning

### Mind Maps for Brainstorming

Explore ideas non-linearly:

```
        ┌─ Config ─┬─ YAML file
        │          └─ CLI args
        │
Backup ─┼─ Storage ─┬─ Local
        │           └─ Cloud (future)
        │
        └─ Schedule ─┬─ Cron
                     └─ Manual
```

Good for early exploration before structure.

### Flowcharts for Processes

Document how things work:

```
[Start] → [Read Config] → [List Files]
                              ↓
                    [Create Archive] → [Compress]
                              ↓
                    [Save to Destination]
                              ↓
                    [Notify User] → [End]
```

Use for complex logic or user flows.

### Wireframes for Interfaces

Sketch UIs before building:

```
┌────────────────────────────┐
│  Backup Dashboard          │
├────────────────────────────┤
│ [Select Folders]           │
│ ┌────────────────────┐     │
│ │ □ ~/Documents      │     │
│ │ □ ~/Projects       │     │
│ │ □ ~/Pictures       │     │
│ └────────────────────┘     │
│                            │
│ [Run Backup]   [Settings]  │
└────────────────────────────┘
```

Test ideas before writing code.

### Architecture Diagrams

Show system components:

```
┌─────────┐     ┌──────────┐     ┌─────────┐
│  CLI    │ ──→ │  Core    │ ──→ │ Storage │
└─────────┘     └──────────┘     └─────────┘
                     │
                     ↓
              ┌──────────────┐
              │ Notification │
              └──────────────┘
```

### ASCII Diagrams in Documentation

For docs that need to be plain text:

```
+----------+    +----------+    +----------+
|  Input   | -> | Process  | -> |  Output  |
+----------+    +----------+    +----------+
```

Works everywhere, versions well.

---

## 7.3 Kanban Basics

### What is Kanban?

A visual system for managing work:
- Cards represent tasks
- Columns represent stages
- Cards move left to right

### Basic Columns

```
┌──────────┬──────────┬──────────┐
│ To Do    │ Doing    │ Done     │
├──────────┼──────────┼──────────┤
│ Task A   │ Task D   │ Task G   │
│ Task B   │          │ Task H   │
│ Task C   │          │          │
└──────────┴──────────┴──────────┘
```

### Work in Progress (WIP) Limits

Limit how many items can be "Doing":

- WIP limit of 2 = only 2 tasks in progress
- Forces focus
- Prevents context switching

If Doing is full, finish something before starting new work.

### Moving Cards Through Stages

Workflow:
1. Create card in "To Do"
2. Move to "Doing" when you start
3. Move to "Done" when complete

Never move backwards (if blocked, note it on the card).

### When Kanban Helps

Good for:
- Ongoing work with no fixed end
- Work that arrives continuously
- Visual thinkers
- Teams with varying capacity

Less good for:
- Fixed-scope projects with deadlines
- Heavily dependent tasks

### GitHub Projects as Kanban

GitHub provides built-in Kanban boards:
1. Go to your repo's Projects tab
2. Create a new project (Board view)
3. Add columns
4. Convert issues to cards

Free and integrated with your code.

---

## 7.4 Issue Tracking

### What Are Issues?

Issues are trackable items of work:
- Bugs
- Features
- Tasks
- Questions

GitHub Issues is the most common system for open source.

### Issue vs Task vs Bug vs Feature

| Type | Description | Example |
|------|-------------|---------|
| Bug | Something broken | "Backup fails on large files" |
| Feature | New capability | "Add cloud backup support" |
| Task | Work to do | "Write installation docs" |
| Question | Needs discussion | "Should we support Windows?" |

Use labels to distinguish them.

### Writing Good Issue Titles

**Bad**: "It doesn't work"
**Good**: "Backup fails with 'permission denied' on /etc folder"

Include:
- What's affected
- The specific problem
- Key details

### Issue Descriptions and Context

Provide enough information:

```markdown
## Description
Backup fails when including /etc folder.

## Steps to Reproduce
1. Add /etc to folders list
2. Run backup
3. See error

## Expected Behavior
Backup completes (skipping unreadable files)

## Actual Behavior
Backup crashes with 'permission denied'

## Environment
- OS: Ubuntu 22.04
- Python: 3.10
- Version: 1.2.0
```

### Labels and Categorization

Common labels:
- `bug`, `feature`, `enhancement`
- `documentation`, `testing`
- `good first issue`, `help wanted`
- `priority: high`, `priority: low`

Labels help filter and organize.

### Assigning and Ownership

Assign issues to people:
- Clear responsibility
- Prevents duplication
- Enables workload balancing

Self-assign when you start working on something.

### Linking Issues to Code

Reference issues in commits and PRs:

```
git commit -m "Fix permission error in backup

Fixes #42"
```

GitHub automatically links them.

---

## 7.5 Milestones

### What Are Milestones?

A milestone is a collection of issues that together represent a significant goal:
- Version 1.0
- Beta release
- "Core features complete"

### Milestone as a Collection of Issues

Group related issues:

```
Milestone: v1.0 Release
├── #12 Basic backup functionality
├── #13 Configuration file
├── #14 Scheduling
├── #15 README documentation
└── #16 Installation guide
```

When all issues are closed, milestone is complete.

### Release Planning with Milestones

Plan releases by milestone:
- **v0.1** - Proof of concept
- **v0.5** - Core features
- **v1.0** - Ready for others to use
- **v1.1** - Bug fixes and polish

### Milestone Scope and Deadlines

Set reasonable scope:
- Not too many issues (overwhelming)
- Not too few (meaningless)
- Optional deadline for motivation

### Tracking Milestone Progress

GitHub shows completion percentage:
- 4 of 10 issues closed = 40%
- Visual progress indicator

Review regularly and adjust scope if needed.

---

## Concepts Covered

This module covered concepts 153-180:

153-157: Simple tools (todo lists, checklists, task lists, priorities, dates)
158-162: Visual planning (mind maps, flowcharts, wireframes, architecture, ASCII)
163-168: Kanban (what it is, columns, WIP limits, moving cards, when to use, GitHub Projects)
169-175: Issue tracking (what issues are, types, titles, descriptions, labels, assigning, linking)
176-180: Milestones (what they are, grouping issues, release planning, scope, tracking)

---

## Check Your Understanding

You should be able to:

- [ ] Create a simple todo list with priorities
- [ ] Draw basic flowcharts and wireframes
- [ ] Explain Kanban columns and WIP limits
- [ ] Write a clear issue with good title and description
- [ ] Create milestones to plan releases

---

## Next Steps

Continue to **Module 8: Estimation and Time Management** to learn how to estimate work accurately.
