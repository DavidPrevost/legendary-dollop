# Module 9: Technical Documentation

Professional projects need architecture docs, ADRs, API docs, and more. This module teaches you to create them.

---

## 9.1 Architecture Documentation

### What is Architecture Documentation?

Architecture docs explain the big picture:
- What components exist
- How they interact
- Why they're structured that way

Different from code comments (which explain details).

### When You Need Architecture Docs

- Project has multiple components
- Others will contribute
- You'll forget the design in 6 months
- You need to explain the system to stakeholders

### Context Diagrams

Show what your system interacts with:

```
                    ┌─────────┐
                    │  User   │
                    └────┬────┘
                         │
                         ↓
┌──────────┐      ┌─────────────┐      ┌──────────┐
│  Email   │ ←──  │   Backup    │ ──→  │  File    │
│  Server  │      │   System    │      │  System  │
└──────────┘      └─────────────┘      └──────────┘
                         │
                         ↓
                  ┌─────────────┐
                  │   Cloud     │
                  │   Storage   │
                  └─────────────┘
```

Shows external dependencies.

### Component Diagrams

Show internal structure:

```
┌─────────────────────────────────────┐
│           Backup System             │
├─────────────────────────────────────┤
│  ┌──────────┐    ┌──────────────┐   │
│  │   CLI    │───→│    Core      │   │
│  └──────────┘    └──────┬───────┘   │
│                         │           │
│         ┌───────────────┼───────┐   │
│         ↓               ↓       ↓   │
│  ┌──────────┐   ┌───────────┐ ┌───┐ │
│  │  Config  │   │  Storage  │ │Log│ │
│  └──────────┘   └───────────┘ └───┘ │
└─────────────────────────────────────┘
```

### Decision Records (ADRs)

Document significant decisions. See section 9.2.

### Keeping Architecture Docs Updated

Architecture changes less than code, but still changes:
- Review when major features are added
- Update diagrams when structure changes
- Note what's outdated if you can't update

---

## 9.2 Architecture Decision Records (ADRs)

### What is an ADR?

A document that captures:
- A significant decision
- The context around it
- Why you decided that way
- The consequences

### ADR Format

```markdown
# ADR-001: Use SQLite for Local Storage

## Status
Accepted

## Context
We need to store backup metadata locally. Options:
- JSON files
- SQLite database
- PostgreSQL

## Decision
Use SQLite for local metadata storage.

## Rationale
- No server needed (SQLite is embedded)
- Supports complex queries (unlike JSON)
- Single file (easy to backup)
- Python has built-in support

## Consequences
- Limited to single-writer (fine for this use)
- Users don't need to install a database
- Easy to inspect with DB tools
```

### When to Write an ADR

Write an ADR when:
- Choosing between alternatives
- Decision is hard to reverse
- Others will wonder "why this way?"
- You'll forget the reasoning

### Good ADR Topics

- Database choice
- Framework/language selection
- API design approach
- Authentication method
- Deployment strategy
- Architecture patterns

Not: "Use tabs vs spaces" (too minor)

---

## 9.3 API Documentation

### What is API Documentation?

Docs that let someone use your functions/endpoints without reading source code.

### Endpoint/Function Documentation Format

```markdown
## backup_folder

Create a backup of the specified folder.

### Signature
```python
backup_folder(source: str, dest: str, compress: bool = True) -> BackupResult
```

### Parameters
| Name | Type | Required | Description |
|------|------|----------|-------------|
| source | str | Yes | Path to folder to backup |
| dest | str | Yes | Path to save backup |
| compress | bool | No | Compress backup (default: True) |

### Returns
`BackupResult` with:
- `success`: bool
- `file_path`: str
- `size_bytes`: int
- `duration_seconds`: float

### Example
```python
result = backup_folder("/home/user/docs", "/backups")
if result.success:
    print(f"Backed up to {result.file_path}")
```

### Errors
- `FileNotFoundError`: Source path doesn't exist
- `PermissionError`: Can't read source or write to dest
- `DiskFullError`: Not enough space for backup
```

### Request/Response Examples

For REST APIs:

