# Module 12: Advanced Topics

**Concepts Covered**: 361-380
**Estimated Time**: 35-45 minutes

---

## Command Substitution

Capture command output for use in other commands.

### Syntax

```bash
$(command)    # modern syntax
`command`     # older syntax (avoid)
```

### Examples

```bash
# Store in variable
current_date=$(date +%Y-%m-%d)
echo "Today is $current_date"

# Use in command
echo "Files: $(ls | wc -l)"

# In filename
tar czf backup_$(date +%Y%m%d).tar.gz folder/
```

---

## Arithmetic Expansion

Calculate numbers in bash.

### Syntax

```bash
$((expression))
```

### Examples

```bash
echo $((5 + 3))        # 8
echo $((10 / 3))       # 3 (integer division)
echo $((2 ** 8))       # 256 (exponent)

# In variables
a=5
b=3
echo $((a + b))        # 8
echo $((a * b))        # 15

# Increment
((count++))
((count += 5))
```

---

## Brace Expansion

Generate sequences and combinations.

### Lists

```bash
echo {a,b,c}           # a b c
echo file.{txt,md,py}  # file.txt file.md file.py
mkdir {src,test,docs}  # create 3 directories
```

### Sequences

```bash
echo {1..5}            # 1 2 3 4 5
echo {a..e}            # a b c d e
echo {01..10}          # 01 02 ... 10 (zero-padded)
echo {0..20..5}        # 0 5 10 15 20 (step)
```

### Combinations

```bash
echo {a,b}{1,2}        # a1 a2 b1 b2
mkdir project/{src,test}/{main,utils}
```

### Practical Uses

```bash
# Create multiple files
touch file{1..10}.txt

# Backup with timestamp
cp config.json{,.bak}    # copies to config.json.bak

# Create directory structure
mkdir -p project/{src,test,docs}/{main,utils}
```

---

## Globbing Patterns

Pattern matching for filenames.

### Basic Patterns

```bash
*           # any characters
?           # single character
[abc]       # a, b, or c
[a-z]       # range
[!abc]      # not a, b, or c
```

### Extended Globbing

Enable with:
```bash
shopt -s extglob
```

Patterns:
```bash
?(pattern)    # zero or one
*(pattern)    # zero or more
+(pattern)    # one or more
@(pattern)    # exactly one
!(pattern)    # not matching
```

Examples:
```bash
ls !(*.txt)              # not .txt files
ls *(src|lib)/*.js       # .js in src or lib
```

---

## Quoting Rules

### No Quotes
Variables expand, globbing happens:
```bash
echo $HOME *.txt
```

### Double Quotes
Variables expand, no globbing:
```bash
echo "$HOME *.txt"    # /home/user *.txt
```

### Single Quotes
Nothing expands (literal):
```bash
echo '$HOME *.txt'    # $HOME *.txt
```

### When to Use

- **Double**: Most cases (preserves spaces in variables)
- **Single**: When you want literal text
- **None**: Rarely (be careful with spaces)

```bash
filename="my file.txt"
cat "$filename"        # correct
cat $filename          # error: two arguments
```

---

## Escape Characters

### Backslash

```bash
echo "Price: \$100"    # Price: $100
echo "Tab:\tNewline:\n"
```

### $'...' Syntax

For escape sequences:
```bash
echo $'Line 1\nLine 2'
echo $'Column1\tColumn2'
```

---

## ANSI Escape Codes

Control terminal appearance.

### Colors

```bash
echo -e "\e[31mRed text\e[0m"
echo -e "\e[32mGreen text\e[0m"
echo -e "\e[1mBold text\e[0m"
```

### Common Codes

| Code | Effect |
|------|--------|
| `\e[0m` | Reset |
| `\e[1m` | Bold |
| `\e[31m` | Red |
| `\e[32m` | Green |
| `\e[33m` | Yellow |
| `\e[34m` | Blue |

### In Scripts

```bash
RED='\e[31m'
GREEN='\e[32m'
NC='\e[0m'

echo -e "${GREEN}Success${NC}"
echo -e "${RED}Error${NC}"
```

---

## Custom Prompt (PS1)

### Basic Customization

```bash
PS1='\u@\h:\w\$ '
```

