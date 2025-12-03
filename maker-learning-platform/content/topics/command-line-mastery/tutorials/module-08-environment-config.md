# Module 8: Environment and Configuration

**Concepts Covered**: 236-265
**Estimated Time**: 40-50 minutes

---

## Environment Variables

Variables that configure your shell and programs.

### View All Variables

```bash
env        # or
printenv
```

### View Specific Variable

```bash
echo $HOME
echo $USER
echo $PATH
```

PowerShell:
```powershell
echo $env:HOME
Get-ChildItem env:
```

---

## Setting Variables

### Temporary (Current Session)

```bash
MY_VAR="hello"
echo $MY_VAR
```

### Export for Child Processes

```bash
export MY_VAR="hello"
```

Without export, variable isn't available to commands you run.

### Unset Variable

```bash
unset MY_VAR
```

---

## Common Environment Variables

| Variable | Description |
|----------|-------------|
| `HOME` | Your home directory |
| `USER` | Your username |
| `PATH` | Directories to search for commands |
| `PWD` | Current directory |
| `SHELL` | Your default shell |
| `EDITOR` | Default text editor |
| `LANG` | Language/locale setting |
| `TERM` | Terminal type |

---

## The PATH Variable

### Understanding PATH

When you type a command, shell searches directories in PATH:

```bash
echo $PATH
# /usr/local/bin:/usr/bin:/bin:/home/user/bin
```

Searched left to right, first match wins.

### Add to PATH

```bash
# Add to beginning (searched first)
export PATH="$HOME/bin:$PATH"

# Add to end
export PATH="$PATH:$HOME/scripts"
```

### Find Command Location

```bash
which python
# /usr/bin/python

type ls
# ls is aliased to 'ls --color=auto'
```

---

## Shell Configuration Files

### Bash

- `~/.bashrc`: Interactive non-login shells
- `~/.bash_profile`: Login shells
- `~/.profile`: Generic profile

Common approach: Put everything in `.bashrc`, source from `.bash_profile`:

```bash
# ~/.bash_profile
if [ -f ~/.bashrc ]; then
    source ~/.bashrc
fi
```

### Zsh

- `~/.zshrc`: Main configuration file
- `~/.zprofile`: Login shells

### PowerShell

```powershell
$PROFILE    # shows profile path
notepad $PROFILE    # edit it
```

---

## Creating Aliases

Shortcuts for commands:

### Temporary Alias

```bash
alias ll='ls -la'
alias gs='git status'
```

### Permanent Aliases

Add to `~/.bashrc` or `~/.zshrc`:

```bash
# Navigation
alias ..='cd ..'
alias ...='cd ../..'
alias ~='cd ~'

# Listing
alias ll='ls -alh'
alias la='ls -A'
alias l='ls -CF'

# Safety
alias rm='rm -i'
alias cp='cp -i'
alias mv='mv -i'

# Git shortcuts
alias gs='git status'
alias ga='git add'
alias gc='git commit'
alias gp='git push'

# Utility
alias c='clear'
alias h='history'
alias grep='grep --color=auto'
```

### View Defined Aliases

```bash
alias
```

### Remove Alias

```bash
unalias ll
```

---

## Shell Functions

More powerful than aliases:

```bash
# Function definition
mkcd() {
    mkdir -p "$1" && cd "$1"
}

# Use it
mkcd new-project
```

### Functions in Config

Add to `~/.bashrc`:

```bash
# Create and enter directory
mkcd() {
    mkdir -p "$1" && cd "$1"
}

# Extract various archives
extract() {
    case "$1" in
        *.tar.gz)  tar xzf "$1" ;;
        *.tar.bz2) tar xjf "$1" ;;
        *.zip)     unzip "$1" ;;
        *.gz)      gunzip "$1" ;;
        *)         echo "Unknown format: $1" ;;
    esac
}

# Quick calculator
calc() {
    echo "scale=2; $*" | bc
}
```

---

## Shell Options

### View Options

```bash
set -o    # list all options
```

### Useful Options

```bash
set -o vi        # vi-style editing
set -o emacs     # emacs-style editing (default)
```

### In Scripts

```bash
set -e    # exit on error
set -u    # error on undefined variable
set -x    # print commands as executed
```

---

## Login vs Non-Login Shells

- **Login shell**: When you log in (ssh, console)
- **Non-login shell**: Terminal in GUI, subshell

Check which:
```bash
echo $0
# -bash (login) or bash (non-login)

shopt login_shell
# on/off
```

---

## Applying Changes

After editing config files:

```bash
source ~/.bashrc
# or
. ~/.bashrc
```

Or open a new terminal.

---

## Practical Configuration

### Example .bashrc

```bash
# ~/.bashrc

# History settings
HISTSIZE=10000
HISTFILESIZE=20000
HISTCONTROL=ignoreboth

# Append to history instead of overwriting
shopt -s histappend

# Check window size after each command
shopt -s checkwinsize

# Aliases
alias ll='ls -alh'
alias la='ls -A'
alias ..='cd ..'
alias grep='grep --color=auto'
alias c='clear'

# Git aliases
alias gs='git status'
alias ga='git add'
alias gc='git commit -m'
alias gp='git push'
alias gl='git log --oneline'

# Functions
mkcd() { mkdir -p "$1" && cd "$1"; }

# Custom prompt
PS1='\[\e[32m\]\u@\h\[\e[0m\]:\[\e[34m\]\w\[\e[0m\]\$ '

# Path additions
export PATH="$HOME/bin:$PATH"

# Default editor
export EDITOR=vim
```

---

## Debugging Configuration

### Check Syntax

```bash
bash -n ~/.bashrc
```

### Trace Execution

```bash
bash -x ~/.bashrc
```

### Common Issues

1. **Typos in aliases**: Double-check syntax
2. **Missing export**: Variables not available in subshells
3. **Wrong file**: Using .bash_profile vs .bashrc
4. **Overwritten PATH**: Always append with `$PATH`

---

## Exercises

### Exercise 1: Environment Variables
```bash
# View current user
echo $USER
echo $HOME

# Create and export variable
export MY_PROJECT="/home/$USER/projects"
echo $MY_PROJECT
```

### Exercise 2: PATH Modification
```bash
# View current PATH
echo $PATH

# Create bin directory
mkdir -p ~/bin

# Add to PATH
export PATH="$HOME/bin:$PATH"

# Verify
echo $PATH
```

### Exercise 3: Create Aliases
```bash
# Temporary aliases
alias ll='ls -la'
alias c='clear'

# Test them
ll
c
```

### Exercise 4: Shell Function
```bash
# Define function
greet() {
    echo "Hello, $1!"
}

# Use it
greet World
greet "$(whoami)"
```

---

## Key Takeaways

1. Environment variables configure your shell
2. Add to PATH to run your scripts from anywhere
3. Use `.bashrc` for your customizations
4. Aliases save typing for common commands
5. Functions handle complex shortcuts
6. `source ~/.bashrc` applies changes immediately

---

## Next Module

In Module 9, you'll learn process management - viewing, controlling, and monitoring running processes.
