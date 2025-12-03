# Command Line Mastery - Level Structure

## Overview

- **Total Levels**: 5 (0-4)
- **Total Concepts**: 380
- **Estimated Total Time**: 30-42 hours

*Note: Time estimates updated based on UX simulation (+15-20%)*

---

## Level 0: Curious (Terminal Newcomer)

**Concepts**: 1-55 (55 concepts)
**Modules**: 1-2
**Time Estimate**: 4-5 hours

### Description
First contact with the terminal. Learn what a terminal is, why it's useful, and how to navigate your file system. By the end, you'll be comfortable moving around directories and understanding paths.

### What You'll Learn
- Terminal basics and shells
- Opening and configuring terminal
- Basic navigation (pwd, cd, ls)
- Paths (absolute, relative)
- Tab completion

### Prerequisites
- None (entry level)

### Comparison Band
Novice - No prior terminal experience required.

### Exit Criteria
- Can open terminal on their system
- Navigate to any directory using cd
- List directory contents
- Understand the difference between absolute and relative paths
- Use tab completion for paths

---

## Level 1: Explorer (File Handler)

**Concepts**: 56-125 (70 concepts)
**Modules**: 3-4
**Time Estimate**: 5-7 hours

### Description
Master file operations and learn to view file contents efficiently. Create, copy, move, and delete files with confidence. Understand permissions and how to read files in different ways.

### What You'll Learn
- Creating files and directories
- Copying, moving, deleting
- File permissions (Unix)
- Viewing files (cat, less, head, tail)
- Comparing files

### Prerequisites
- Level 0 completion (basic navigation)

### Comparison Band
Novice → Competent - Can perform basic file operations.

### Exit Criteria
- Create and organize project directories
- Copy and move files safely
- Understand and read permission strings
- View large files efficiently with less
- Compare two files for differences

---

## Level 2: Tinkerer (Search Specialist)

**Concepts**: 126-205 (80 concepts)
**Modules**: 5-6
**Time Estimate**: 7-10 hours

### Description
Find anything in your system and transform text like a pro. Master find and grep for searching, then learn text processing tools like sort, cut, sed, and awk.

### What You'll Learn
- Finding files (find command)
- Searching text (grep, regex basics)
- Sorting and filtering (sort, uniq)
- Text manipulation (cut, sed, awk)
- Data transformation

### Prerequisites
- Level 1 completion (file operations)

### Comparison Band
Competent - Can search and process text data effectively.

### Exit Criteria
- Find files by name, size, or date
- Search for patterns in files using grep
- Write basic regular expressions
- Sort and deduplicate data
- Extract and transform columns of data

---

## Level 3: Builder (Pipeline Architect)

**Concepts**: 206-295 (90 concepts)
**Modules**: 7-9
**Time Estimate**: 6-9 hours

### Description
Combine commands into powerful pipelines and manage your environment. Understand I/O streams, master piping, configure your shell, and control processes.

### What You'll Learn
- Pipes and redirection
- Environment variables
- Shell configuration
- Process management
- Job control

### Prerequisites
- Level 2 completion (search and text processing)

### Comparison Band
Competent → Proficient - Can build multi-stage command pipelines.

### Exit Criteria
- Chain commands with pipes effectively
- Redirect output to files or other commands
- Set up persistent aliases and environment variables
- Monitor and control running processes
- Run background tasks and bring them to foreground

---

## Level 4: Maker (Automation Master)

**Concepts**: 296-380 (85 concepts)
**Modules**: 10-12
**Time Estimate**: 6-8 hours

### Description
Automate tasks with shell scripts and use network commands. Write maintainable scripts with arguments, loops, and error handling. Connect to remote systems and download files.

### What You'll Learn
- Shell scripting fundamentals
- Control flow (if, for, while)
- Script arguments and exit codes
- Network commands (curl, ssh)
- Advanced shell features

### Prerequisites
- Level 3 completion (pipes and environment)

### Comparison Band
Proficient → Expert - Can write automation scripts and use network tools.

### Exit Criteria
- Write scripts with arguments and error handling
- Use loops and conditionals appropriately
- Download files and interact with APIs via curl
- Connect to remote systems with SSH
- Apply quoting and expansion rules correctly

---

## Level Progression Summary

| Level | Name | Concepts | Modules | Hours | Band |
|-------|------|----------|---------|-------|------|
| 0 | Curious | 55 | 1-2 | 3-4 | Novice |
| 1 | Explorer | 70 | 3-4 | 4-6 | Novice→Competent |
| 2 | Tinkerer | 80 | 5-6 | 6-8 | Competent |
| 3 | Builder | 90 | 7-9 | 6-9 | Competent→Proficient |
| 4 | Maker | 85 | 10-12 | 6-8 | Proficient→Expert |

---

## Platform Coverage

Each level includes coverage of:
- **Unix/Linux**: Bash commands
- **macOS**: Terminal.app/iTerm2 with Bash/Zsh
- **Windows**: PowerShell equivalents, CMD where relevant

Cross-platform differences are highlighted throughout, with equivalent commands shown for each environment.

---

## Integration with Other Subjects

### Feeds Into
- **Bash/Shell** (Subject 4): Deep dive into shell scripting
- **Git/GitHub** (Subject 6): Uses terminal for version control
- **Docker/Compose** (Subject 8): Docker CLI commands
- **Python** (Subject 3): Running Python from terminal

### Receives From
- **Project Foundations** (Subject 1): Documentation and planning skills
