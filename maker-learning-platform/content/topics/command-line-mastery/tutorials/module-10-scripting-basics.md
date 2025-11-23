# Module 10: Scripting Basics

**Concepts Covered**: 296-330
**Estimated Time**: 50-60 minutes

---

## What is a Shell Script?

A text file containing shell commands that run in sequence. Automate repetitive tasks!

---

## Creating Your First Script

### 1. Create File

```bash
touch myscript.sh
```

### 2. Add Shebang

First line specifies interpreter:

```bash
#!/bin/bash
```

Other options:
```bash
#!/bin/sh       # POSIX shell
#!/usr/bin/env bash  # Find bash in PATH
```

### 3. Add Commands

```bash
#!/bin/bash
echo "Hello, World!"
date
```

### 4. Make Executable

```bash
chmod +x myscript.sh
```

### 5. Run It

```bash
./myscript.sh
```

---

## Script Arguments

Access arguments with `$1`, `$2`, etc.

```bash
#!/bin/bash
echo "Script name: $0"
echo "First argument: $1"
echo "Second argument: $2"
echo "All arguments: $@"
echo "Number of arguments: $#"
```

Run:
```bash
./script.sh hello world
# Script name: ./script.sh
# First argument: hello
# Second argument: world
# All arguments: hello world
# Number of arguments: 2
```

### Special Variables

| Variable | Meaning |
|----------|---------|
| `$0` | Script name |
| `$1-$9` | Positional arguments |
| `$@` | All arguments as separate words |
| `$*` | All arguments as single word |
| `$#` | Number of arguments |
| `$?` | Exit status of last command |
| `$$` | Current process ID |

---

## Exit Status

Every command returns an exit code:
- **0**: Success
- **Non-zero**: Failure

### Check Status

```bash
command
echo $?
```

### Set Exit Status

```bash
#!/bin/bash
if [ some_condition ]; then
    exit 0    # success
else
    exit 1    # failure
fi
```

---

## Conditional Execution

### && and ||

```bash
command1 && command2    # run if command1 succeeds
command1 || command2    # run if command1 fails
```

---

## If Statements

### Basic Syntax

```bash
if [ condition ]; then
    commands
fi
```

### With Else

```bash
if [ condition ]; then
    commands
else
    other_commands
fi
```

### With Elif

```bash
if [ condition1 ]; then
    commands1
elif [ condition2 ]; then
    commands2
else
    commands3
fi
```

---

## Test Conditions

### File Tests

```bash
[ -f file ]    # file exists and is regular file
[ -d dir ]     # directory exists
[ -e path ]    # path exists
[ -r file ]    # file is readable
[ -w file ]    # file is writable
[ -x file ]    # file is executable
[ -s file ]    # file is not empty
```

### String Tests

```bash
[ -z "$str" ]       # string is empty
[ -n "$str" ]       # string is not empty
[ "$a" = "$b" ]     # strings equal
[ "$a" != "$b" ]    # strings not equal
```

### Numeric Tests

```bash
[ "$a" -eq "$b" ]   # equal
[ "$a" -ne "$b" ]   # not equal
[ "$a" -lt "$b" ]   # less than
[ "$a" -le "$b" ]   # less than or equal
[ "$a" -gt "$b" ]   # greater than
[ "$a" -ge "$b" ]   # greater than or equal
```

### Example

```bash
#!/bin/bash
if [ -f "$1" ]; then
    echo "File exists"
else
    echo "File not found"
fi
```

---

## Case Statements

For multiple conditions:

```bash
#!/bin/bash
case "$1" in
    start)
        echo "Starting..."
        ;;
    stop)
        echo "Stopping..."
        ;;
    restart)
        echo "Restarting..."
        ;;
    *)
        echo "Usage: $0 {start|stop|restart}"
        exit 1
        ;;
esac
```

---

## Loops

### For Loop

```bash
for item in list; do
    commands
done
```

