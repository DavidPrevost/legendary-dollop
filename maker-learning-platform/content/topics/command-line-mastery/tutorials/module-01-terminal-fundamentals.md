# Module 1: Terminal Fundamentals

**Concepts Covered**: 1-25
**Estimated Time**: 30-45 minutes

---

## What is a Terminal?

A **terminal** (also called console or command line) is a text-based interface for interacting with your computer. Instead of clicking buttons and icons, you type commands.

### Terminal vs Shell

- **Terminal**: The window/application where you type
- **Shell**: The program that interprets your commands

Common shells:
- **Bash**: Default on Linux and older macOS
- **Zsh**: Default on newer macOS
- **PowerShell**: Modern Windows shell
- **CMD**: Legacy Windows shell

---

## Opening Your Terminal

### Windows
- Press `Win + X`, select "Terminal" or "PowerShell"
- Or search for "Terminal" in Start menu
- Or press `Win + R`, type `cmd` or `powershell`

### macOS
- Press `Cmd + Space`, type "Terminal"
- Or find Terminal in Applications → Utilities

### Linux
- Press `Ctrl + Alt + T` (most distributions)
- Or search for "Terminal" in applications

---

## Terminal Anatomy

```
user@hostname:~/projects$ _
```

Breaking this down:
- `user`: Your username
- `hostname`: Computer name
- `~/projects`: Current directory
- `$`: Prompt (indicates ready for input)
- `_`: Cursor position

On Windows PowerShell:
```
PS C:\Users\username>
```

---

## Your First Commands

### Check Where You Are

```bash
pwd
```
**P**rint **W**orking **D**irectory - shows your current location.

PowerShell equivalent:
```powershell
Get-Location
# or simply
pwd
```

### Clear the Screen

```bash
clear
```

Windows:
```cmd
cls
```

### Exit the Terminal

```bash
exit
```

---

## Command History

Navigate previous commands:
- **Up Arrow**: Previous command
- **Down Arrow**: Next command
- **Ctrl + R**: Search history (Bash/Zsh)

This saves massive time - never retype long commands!

---

## Case Sensitivity

**Linux/macOS**: Case-sensitive
- `file.txt` and `File.txt` are different files

**Windows**: Case-insensitive
- `file.txt` and `File.txt` are the same

---

## Tab Completion

Type partial names and press **Tab** to autocomplete:

```bash
cd Doc[Tab]
# completes to: cd Documents/
```

Press Tab twice to see all matches:
```bash
cd D[Tab][Tab]
# shows: Desktop/ Documents/ Downloads/
```

---

## Terminal Customization

### Colors and Fonts

Most terminal applications allow customization:
- Color schemes (dark themes are popular)
- Font size and family (use monospace fonts)
- Transparency and padding

### Multiple Tabs/Windows

Open multiple terminals for different tasks:
- `Ctrl + Shift + T`: New tab (Linux terminals)
- `Cmd + T`: New tab (macOS Terminal)

---

## Common Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| `Ctrl + C` | Cancel current command |
| `Ctrl + L` | Clear screen |
| `Ctrl + A` | Move to line start |
| `Ctrl + E` | Move to line end |
| `Ctrl + U` | Clear line before cursor |
| `Ctrl + K` | Clear line after cursor |
| `Ctrl + W` | Delete word before cursor |
| `Tab` | Autocomplete |

---

## Why Use the Terminal?

### Advantages Over GUI
- **Speed**: Commands are faster than clicking
- **Automation**: Scripts can repeat tasks
- **Remote access**: Work on servers
- **Precision**: Exact control over operations
- **Ubiquity**: Available on all systems

### When to Use Terminal
- Batch operations (rename 100 files)
- Automation and scripting
- Development workflows (Git, npm, etc.)
- Server administration
- When GUI isn't available

---

## Copy and Paste

### Linux
- **Copy**: `Ctrl + Shift + C`
- **Paste**: `Ctrl + Shift + V`

### macOS
- **Copy**: `Cmd + C`
- **Paste**: `Cmd + V`

### Windows
- **Copy**: `Ctrl + C` (in new Terminal)
- **Paste**: `Ctrl + V` (in new Terminal)
- Or right-click to paste

---

## Exercises

### Exercise 1: Open and Explore
1. Open your terminal
2. Run `pwd` to see your location
3. Run `whoami` to see your username
4. Run `date` to see current date/time
5. Clear the screen

### Exercise 2: History Navigation
1. Run these commands:
   - `echo "first"`
   - `echo "second"`
   - `echo "third"`
2. Use up arrow to run "second" again
3. Use `Ctrl + R` and type "fir" to find "first"

### Exercise 3: Tab Completion
1. Type `cd /` and press Tab twice
2. Type `cd /u` and press Tab
3. Continue using Tab to navigate to a directory

---

## Key Takeaways

1. Terminal is a text interface; shell interprets commands
2. Use `pwd` to check your location
3. History and tab completion save time
4. Commands are case-sensitive on Unix systems
5. `Ctrl + C` cancels any stuck command

---

## Next Module

In Module 2, you'll learn to navigate the file system - moving between directories and understanding paths.
