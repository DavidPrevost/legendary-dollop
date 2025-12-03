# Module 3: Markdown Fundamentals

Markdown is the standard way to write documentation. This module teaches you everything you need to create well-formatted documents.

---

## 3.1 What is Markdown?

### Markdown as a Lightweight Markup Language

Markdown is a way to format text using simple symbols. Instead of clicking buttons in a word processor, you type characters like `#`, `*`, and `-` to indicate formatting.

```markdown
# This is a heading
This is **bold** and this is *italic*.
- This is a list item
```

When rendered, this becomes:
- A large heading
- Bold and italic text
- A bullet point

### Why Markdown is Popular

1. **Readable as plain text** - Even without rendering, Markdown is easy to read
2. **Portable** - Works everywhere: GitHub, VS Code, note apps, wikis
3. **Simple** - Learn the basics in minutes
4. **Version control friendly** - It's just text, so diffs work perfectly
5. **Convertible** - Export to HTML, PDF, Word, and more

### Where Markdown is Used

- **GitHub** - README files, issues, comments, wikis
- **Documentation** - Most developer docs are Markdown
- **Note-taking** - Obsidian, Notion, Bear
- **Static sites** - Jekyll, Hugo, MkDocs
- **Messaging** - Slack, Discord (limited support)

### Markdown Flavors

The core syntax is standardized (CommonMark), but platforms add extensions:

- **GitHub Flavored Markdown (GFM)** - Task lists, tables, autolinks
- **Obsidian Markdown** - Wikilinks, callouts
- **Pandoc Markdown** - Citations, footnotes

This tutorial uses GFM since you'll likely use GitHub.

### Markdown File Extension

Markdown files use the `.md` extension:
- `README.md`
- `CHANGELOG.md`
- `notes.md`

---

## 3.2 Text Formatting

### Paragraphs and Line Breaks

Paragraphs are separated by blank lines:

```markdown
This is the first paragraph.

This is the second paragraph.
```

For a line break within a paragraph, end the line with two spaces or use `<br>`:

```markdown
Line one
Line two
```

### Bold Text

Wrap with double asterisks or underscores:

```markdown
This is **bold** text.
This is also __bold__ text.
```

Use `**asterisks**` for consistency.

### Italic Text

Wrap with single asterisks or underscores:

```markdown
This is *italic* text.
This is also _italic_ text.
```

Use `*asterisks*` for consistency.

### Bold and Italic Combined

```markdown
This is ***bold and italic*** text.
```

### Strikethrough Text

Wrap with double tildes (GFM extension):

```markdown
This is ~~strikethrough~~ text.
```

### Inline Code

Wrap with backticks for code within a sentence:

```markdown
Run the `npm install` command.
The variable `userName` stores the name.
```

---

## 3.3 Headings and Structure

### Heading Levels

Use `#` symbols for headings (1-6 levels):

```markdown
# Heading 1 (Title)
## Heading 2 (Major section)
### Heading 3 (Subsection)
#### Heading 4 (Sub-subsection)
##### Heading 5 (Rarely used)
###### Heading 6 (Rarely used)
```

### Heading Hierarchy

**Do this:**
```markdown
# Project Title
## Installation
### Prerequisites
### Steps
## Usage
## Configuration
```

**Don't do this:**
```markdown
# Project Title
### Skipped heading 2!
##### Way too deep
```

Always use headings in order. Don't skip levels.

### When to Use Each Level

