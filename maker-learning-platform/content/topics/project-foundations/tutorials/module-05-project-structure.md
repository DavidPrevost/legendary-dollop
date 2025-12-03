# Module 5: Project Structure

A well-organized project is easier to navigate, maintain, and share. This module teaches you how to structure projects like a professional.

---

## 5.1 File Organization Principles

### Why Structure Matters

Good structure:
- Makes files easy to find
- Signals professionalism
- Enables tooling (tests, builds)
- Helps new contributors understand the codebase

Bad structure:
- Everything in one folder
- Random file names
- No separation between code, tests, and docs
- You can't find anything

### Separation of Concerns

Keep different types of files separate:
- **Source code** in one place
- **Tests** in another
- **Documentation** in another
- **Configuration** at the root

This makes it clear what each part does.

### Discoverability

A new person should be able to find:
- The main code (src/, lib/)
- The documentation (README, docs/)
- The configuration (config files at root)
- The tests (tests/)

Standard locations = instant understanding.

### Consistency Across Projects

Use the same structure for all your projects:
- Build muscle memory
- Reuse scripts and configs
- Reduce cognitive load
- Others will recognize the pattern

### Platform-Specific Conventions

Different ecosystems have conventions:
- **Python**: `src/`, `tests/`, `setup.py`
- **Node.js**: `src/`, `__tests__/`, `package.json`
- **Go**: Package-based, `cmd/`, `internal/`

Follow your ecosystem's conventions.

---

## 5.2 Common Directory Patterns

### Source Code Directories

Where your main code lives:

```
src/           # Common choice
lib/           # Libraries/packages
app/           # Application code
```

Python example:
```
src/
  myproject/
    __init__.py
    main.py
    utils.py
```

### Test Directories

Where tests live:

```
tests/         # Python, Go
__tests__/     # JavaScript (Jest)
spec/          # Ruby (RSpec)
test/          # General
```

Mirror your source structure:
```
src/
  utils.py
tests/
  test_utils.py
```

### Documentation Directories

```
docs/          # Detailed documentation
```

Contents might include:
- API documentation
- Architecture docs
- Tutorials
- ADRs (Architecture Decision Records)

### Configuration Files

Live at the project root:
```
config.yaml
.env
pyproject.toml
package.json
```

Root placement = easy to find.

### Build Output Directories

Where compiled/generated files go:

```
dist/          # Distribution packages
build/         # Build artifacts
out/           # Output
```

These are usually gitignored.

### Asset Directories

For static files:

```
assets/        # General assets
static/        # Web static files
images/        # Images
```

---

## 5.3 Naming Conventions

### File Naming

Common conventions:
- **lowercase-with-hyphens**: `user-profile.js`
- **lowercase_with_underscores**: `user_profile.py`
- **camelCase**: `userProfile.js`
- **PascalCase**: `UserProfile.cs`

Pick one and be consistent. For cross-platform, lowercase is safest.

### Directory Naming

Usually lowercase:
- `src/` not `Src/`
- `tests/` not `Tests/`
- `docs/` not `Documentation/`

### Case Sensitivity

**Warning**: macOS/Windows are case-insensitive, Linux is case-sensitive.

If you have `Config.yaml` and `config.yaml`, it will work on Mac but break on Linux. Always use consistent casing.

### Avoiding Special Characters

Avoid in file/folder names:
- Spaces (use hyphens/underscores)
- Special characters (`!@#$%`)
- Starting with dots (except hidden files)

Good: `my-project-config.yaml`
Bad: `My Project Config!.yaml`

### Descriptive vs Concise Names

Balance clarity and brevity:
- `utils.py` ✓ (concise, understood)
- `u.py` ✗ (too cryptic)
- `utility-functions-for-string-manipulation.py` ✗ (too verbose)

### Version Numbers in Names

Avoid versioning in filenames:
- `script_v2_final_FINAL.py` ✗

Use Git for versioning instead.

---

## 5.4 Standard Files

Every project should have these files at the root:

### README.md

What the project is and how to use it. (See Module 4)

### LICENSE

Legal terms for using your code.

Common licenses:
- **MIT** - Do whatever, just include the license
- **Apache 2.0** - Like MIT, with patent protection
- **GPL** - Must share modifications
- **Unlicense** - Public domain

Use [choosealicense.com](https://choosealicense.com) to decide.

### .gitignore

Files Git should ignore:
```gitignore
# Dependencies
node_modules/
venv/

# Build output
dist/
build/

# Environment
.env
.env.local

# IDE
.vscode/
.idea/

# OS
.DS_Store
Thumbs.db

# Logs
*.log
```

Use [gitignore.io](https://gitignore.io) for templates.

### CHANGELOG.md

Record of changes by version:
```markdown
# Changelog

## [Unreleased]
### Added
- New backup feature

## [1.0.0] - 2024-01-15
### Added
- Initial release
```

Follow [Keep a Changelog](https://keepachangelog.com) format.

### CONTRIBUTING.md

How others can contribute:
- How to report bugs
- How to request features
- How to submit PRs
- Code style guidelines

### Configuration Files

Language-specific config at root:
- `pyproject.toml` / `setup.py` (Python)
- `package.json` (Node.js)
- `Cargo.toml` (Rust)
- `go.mod` (Go)

### Environment Files

For secrets and environment-specific config:
- `.env` - Default environment
- `.env.example` - Template (committed)
- `.env.local` - Local overrides (not committed)

**Never commit actual `.env` files with secrets.**

---

## Putting It Together

### Example Python Project
```
my-backup-tool/
├── README.md
├── LICENSE
├── .gitignore
├── CHANGELOG.md
├── CONTRIBUTING.md
├── pyproject.toml
├── requirements.txt
├── src/
│   └── backup_tool/
│       ├── __init__.py
│       ├── main.py
│       ├── backup.py
│       └── utils.py
├── tests/
│   ├── test_backup.py
│   └── test_utils.py
├── docs/
│   ├── installation.md
│   └── configuration.md
└── examples/
    └── basic_usage.py
```

### Example JavaScript Project
```
my-dashboard/
├── README.md
├── LICENSE
├── .gitignore
├── package.json
├── src/
│   ├── index.js
│   ├── components/
│   └── utils/
├── __tests__/
│   └── index.test.js
├── public/
│   └── index.html
└── docs/
    └── api.md
```

---

## Concepts Covered

This module covered concepts 107-130:

107-111: Organization principles (why structure matters, separation, discoverability, consistency, conventions)
112-117: Common directories (src, tests, docs, config, build, assets)
118-123: Naming conventions (files, directories, case sensitivity, special chars, descriptive names, versioning)
124-130: Standard files (README, LICENSE, .gitignore, CHANGELOG, CONTRIBUTING, config, environment)

---

## Check Your Understanding

You should be able to:

- [ ] Explain why project structure matters
- [ ] Create a directory structure for a new project
- [ ] Choose appropriate file naming conventions
- [ ] List the standard files every project needs
- [ ] Create a proper .gitignore file

---

## Next Steps

Continue to **Module 6: Project Planning Basics** to learn how to plan before you build.

Or complete the **Level 2 Milestone Project: Project Scaffold** to apply these skills.
