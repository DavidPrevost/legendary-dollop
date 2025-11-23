# Module 6: Project Planning Basics

A little planning prevents a lot of wasted effort. This module teaches you how to define, scope, and break down projects.

---

## 6.1 Why Plan?

### Planning vs Diving In

Two extremes:
- **No planning**: Jump in, figure it out, probably rewrite later
- **Over-planning**: Spend weeks planning, never start building

**Right balance**: Enough planning to know where you're going, then start building and adapt.

### The Planning Spectrum

| Project Size | Planning Needed |
|-------------|-----------------|
| One-off script | Minimal (README with goals) |
| Personal tool | Light (goals, basic tasks) |
| Shared project | Moderate (user stories, milestones) |
| Team project | Detailed (full plan, reviews) |

### Right-Sizing Your Planning Effort

Ask:
- How long will this take? (longer = more planning)
- Will others use it? (yes = more planning)
- Can I change it easily? (no = more planning)
- What happens if it fails? (bad = more planning)

### Planning for Personal Projects

Even for yourself:
- Write down what you're building
- List the main features
- Identify the first milestone
- Set a "good enough" threshold

### When to Skip Formal Planning

Skip detailed planning when:
- You're just exploring/learning
- It's truly a throwaway script
- The problem is well-understood
- You can easily start over

---

## 6.2 Defining Your Project

### Problem Statement

Start with the problem, not the solution:

**Bad**: "I want to build a backup script"
**Good**: "I keep losing files because I forget to back them up. I need automated backups that happen without me remembering."

Format:
```
[Who] has [problem] because [cause].
Currently they [workaround].
This is bad because [consequence].
```

### Goals and Objectives

**Primary goal**: The one thing it must do
**Secondary goals**: Nice to have
**Non-goals**: Explicitly out of scope

Example:
```markdown
## Goals

### Primary
- Automatically back up specified folders daily

### Secondary
- Compress backups to save space
- Notify me if backup fails
- Delete backups older than 30 days

### Non-goals (out of scope)
- Cloud backup (just local for now)
- Backing up system files
- Real-time sync
```

Non-goals prevent scope creep.

### Success Criteria

How do you know it's done?

```markdown
## Success Criteria
- [ ] Backups run daily without manual action
- [ ] Backups complete in under 5 minutes
- [ ] I can restore a file from last week
- [ ] I get a notification if backup fails
```

These are testable.

### Scope Boundaries

Define what's included and excluded:

```markdown
## In Scope
- Local file backup
- Schedule-based triggers
- Simple compression

## Out of Scope
- Cloud storage
- Database backup
- Encryption
```

### Target Users

Even for personal projects, define who it's for:

```markdown
## Target User
Me—a developer with:
- Multiple project folders
- Weekly need to recover deleted files
- Low patience for configuration
```

This guides design decisions.

---

## 6.3 Breaking Down Work

### From Idea to Tasks

You can't build "a backup system" in one sitting. Break it down:

1. **Research** - How do other backup tools work?
2. **Design** - What's my approach?
3. **Build** - Implement each component
4. **Test** - Verify it works
5. **Document** - Write instructions
6. **Deploy** - Set it up for real use

### Work Breakdown Structure Basics

Hierarchical decomposition:

```
Backup Tool
├── Core Features
│   ├── Select folders to backup
│   ├── Create timestamped archive
│   ├── Compress archive
│   └── Delete old backups
├── Scheduling
│   ├── Run on schedule
│   └── Run on demand
├── Notifications
│   ├── Success notification
│   └── Failure notification
└── Configuration
    ├── Config file format
    └── CLI arguments
```

### Task Granularity

**Too big**: "Build the backup feature"
- Not actionable—where do you start?

**Too small**: "Write line 1 of backup.py"
- Wastes time tracking

**Just right**: "Create function to list files in folder"
- Can complete in one sitting
- Clear when done

Rule of thumb: Tasks should take 30 minutes to 4 hours.

### Dependencies Between Tasks

Some tasks must come first:

```
[Design config format]
    → [Implement config loading]
        → [Implement CLI arguments]
```

Identify blockers early so you don't get stuck.

### Identifying Blockers

Blockers are dependencies you don't control:
- Waiting for API access
- Need to learn a technology
- Need hardware you don't have

Address blockers first or plan around them.

### The Walking Skeleton Approach

Build a minimal end-to-end version first:
1. Simplest possible backup (copy one file)
2. Simplest possible schedule (manual trigger)
3. Simplest possible notification (print to console)

Then enhance each part. You always have something working.

---

## 6.4 Requirements

### What Are Requirements?

Requirements describe what the system must do. They're the contract between "what you want" and "what you build."

### Functional Requirements

What the system does:
- "The system shall back up specified folders"
- "The system shall compress backups"
- "The system shall delete backups older than X days"

Use "shall" for clarity.

### Non-Functional Requirements

How the system does it:
- **Performance**: "Backups complete in under 5 minutes"
- **Reliability**: "Backups succeed 99% of the time"
- **Usability**: "Config takes under 5 minutes to set up"
- **Security**: "Backups are not readable by other users"

Often more important than functional requirements.

### User Stories

User-centric format:

```
As a [type of user],
I want [action/feature],
So that [benefit/value].
```

Examples:
```markdown
As a developer,
I want my project folders backed up daily,
So that I can recover accidentally deleted files.

As a user with limited disk space,
I want old backups automatically deleted,
So that backups don't fill my drive.
```

### Acceptance Criteria

How you know a story is done:

```markdown
**Story**: Daily backup of project folders

**Acceptance Criteria**:
- [ ] Backups run at the configured time
- [ ] All specified folders are included
- [ ] Backup file is created with timestamp
- [ ] Backup file is not empty
- [ ] Log entry is created
```

Each criterion is testable.

### Prioritization: MoSCoW Method

Categorize requirements:
- **Must have**: Core functionality (backup files)
- **Should have**: Important but not critical (compression)
- **Could have**: Nice to have (cloud upload)
- **Won't have**: Explicitly out of scope (real-time sync)

Focus on Musts first, then Shoulds.

---

## Concepts Covered

This module covered concepts 131-152:

131-135: Why plan (vs diving in, spectrum, right-sizing, personal projects, when to skip)
136-140: Defining your project (problem statement, goals, success criteria, scope, target users)
141-146: Breaking down work (idea to tasks, WBS, granularity, dependencies, blockers, walking skeleton)
147-152: Requirements (what they are, functional, non-functional, user stories, acceptance criteria, MoSCoW)

---

## Check Your Understanding

You should be able to:

- [ ] Explain when and how much to plan
- [ ] Write a clear problem statement
- [ ] Define goals, non-goals, and success criteria
- [ ] Break a project into actionable tasks
- [ ] Write user stories with acceptance criteria
- [ ] Prioritize requirements using MoSCoW

---

## Next Steps

Continue to **Module 7: Planning Tools and Techniques** to learn practical tools for managing your plans.
