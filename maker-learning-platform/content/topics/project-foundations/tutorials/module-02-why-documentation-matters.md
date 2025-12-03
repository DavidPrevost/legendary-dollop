# Module 2: Why Documentation Matters

Every maker needs documentation skills. This module explains why and introduces the types and principles of good documentation.

---

## 2.1 The Case for Documentation

### What is Documentation?

Documentation is any written material that explains your project:

- How to use it
- How it works
- How to contribute to it
- Why decisions were made

It can be as simple as comments in your code or as complex as a full website with tutorials, references, and API guides.

### Why Makers Need Documentation

**"I'll remember how this works."** - No, you won't.

Even personal projects need documentation because:

1. **Future-you is a stranger** - In six months, you won't remember why you wrote that script or what those config values mean
2. **Context switches are expensive** - Coming back to a project without docs means re-learning it from scratch
3. **You'll want to share** - That script that fixed your problem will help others
4. **Debugging is easier** - When something breaks, docs help you understand what it was supposed to do

### Documentation as a Gift to Future-You

Think of documentation as a gift to yourself in the future. When you write:

- "This value must be at least 10 or the script crashes"
- "Run the backup before modifying these files"
- "This API returns dates in UTC, not local time"

...you're saving hours of frustration for future-you who has completely forgotten these details.

### Documentation for Collaboration

If you ever want to:
- Share your project with others
- Get help debugging
- Have someone contribute improvements
- Hand off maintenance

...you need documentation. Without it, people can't use your project, no matter how good the code is.

### The Cost of Poor Documentation

Poor documentation leads to:
- Abandoned projects (you forgot how they work)
- Wasted time (re-figuring things out)
- Frustrated users (can't get it working)
- No contributions (can't understand the code)
- Security issues (misconfiguration)

### Minimum Viable Documentation

You don't need to write a book for every script. **Minimum viable documentation** includes:

- What it does (one sentence)
- How to run it
- Any requirements or dependencies
- Configuration options (if any)

This takes 5 minutes and saves hours.

---

## 2.2 Types of Documentation

### User Documentation

**Who**: People using your project
**Goal**: Get them up and running

Includes:
- Installation instructions
- Usage examples
- Configuration guide
- Troubleshooting tips
- FAQ

### Developer Documentation

**Who**: People maintaining or extending the code
**Goal**: Help them understand how it works

Includes:
- Architecture overview
- Code organization
- Design decisions
- API references
- Development setup

### Process Documentation

**Who**: Contributors
**Goal**: Show them how to participate

Includes:
- How to report bugs
- How to suggest features
- Code style guidelines
- Pull request process
- Release procedures

### Reference Documentation

**Who**: Anyone who needs to look something up
**Goal**: Quick answers to specific questions

Includes:
- Command reference
- Configuration options
- API endpoints
- Error codes
- Glossary

### Tutorial Documentation

**Who**: Learners
**Goal**: Teach concepts through guided examples

Includes:
- Step-by-step guides
- Conceptual explanations
- Worked examples
- Exercises

### Inline Documentation

**Who**: Anyone reading the code
**Goal**: Explain non-obvious code

Includes:
- Code comments
- Docstrings
- Type annotations
- TODO markers

---

## 2.3 Documentation Principles

### Write for Your Audience

Different readers need different information:

- **New users** need quick start guides
- **Experienced users** need references
- **Contributors** need architecture overviews
- **Future-you** needs context and rationale

Ask: "Who will read this and what do they need to know?"

### Keep It Simple and Clear

- Use plain language
- Avoid jargon (or define it)
- Short sentences
- One idea per paragraph
- Active voice ("Run the command" not "The command should be run")

### Use Examples Liberally

Show, don't just tell:

❌ "The script accepts a filename parameter"
✅ "The script accepts a filename parameter: `python backup.py /path/to/file.txt`"

Real examples with real values beat abstract descriptions.

### Structure for Scanning

People scan documentation; they don't read every word.

- Use headings to organize
- Use bullet points for lists
- Use code blocks for commands
- Use tables for comparisons
- Put the most important information first

### Keep Documentation Close to Code

Documentation far from code gets outdated. Keep:

- README in the project root
- Code comments in the code
- API docs near the API code
- Config docs near the config

When you change code, the documentation is right there to remind you.

### Update Documentation with Changes

**Documentation rot** is when docs describe old behavior. Every code change should prompt:

- Does the README need updating?
- Are the examples still correct?
- Did the API change?
- Are there new configuration options?

Outdated documentation is worse than no documentation—it actively misleads.

### Don't Document What Code Makes Obvious

Bad comment:
```python
# Add 1 to x
x = x + 1
```

Good comment:
```python
# Offset by 1 because the API uses 1-based indexing
x = x + 1
```

Document the **why**, not the **what**. The code shows what; only comments can explain why.

---

## Concepts Covered

This module covered concepts 22-40:

22. What is documentation
23. Why makers need documentation
24. Documentation as a gift to future-you
25. Documentation for collaboration
26. The cost of poor documentation
27. Minimum viable documentation concept
28. User documentation
29. Developer documentation
30. Process documentation
31. Reference documentation
32. Tutorial documentation
33. Inline documentation
34. Write for your audience
35. Keep it simple and clear
36. Use examples liberally
37. Structure for scanning
38. Keep documentation close to code
39. Update documentation with changes
40. Don't document what code makes obvious

---

## Check Your Understanding

Before moving on, you should be able to:

- [ ] Explain why personal projects need documentation
- [ ] Identify the six types of documentation
- [ ] List the components of minimum viable documentation
- [ ] Describe three documentation principles
- [ ] Explain what "documentation rot" is

---

## Next Steps

Continue to **Module 3: Markdown Fundamentals** to learn the syntax you'll use for all your documentation.

Or complete the **Level 0 Milestone Project: Platform Explorer** if you haven't already.
