# Module 10: Documentation Workflow

Good documentation requires good process. This module teaches you how to write, review, and maintain docs effectively.

---

## 10.1 Writing Process

### Start with an Outline

Before writing, structure your document:

```markdown
# Backup System Architecture

## Overview
- What is this document

## Context
- What the system interacts with

## Components
- Main parts and their responsibilities

## Data Flow
- How data moves through the system

## Decisions
- Key architectural choices
```

Outlines prevent rambling.

### Write the First Draft Quickly

Don't edit while writing:
- Get ideas down
- Don't worry about perfection
- Fill in details later

First draft is for you. Editing is for readers.

### Edit for Clarity

After drafting, improve:
- Remove unnecessary words
- Simplify complex sentences
- Add examples
- Improve structure

Read aloud—if it sounds awkward, rewrite it.

### Get Feedback

Share with someone who will use the docs:
- Can they follow the instructions?
- What's confusing?
- What's missing?

Fresh eyes catch what you miss.

### Iterate and Improve

Documentation is never "done":
- Incorporate feedback
- Update when things change
- Improve based on questions

---

## 10.2 Documentation Review

### Self-Review Checklist

Before sharing:

- [ ] Headings form a logical outline
- [ ] Examples are complete and tested
- [ ] No placeholder text ("TODO", "TBD")
- [ ] Links work
- [ ] Code blocks have language hints
- [ ] Spelling and grammar checked
- [ ] Consistent formatting

### Peer Review for Docs

Like code review, but for docs:
- Is it clear?
- Is it accurate?
- Is anything missing?
- Can you follow the steps?

### Testing Documentation

**Follow your own instructions**:
1. Set up a fresh environment
2. Follow your installation docs
3. Note every stumble
4. Fix the docs

If you can't follow them, no one can.

### Common Documentation Issues

| Issue | Solution |
|-------|----------|
| Too much jargon | Define terms or use simpler words |
| Missing context | Add overview/background section |
| Wall of text | Break into sections, add lists |
| Outdated examples | Test examples before publishing |
| Assumed knowledge | Make prerequisites explicit |

### Proofreading Tips

- Read backwards (catches typos)
- Read aloud (catches awkward phrasing)
- Use spell check (but don't rely on it)
- Print it out (see it differently)
- Wait a day (fresh perspective)

---

## 10.3 Keeping Docs Current

### Documentation Rot

Docs get stale:
- Features change but docs don't
- Examples use old syntax
- Links break
- Screenshots show old UI

Stale docs are dangerous—they mislead.

### Triggers for Updates

Update docs when:
- You change code behavior
- You add features
- You fix bugs that affect usage
- You hear "the docs are wrong"
- Dependencies change

### Documentation Alongside Code

Make it part of development:
- Write docs before merging
- Review docs with code
- Docs in same pull request as code

If it's not documented, it doesn't ship.

### Periodic Documentation Review

Schedule reviews:
- Monthly: Check for broken links
- Quarterly: Test installation instructions
- Yearly: Major review and cleanup

Add to your calendar.

### Archiving Outdated Docs

Don't delete—archive:
- Move to `docs/archive/`
- Note "This is for version X"
- Link to current version

Users of old versions need old docs.

---

## 10.4 Documentation as Code

### Docs in Version Control

Treat docs like code:
- Store in Git
- Track changes
- Branch and merge
- Review before merging

Same workflow as code.

### Docs Review in Pull Requests

Include docs in PRs:
- "Adds feature X and updates docs"
- Reviewer checks both code and docs
- Docs must pass review to merge

### Automated Doc Generation

Generate docs from code:
- API docs from docstrings
- Config docs from schemas
- README badges from status

Tools: Sphinx (Python), JSDoc (JS), godoc (Go)

### Doc Testing and Linting

Automate quality checks:
- Spell checking (vale, aspell)
- Link checking (markdown-link-check)
- Style linting (markdownlint)
- Example testing (doctest)

Add to CI pipeline.

### Continuous Documentation

Just like continuous integration:
- Docs build on every commit
- Deploy docs automatically
- Preview docs in PRs

Tools: ReadTheDocs, GitHub Pages, Netlify

---

## Concepts Covered

This module covered concepts 222-241:

222-226: Writing process (outline, first draft, editing, feedback, iteration)
227-231: Documentation review (self-review, peer review, testing, common issues, proofreading)
232-236: Keeping docs current (rot, triggers, alongside code, periodic review, archiving)
237-241: Documentation as code (version control, PR review, auto-generation, linting, continuous docs)

---

## Check Your Understanding

You should be able to:

- [ ] Outline a document before writing
- [ ] Self-review documentation before sharing
- [ ] Identify and fix common documentation issues
- [ ] Explain when documentation needs updating
- [ ] Describe how to treat docs like code

---

## Next Steps

Continue to **Module 11: Planning Your First Project** to put everything together.

Or complete the **Level 4 Milestone Project: Documentation Suite** to demonstrate mastery.
