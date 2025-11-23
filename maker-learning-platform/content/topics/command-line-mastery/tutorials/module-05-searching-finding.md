# Module 5: Searching and Finding

**Concepts Covered**: 126-165
**Estimated Time**: 50-60 minutes

---

## Finding Files: The find Command

### Basic Syntax

```bash
find [path] [conditions] [actions]
```

### Find by Name

```bash
find . -name "*.txt"           # in current dir
find /home -name "config.json" # in /home
find . -iname "readme*"        # case-insensitive
```

### Find by Type

```bash
find . -type f -name "*.py"    # files only
find . -type d -name "test*"   # directories only
find . -type l                  # symbolic links
```

### Find by Size

```bash
find . -size +100M    # larger than 100MB
find . -size -1k      # smaller than 1KB
find . -size 50M      # exactly 50MB
```

Size suffixes: c (bytes), k (KB), M (MB), G (GB)

### Find by Time

```bash
find . -mtime -7      # modified in last 7 days
find . -mtime +30     # modified more than 30 days ago
find . -mmin -60      # modified in last 60 minutes
```

### Combining Conditions

```bash
# AND (default)
find . -name "*.log" -size +1M

# OR
find . -name "*.jpg" -o -name "*.png"

# NOT
find . ! -name "*.tmp"
```

### Execute Commands on Results

```bash
# Delete old temp files
find /tmp -name "*.tmp" -mtime +7 -delete

# Run command on each file
find . -name "*.txt" -exec wc -l {} \;

# More efficient with +
find . -name "*.py" -exec chmod 644 {} +
```

### Exclude Directories

```bash
find . -name "*.js" -not -path "./node_modules/*"
```

---

## Searching Text: grep

### Basic Search

```bash
grep "error" logfile.txt
```

### Common Options

```bash
grep -i "error" file.txt    # case-insensitive
grep -n "error" file.txt    # show line numbers
grep -c "error" file.txt    # count matches
grep -l "error" *.txt       # list files with matches
grep -L "error" *.txt       # list files without matches
```

### Recursive Search

```bash
grep -r "TODO" .            # search all files
grep -r "TODO" --include="*.py" .  # only Python files
```

### Context Lines

```bash
grep -B 2 "error" file.txt  # 2 lines before
grep -A 2 "error" file.txt  # 2 lines after
grep -C 2 "error" file.txt  # 2 lines both sides
```

### Invert Match

```bash
grep -v "debug" logfile.txt  # lines NOT containing "debug"
```

---

## Regular Expressions

Grep uses regex for pattern matching.

### Basic Patterns

```bash
grep "^Start" file.txt      # lines starting with "Start"
grep "end$" file.txt        # lines ending with "end"
grep "^$" file.txt          # empty lines
grep "..." file.txt         # lines with at least 3 chars
```

### Character Classes

```bash
grep "[0-9]" file.txt       # contains digit
grep "[a-zA-Z]" file.txt    # contains letter
grep "[^0-9]" file.txt      # contains non-digit
```

### Quantifiers

```bash
grep "go*d" file.txt        # god, good, goood...
grep "go\+d" file.txt       # good, goood... (1+ o's)
grep "colou\?r" file.txt    # color or colour
```

### Extended Regex

Use `-E` for extended syntax:

```bash
grep -E "cat|dog" file.txt         # cat or dog
grep -E "[0-9]{3}" file.txt        # 3 digits
grep -E "^[A-Z][a-z]+" file.txt    # capitalized words
```

### Common Patterns

```bash
# Email-like
grep -E "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+" file.txt

# IP address-like
grep -E "[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}" file.txt

# URL
grep -E "https?://[^ ]+" file.txt
```

---

## Modern Alternatives

### ripgrep (rg)

Faster and smarter than grep:

```bash
rg "TODO"                    # recursive by default
rg "error" -i                # case-insensitive
rg "pattern" -t py           # only Python files
rg "pattern" --hidden        # include hidden files
```

### The Silver Searcher (ag)

```bash
ag "TODO"
ag "pattern" --python
```

### fzf (Fuzzy Finder)

Interactive fuzzy search:

```bash
# Find and open file
vim $(fzf)

# Search command history
history | fzf
```

---

## Locate Command

Pre-indexed fast search:

```bash
locate filename
```

Update database:
```bash
sudo updatedb
```

---

## Searching Command Output

Pipe to grep:

```bash
ps aux | grep python
history | grep "git commit"
ls -la | grep "^d"           # only directories
```

---

## Practical Examples

### Find Large Files

```bash
find /home -type f -size +100M -exec ls -lh {} \;
```

### Find and Delete Old Logs

```bash
find /var/log -name "*.log" -mtime +30 -delete
```

### Search for Configuration

```bash
grep -r "database_url" /etc/
```

### Find Files Modified Today

```bash
find . -mtime 0 -type f
```

### Count TODO Comments

```bash
grep -r "TODO" --include="*.py" . | wc -l
```

### Find Empty Files

```bash
find . -type f -empty
```

---

## Exercises

### Exercise 1: Find Practice
```bash
# Create test structure
mkdir -p test/{a,b,c}
touch test/a/file1.txt test/b/file2.log test/c/file3.txt

# Find all .txt files
find test -name "*.txt"

# Find files larger than 0 bytes (none here)
find test -size +0
```

### Exercise 2: Grep Practice
```bash
# Create test file
cat > test.txt << 'EOF'
INFO: Started server
ERROR: Connection failed
DEBUG: Attempting reconnect
ERROR: Timeout exceeded
INFO: Server stopped
EOF

# Find errors
grep "ERROR" test.txt

# Count errors
grep -c "ERROR" test.txt

# Show context
grep -C 1 "ERROR" test.txt
```

### Exercise 3: Regex Practice
```bash
# Find lines starting with INFO
grep "^INFO" test.txt

# Find lines with numbers
grep "[0-9]" test.txt
```

### Exercise 4: Combined Search
```bash
# Find Python files containing "import"
find . -name "*.py" -exec grep -l "import" {} \;
```

---

## Key Takeaways

1. `find` for locating files by name, size, date
2. `grep` for searching text within files
3. Combine with `-exec` to act on results
4. Learn basic regex: `^`, `$`, `[]`, `*`, `+`
5. Use `grep -r` for recursive search

---

## Next Module

In Module 6, you'll learn text processing - transforming data with sort, cut, sed, and awk.