```markdown
## POST /backup

Create a new backup.

### Request
```json
{
  "source": "/home/user/docs",
  "destination": "/backups",
  "compress": true
}
```

### Response
```json
{
  "id": "backup_20240115_143022",
  "status": "completed",
  "size_bytes": 1048576,
  "file_path": "/backups/backup_20240115_143022.tar.gz"
}
```
```

### Error Documentation

```markdown
### Errors

| Code | Description |
|------|-------------|
| 400 | Invalid request body |
| 404 | Source path not found |
| 500 | Internal server error |
```

### Authentication Documentation

If auth is required:

```markdown
## Authentication

All endpoints require an API key in the header:

```
Authorization: Bearer YOUR_API_KEY
```

Get your key from Settings → API Keys.
```

---

## 9.4 Configuration Documentation

### Documenting Config Files

```markdown
## Configuration

Create `config.yaml` in the project root:

```yaml
# Backup Configuration

backup:
  # Folders to include in backup (required)
  folders:
    - ~/Documents
    - ~/Projects

  # Where to save backups (required)
  destination: ~/Backups

  # Compress backups (optional, default: true)
  compress: true

  # Delete backups older than this (optional, default: 30)
  retention_days: 30

notifications:
  # Email on failure (optional)
  email: you@example.com
```
```

### Environment Variables

```markdown
## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| BACKUP_CONFIG | Path to config file | ./config.yaml |
| BACKUP_LOG_LEVEL | Log verbosity | INFO |
| SMTP_HOST | Email server | localhost |
| SMTP_PORT | Email port | 587 |
```

### Default Values

Always document defaults:
- What happens if not specified
- Sensible defaults require less config

### Required vs Optional Settings

Mark clearly:

```yaml
backup:
  folders:       # Required
  destination:   # Required
  compress:      # Optional (default: true)
```

### Configuration Examples

Provide complete, working examples:

```markdown
### Minimal Configuration
```yaml
backup:
  folders:
    - ~/Documents
  destination: ~/Backups
```

### Full Configuration
```yaml
backup:
  folders:
    - ~/Documents
    - ~/Projects
  destination: ~/Backups
  compress: true
  retention_days: 14

notifications:
  email: you@example.com

logging:
  level: DEBUG
  file: ~/backup.log
```
```

---

## 9.5 Changelog and Versioning

### What is a Changelog?

A record of changes between versions:
- What was added
- What changed
- What was fixed
- What was removed

### Keep a Changelog Format

Standard format:

```markdown
# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased]
### Added
- Cloud backup support

## [1.1.0] - 2024-01-20
### Added
- Compression option
### Fixed
- Backup fails on empty folders

## [1.0.0] - 2024-01-15
### Added
- Initial release
- Basic backup functionality
- Email notifications
```

### Semantic Versioning

MAJOR.MINOR.PATCH (e.g., 1.2.3)

- **MAJOR**: Breaking changes (1.x → 2.0)
- **MINOR**: New features, backward compatible (1.1 → 1.2)
- **PATCH**: Bug fixes (1.2.3 → 1.2.4)

### When to Bump Versions

| Change | Version Bump |
|--------|-------------|
| Bug fix | Patch (x.x.1) |
| New feature | Minor (x.1.0) |
| Breaking change | Major (1.0.0) |

### Release Notes vs Changelog

- **Changelog**: Technical, every change
- **Release notes**: User-facing, highlights

Both are useful.

---

## Concepts Covered

This module covered concepts 199-221:

199-204: Architecture documentation (what, when, context diagrams, components, ADRs, keeping updated)
205-210: API documentation (what, format, examples, errors, auth)
211-215: Configuration documentation (config files, env vars, defaults, required/optional, examples)
216-221: Changelog and versioning (what, format, semver, when to bump, release notes)

---

## Check Your Understanding

You should be able to:

- [ ] Create architecture diagrams
- [ ] Write an ADR with proper format
- [ ] Document an API endpoint completely
- [ ] Document configuration options
- [ ] Maintain a changelog with semantic versioning

---

## Next Steps

Continue to **Module 10: Documentation Workflow** to learn how to maintain docs effectively.
