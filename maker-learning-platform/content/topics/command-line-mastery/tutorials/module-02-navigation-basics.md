# Module 2: Navigation Basics

**Concepts Covered**: 26-55
**Estimated Time**: 35-45 minutes

---

## File System Hierarchy

Your computer organizes files in a tree structure:

```
/ (root)
├── home/
│   └── username/
│       ├── Documents/
│       ├── Downloads/
│       └── projects/
├── usr/
├── etc/
└── tmp/
```

Windows:
```
C:\
├── Users\
│   └── username\
│       ├── Documents\
│       ├── Downloads\
│       └── projects\
├── Program Files\
└── Windows\
```

---

## Key Directories

- **Root** (`/` or `C:\`): Top of the file system
- **Home** (`~` or `C:\Users\username`): Your personal space
- **Current** (`.`): Where you are now
- **Parent** (`..`): One level up

---

## Navigation Commands

### Print Working Directory

```bash
pwd
```

Shows where you are right now.

### List Contents

```bash
ls
```

PowerShell/CMD:
```cmd
dir
```

### Change Directory

```bash
cd Documents
```

---

## List Options (ls)

### Detailed list
```bash
ls -l
```
Shows permissions, owner, size, date.

### Show hidden files
```bash
ls -a
```
Hidden files start with `.` (like `.bashrc`).

### Human-readable sizes
```bash
ls -lh
```
Shows KB, MB, GB instead of bytes.

### Combine options
```bash
ls -lah
```
All details, hidden files, human sizes.

Windows PowerShell:
```powershell
Get-ChildItem -Force  # shows hidden
ls -Force             # shorthand
```

---

## Absolute vs Relative Paths

### Absolute Paths
Start from root - always work regardless of where you are:
```bash
cd /home/username/Documents
```

Windows:
```cmd
cd C:\Users\username\Documents
```

### Relative Paths
Relative to your current location:
```bash
cd Documents       # go into Documents here
cd ../Downloads    # up one, then into Downloads
```

---

## Path Shortcuts

| Shortcut | Meaning | Example |
|----------|---------|---------|
| `~` | Home directory | `cd ~` |
| `.` | Current directory | `cp file.txt ./backup/` |
| `..` | Parent directory | `cd ..` |
| `-` | Previous directory | `cd -` |

---

## Navigation Examples

### Go to home directory
```bash
cd ~
# or just
cd
```

### Go up one level
```bash
cd ..
```

### Go up two levels
```bash
cd ../..
```

### Go to previous directory
```bash
cd -
```
Great for toggling between two directories!

### Go to absolute path
```bash
cd /var/log
```

---

## Path Separators

- **Unix** (Linux/macOS): Forward slash `/`
- **Windows**: Backslash `\`

PowerShell accepts both:
```powershell
cd C:/Users/name  # works
cd C:\Users\name  # also works
```

---

## Handling Spaces in Paths

Use quotes or escapes:

```bash
cd "My Documents"
cd My\ Documents
```

---

## Directory Stack

Push and pop directories like a browser history:

```bash
pushd /var/log    # save current, go to /var/log
pushd /etc        # save /var/log, go to /etc
popd              # back to /var/log
popd              # back to original
```

---

## Finding Executables

### Where is a command?

```bash
which python
# /usr/bin/python

type ls
# ls is aliased to 'ls --color=auto'
```

Windows:
```cmd
where python
```

### The PATH Variable

When you type a command, the shell searches directories in `PATH`:

```bash
echo $PATH
# /usr/local/bin:/usr/bin:/bin
```

Commands are found in these directories, in order.

---

## Common Directory Locations

| Location | Purpose |
|----------|---------|
| `/home/user` | Your files |
| `/etc` | System configuration |
| `/var/log` | Log files |
| `/tmp` | Temporary files |
| `/usr/bin` | User programs |
| `/opt` | Optional software |

Windows:
| Location | Purpose |
|----------|---------|
| `C:\Users\name` | Your files |
| `C:\Program Files` | Installed programs |
| `C:\Windows\System32` | System files |
| `%TEMP%` | Temporary files |

---

## Exercises

### Exercise 1: Basic Navigation
1. Open terminal
2. Run `pwd` to see where you are
3. `cd ~` to go home
4. `ls -la` to see all files
5. `cd /tmp` (or `cd %TEMP%` on Windows)
6. `cd -` to go back

### Exercise 2: Relative Paths
1. Go to home: `cd ~`
2. Create structure: `mkdir -p test/sub1/sub2`
3. Navigate: `cd test/sub1/sub2`
4. Go up: `cd ..` (now in sub1)
5. Go up twice: `cd ../..` (now in home)

### Exercise 3: Tab Completion
Navigate to the deepest directory you can find using only tab completion.

### Exercise 4: Find Commands
1. Find where `python` is: `which python`
2. Find where `git` is: `which git`
3. View your PATH: `echo $PATH`

---

## Key Takeaways

1. Use `pwd` to know where you are
2. Use `ls -la` to see everything in a directory
3. Absolute paths start from root; relative from current
4. `..` goes up, `~` goes home, `-` goes back
5. Tab completion prevents typos

---

## Next Module

In Module 3, you'll learn file operations - creating, copying, moving, and deleting files and directories.