- **H1 (#)** - Document title only (usually one per document)
- **H2 (##)** - Major sections
- **H3 (###)** - Subsections within H2
- **H4-H6** - Further nesting (use sparingly)

### Horizontal Rules

Create a horizontal line with three or more hyphens, asterisks, or underscores:

```markdown
---
```

Use to separate major sections.

### Document Outline Best Practices

- Start with a single H1 (the title)
- Use H2 for top-level sections
- Think of your document as an outline
- Headings should be scannable—someone should understand the structure from headings alone

---

## 3.4 Lists

### Unordered Lists

Use `-`, `*`, or `+` (pick one and be consistent):

```markdown
- First item
- Second item
- Third item
```

Or:

```markdown
* First item
* Second item
* Third item
```

### Ordered Lists

Use numbers followed by periods:

```markdown
1. First step
2. Second step
3. Third step
```

The numbers don't have to be sequential—Markdown renumbers them:

```markdown
1. First
1. Second
1. Third
```

Still renders as 1, 2, 3.

### Nested Lists

Indent with spaces (usually 2 or 4):

```markdown
- Parent item
  - Child item
  - Another child
    - Grandchild
- Another parent
```

### Task Lists

GFM extension for checkboxes:

```markdown
- [x] Completed task
- [ ] Incomplete task
- [ ] Another todo
```

Renders as checkboxes.

### List Formatting Best Practices

- Use unordered lists for items without sequence
- Use ordered lists for steps or rankings
- Be consistent with markers (`-` vs `*`)
- Don't over-nest (3 levels max)

---

## 3.5 Links and Images

### Inline Links

```markdown
[Link text](https://example.com)
```

Example:
```markdown
Check out [GitHub](https://github.com) for more info.
```

### Reference-Style Links

Define links separately for cleaner text:

```markdown
Check out [GitHub][gh] and [GitLab][gl].

[gh]: https://github.com
[gl]: https://gitlab.com
```

Useful for repeated links or long URLs.

### Relative Links

Link to other files in your project:

```markdown
See the [installation guide](docs/installation.md).
Read the [changelog](../CHANGELOG.md).
```

### Anchor Links

Link to headings within the same document:

```markdown
See the [Installation](#installation) section.
```

The anchor is the heading text, lowercased, with spaces as hyphens.

### Images

```markdown
![Alt text](image-url.png)
```

Example:
```markdown
![Project logo](images/logo.png)
```

Alt text describes the image for accessibility.

### Image Sizing

Standard Markdown doesn't support sizing. Use HTML:

```markdown
<img src="image.png" alt="Description" width="300">
```

### Linking Images

Wrap image syntax in link syntax:

```markdown
[![Alt text](image.png)](https://example.com)
```

Clicking the image follows the link.

---

## 3.6 Code

### Inline Code

Use single backticks:

```markdown
Run `npm start` to begin.
```

### Fenced Code Blocks

Use triple backticks:

````markdown
```
Code goes here
Multiple lines
```
````

### Syntax Highlighting

Add the language after the opening backticks:

````markdown
```python
def greet(name):
    return f"Hello, {name}!"
```
````

````markdown
```javascript
function greet(name) {
  return `Hello, ${name}!`;
}
```
````

````markdown
```bash
#!/bin/bash
echo "Hello, World!"
```
````

Common language identifiers: `python`, `javascript`, `bash`, `json`, `yaml`, `html`, `css`, `sql`

### Indented Code Blocks

Indent with 4 spaces (older style, avoid):

```markdown
    This is code
    More code
```

Use fenced blocks instead—they support syntax highlighting.

### Code Block Best Practices

- Always specify the language for syntax highlighting
- Use inline code for short snippets within sentences
- Use fenced blocks for multi-line code
- Keep code blocks focused—don't dump entire files

---

## 3.7 Advanced Markdown

### Blockquotes

Prefix with `>`:

```markdown
> This is a quote.
> It can span multiple lines.
>
> And multiple paragraphs.
```

Nest quotes with multiple `>`:

```markdown
> Main quote
> > Nested quote
```

### Tables

Create tables with pipes and hyphens:

```markdown
| Header 1 | Header 2 | Header 3 |
|----------|----------|----------|
| Cell 1   | Cell 2   | Cell 3   |
| Cell 4   | Cell 5   | Cell 6   |
```

### Table Alignment

Use colons in the separator row:

```markdown
| Left | Center | Right |
|:-----|:------:|------:|
| L    |   C    |     R |
```

- `:---` Left align
- `:---:` Center align
- `---:` Right align

### Escaping Special Characters

Use backslash to show literal characters:

```markdown
\*Not italic\*
\# Not a heading
```

### HTML in Markdown

You can use HTML when Markdown isn't enough:

```markdown
<details>
<summary>Click to expand</summary>

Hidden content here.

</details>
```

Use sparingly—it reduces portability.

### Emoji Shortcodes

GFM supports emoji codes:

```markdown
:smile: :rocket: :thumbsup:
```

See [emoji cheat sheet](https://www.webfx.com/tools/emoji-cheat-sheet/) for codes.

### Footnotes

GFM extension:

```markdown
Here's a statement[^1].

[^1]: This is the footnote text.
```

---

## Concepts Covered

This module covered concepts 41-80:

41-45: What is Markdown, why it's popular, where it's used, flavors, file extension
46-51: Text formatting (paragraphs, bold, italic, strikethrough, inline code)
52-56: Headings and structure (levels, hierarchy, horizontal rules)
57-61: Lists (unordered, ordered, nested, task lists)
62-68: Links and images (inline, reference, relative, anchor, images)
69-73: Code (inline, fenced blocks, syntax highlighting)
74-80: Advanced (blockquotes, tables, escaping, HTML, emoji, footnotes)

---

## Check Your Understanding

You should now be able to:

- [ ] Create documents with proper heading hierarchy
- [ ] Format text with bold, italic, and code
- [ ] Create ordered and unordered lists
- [ ] Add links and images
- [ ] Write code blocks with syntax highlighting
- [ ] Create tables with alignment

---

## Practice Exercise

Create a Markdown document that includes:
1. A title (H1) and at least two sections (H2)
2. Bold and italic text
3. An unordered list and an ordered list
4. A task list with some items checked
5. A link to any website
6. A code block with syntax highlighting
7. A table with at least 3 columns

---

## Next Steps

Continue to **Module 4: README Files** to learn how to apply Markdown to project documentation.

Or complete the **Level 1 Milestone Project: Personal README** to practice these skills.