Examples:

```bash
# Iterate over words
for fruit in apple banana orange; do
    echo "$fruit"
done

# Iterate over files
for file in *.txt; do
    echo "Processing $file"
done

# C-style for loop
for ((i=1; i<=5; i++)); do
    echo "$i"
done
```

### While Loop

```bash
while [ condition ]; do
    commands
done
```

Example:

```bash
count=1
while [ $count -le 5 ]; do
    echo "Count: $count"
    ((count++))
done
```

### Until Loop

```bash
until [ condition ]; do
    commands
done
```

Runs until condition becomes true.

### Loop Control

```bash
break      # exit loop
continue   # skip to next iteration
```

---

## Reading Input

### From User

```bash
read -p "Enter name: " name
echo "Hello, $name"
```

### From File

```bash
while read line; do
    echo "$line"
done < file.txt
```

---

## Script Functions

```bash
function_name() {
    commands
}
```

Example:

```bash
#!/bin/bash

greet() {
    echo "Hello, $1!"
}

add() {
    echo $(($1 + $2))
}

greet "World"
result=$(add 5 3)
echo "5 + 3 = $result"
```

---

## Error Handling

### Exit on Error

```bash
set -e
```

Script stops if any command fails.

### Check Commands

```bash
if ! command; then
    echo "Command failed"
    exit 1
fi
```

### Trap Errors

```bash
trap 'echo "Error on line $LINENO"' ERR
```

---

## Debugging

### Print Commands

```bash
set -x    # print each command
set +x    # stop printing
```

### Debug Mode

```bash
bash -x script.sh
```

---

## Strict Mode

Best practice for scripts:

```bash
#!/bin/bash
set -euo pipefail
```

- `-e`: Exit on error
- `-u`: Error on undefined variable
- `-o pipefail`: Pipeline fails if any command fails

---

## Comments

```bash
# This is a comment

# Multi-line comments
: '
This is a
multi-line comment
'
```

---

## Practical Script Example

```bash
#!/bin/bash
set -euo pipefail

# Backup script

# Configuration
SOURCE_DIR="${1:?Usage: $0 source_dir}"
BACKUP_DIR="/backup"
DATE=$(date +%Y%m%d_%H%M%S)
BACKUP_NAME="backup_$DATE.tar.gz"

# Functions
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# Main
log "Starting backup of $SOURCE_DIR"

if [ ! -d "$SOURCE_DIR" ]; then
    log "Error: Source directory not found"
    exit 1
fi

mkdir -p "$BACKUP_DIR"
tar czf "$BACKUP_DIR/$BACKUP_NAME" "$SOURCE_DIR"

log "Backup complete: $BACKUP_NAME"
```

---

## Exercises

### Exercise 1: Basic Script
```bash
#!/bin/bash
echo "Hello, $USER!"
echo "Today is $(date)"
echo "You are in $(pwd)"
```

### Exercise 2: Script with Arguments
```bash
#!/bin/bash
if [ $# -eq 0 ]; then
    echo "Usage: $0 name"
    exit 1
fi
echo "Hello, $1!"
```

### Exercise 3: File Check
```bash
#!/bin/bash
for file in "$@"; do
    if [ -f "$file" ]; then
        echo "$file: $(wc -l < "$file") lines"
    else
        echo "$file: not found"
    fi
done
```

### Exercise 4: Loop Practice
```bash
#!/bin/bash
for i in {1..5}; do
    echo "Number: $i"
done
```

---

## Key Takeaways

1. Start with `#!/bin/bash` and `chmod +x`
2. Use `$1`, `$2` for arguments, `$#` for count
3. `[ condition ]` for tests in if statements
4. `for`/`while` loops for iteration
5. `set -euo pipefail` for robust scripts
6. Functions keep code organized

---

## Next Module

In Module 11, you'll learn networking commands - curl, ssh, and connecting to remote systems.
