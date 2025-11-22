# Maker Learning Platform

A learning platform for hobbyists and tinkerers who want to understand and control their digital world.

**This is NOT another coding bootcamp.** This is for makers who want to automate their homes, understand their technology stack, and build useful personal tools.

## Quick Start

### Prerequisites

- Python 3.8 or higher
- That's it! Start with just a laptop.

### Installation

#### Windows (PowerShell)

```powershell
# Clone the repository
git clone https://github.com/DavidPrevost/legendary-dollop.git
cd legendary-dollop/maker-learning-platform

# Create virtual environment
python -m venv venv

# Activate virtual environment
.\venv\Scripts\Activate.ps1

# Install dependencies
pip install -e .
```

#### macOS/Linux (Bash)

```bash
# Clone the repository
git clone https://github.com/DavidPrevost/legendary-dollop.git
cd legendary-dollop/maker-learning-platform

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -e .
```

### First Run

```bash
# Check your system capabilities
maker check

# See what you can learn
maker explore

# Start your first project
maker start python/tinkerer/file-organizer
```

## What Makes This Different

- **Capability-aware**: Knows what hardware and software you have
- **Life-improving**: Every project solves a real problem
- **Choose your adventure**: Multiple valid paths based on your interests
- **Integration-focused**: Real projects combine multiple skills
- **Hackable**: The platform itself is a learning project

## Core Principles

1. **Breadth over depth** - We celebrate generalists
2. **Practical over perfect** - Working code beats pristine code
3. **Flexible paths** - Non-linear progression based on interests
4. **Integration focus** - Real projects combine multiple skills
5. **Accessibility first** - Start with just a laptop
6. **User agency** - No gatekeeping, you choose your path

Read the full principles in [docs/CORE_PRINCIPLES.md](docs/CORE_PRINCIPLES.md).

## Documentation

- [Project Vision](docs/PROJECT_VISION.md) - Why this exists
- [Core Principles](docs/CORE_PRINCIPLES.md) - Our immutable values
- [Architecture Decisions](docs/ARCHITECTURE_DECISIONS.md) - Technical choices and rationale
- [Roadmap](docs/ROADMAP.md) - Development phases and plans

## Project Structure

```
maker-learning-platform/
├── docs/                    # Documentation
├── core/                    # Core platform logic
│   ├── capability_checker/  # System detection
│   ├── progress_tracker/    # Learning progress
│   ├── skill_tree/          # Skill relationships
│   └── project_validator/   # Project completion
├── content/                 # Learning content
│   ├── languages/           # Language-specific content
│   ├── skills/              # Skill definitions
│   └── integrations/        # Cross-skill projects
├── platform/                # Platform interfaces
│   └── cli/                 # Command-line interface
└── tools/                   # Development tools
    └── context_manager/     # Session management
```

## Development

### Setup Development Environment

```bash
# After activating venv
pip install -e ".[dev]"
```

### Running Tests

```bash
pytest
```

### Code Style

```bash
# Format code
black .

# Lint code
ruff check .
```

## Contributing

We welcome contributions! Please read our principles first - every contribution should align with them.

## License

MIT License - See LICENSE file for details.

---

*Built for people who want to automate their coffee maker today and have the skills to become a DevOps engineer tomorrow.*