### Special Characters

| Code | Meaning |
|------|---------|
| `\u` | Username |
| `\h` | Hostname |
| `\w` | Full working directory |
| `\W` | Current directory name |
| `\d` | Date |
| `\t` | Time (24h) |
| `\$` | $ or # (root) |

### With Colors

```bash
PS1='\[\e[32m\]\u@\h\[\e[0m\]:\[\e[34m\]\w\[\e[0m\]\$ '
```

The `\[` and `\]` prevent length counting issues.

---

## History Expansion

### Quick Repeats

```bash
!!          # last command
!$          # last argument of last command
!*          # all arguments of last command
!-2         # two commands ago
```

### Examples

```bash
sudo !!              # rerun last as sudo
ls /some/long/path
cd !$                # cd to that path

vim file1.txt file2.txt
git add !*           # git add file1.txt file2.txt
```

### Search History

```bash
!grep       # last command starting with grep
!?pattern   # last command containing pattern
```

---

## Readline Shortcuts

Efficient command line editing.

### Movement

| Shortcut | Action |
|----------|--------|
| `Ctrl+A` | Beginning of line |
| `Ctrl+E` | End of line |
| `Ctrl+B` | Back one character |
| `Ctrl+F` | Forward one character |
| `Alt+B` | Back one word |
| `Alt+F` | Forward one word |

### Editing

| Shortcut | Action |
|----------|--------|
| `Ctrl+K` | Kill to end of line |
| `Ctrl+U` | Kill to beginning |
| `Ctrl+W` | Kill word before |
| `Ctrl+Y` | Yank (paste) killed text |
| `Ctrl+T` | Transpose characters |
| `Alt+T` | Transpose words |

### History

| Shortcut | Action |
|----------|--------|
| `Ctrl+R` | Reverse search |
| `Ctrl+P` | Previous command |
| `Ctrl+N` | Next command |

---

## Terminal Multiplexers Deep Dive

### tmux Basics

```bash
tmux                    # start session
tmux new -s name        # named session
tmux ls                 # list sessions
tmux attach -t name     # attach to session
```

### Key Bindings (prefix: Ctrl+B)

- `c`: New window
- `n/p`: Next/previous window
- `%`: Split vertical
- `"`: Split horizontal
- `o`: Switch pane
- `d`: Detach
- `x`: Kill pane

### Useful Configuration (~/.tmux.conf)

```bash
# Change prefix to Ctrl+A
set -g prefix C-a
unbind C-b

# Mouse support
set -g mouse on

# Easier splits
bind | split-window -h
bind - split-window -v
```

---

## Command Line Philosophy

### Unix Philosophy

1. Do one thing well
2. Write programs to work together
3. Text streams are universal interface

### Practical Application

- Combine small tools with pipes
- Use text formats (JSON, CSV)
- Automate everything repeatable
- Script your setup

---

## Exercises

### Exercise 1: Expansions
```bash
# Brace expansion
echo {1..5}
mkdir dir{1,2,3}
ls dir*

# Arithmetic
echo $((100 / 7))
count=5
echo $((count * 2))
```

### Exercise 2: Command Substitution
```bash
# Current date in filename
echo "backup_$(date +%Y%m%d).tar.gz"

# Count files
echo "There are $(ls | wc -l) files here"
```

### Exercise 3: Quoting
```bash
var="hello world"
echo $var        # two words
echo "$var"      # one word with space

echo '$var'      # literal
echo "$var"      # expanded
```

### Exercise 4: Custom Prompt
```bash
# Simple custom prompt
PS1='[\t] \u:\W\$ '

# With color
PS1='\[\e[34m\]\W\[\e[0m\]\$ '
```

---

## Key Takeaways

1. `$()` captures command output
2. `$(())` does arithmetic
3. `{}` generates sequences and combinations
4. Always quote variables: `"$var"`
5. Customize prompt with PS1
6. `!!` and `!$` save typing

---

## Congratulations!

You've completed Command Line Mastery! You now have skills to:

- Navigate and manage files efficiently
- Search and process text data
- Build powerful command pipelines
- Automate tasks with scripts
- Connect to remote systems

Keep practicing and soon these commands will be second nature.
