# Module 7: Pipes and Redirection

**Concepts Covered**: 206-235
**Estimated Time**: 45-55 minutes

---

## Standard Streams

Every program has three standard streams:

1. **stdin** (0): Standard input
2. **stdout** (1): Standard output
3. **stderr** (2): Standard error

```
         ┌─────────┐
stdin →  │ Program │ → stdout
         └────┬────┘
              ↓
           stderr
```

---

## Output Redirection

### Write to File

```bash
echo "Hello" > output.txt
```

Creates file or overwrites existing.

### Append to File

```bash
echo "More text" >> output.txt
```

Adds to end of file.

### Redirect Command Output

```bash
ls -la > listing.txt
date > timestamp.txt
```

---

## Input Redirection

### Read from File

```bash
sort < unsorted.txt
wc -l < file.txt
```

### Here Documents

Inline multi-line input:

```bash
cat << EOF
Line 1
Line 2
Line 3
EOF
```

### Here Strings

Single-line input:

```bash
grep "pattern" <<< "search in this string"
```

---

## Error Redirection

### Redirect stderr

```bash
command 2> errors.txt
```

### Redirect Both stdout and stderr

```bash
command > output.txt 2>&1
# or (bash shorthand)
command &> output.txt
```

### Separate Files

```bash
command > output.txt 2> errors.txt
```

### Discard Output

```bash
command > /dev/null           # discard stdout
command 2> /dev/null          # discard stderr
command &> /dev/null          # discard both
```

---

## Pipes

Connect output of one command to input of another:

```bash
command1 | command2
```

### Basic Examples

```bash
ls | wc -l                    # count files
cat file.txt | grep "error"   # filter lines
history | grep "git"          # find commands
```

### Chaining Multiple

```bash
cat log.txt | grep "ERROR" | sort | uniq -c | sort -rn
```

This:
1. Reads log file
2. Filters for ERROR lines
3. Sorts them
4. Counts unique ones
5. Sorts by count

---

## Tee Command

Split output to file AND stdout:

```bash
command | tee output.txt
```

Now output goes both to screen and file.

### Append with Tee

```bash
command | tee -a output.txt
```

### Multiple Files

```bash
command | tee file1.txt file2.txt
```

---

## xargs

Build command lines from input:

```bash
find . -name "*.txt" | xargs wc -l
```

### With Placeholder

```bash
find . -name "*.log" | xargs -I {} mv {} {}.bak
```

### Parallel Execution

```bash
find . -name "*.jpg" | xargs -P 4 -I {} convert {} -resize 50% {}
```

Runs 4 processes in parallel.

### Handle Special Characters

```bash
find . -name "*.txt" -print0 | xargs -0 wc -l
```

Uses null separator for files with spaces.

---

## Pipeline Patterns

### Count and Sort

```bash
cut -d ',' -f 1 data.csv | sort | uniq -c | sort -rn | head -10
```

### Filter, Transform, Save

```bash
cat input.txt | grep "pattern" | sed 's/old/new/g' | tee output.txt
```

### Process and Summarize

```bash
ps aux | awk '{sum += $4} END {print "Total Memory:", sum "%"}'
```

---

## Process Substitution

Use command output as a file:

```bash
diff <(sort file1.txt) <(sort file2.txt)
```

Compares sorted versions without modifying files.

---

## Exit Status

Commands return exit codes:
- **0**: Success
- **Non-zero**: Failure

### Check Status

```bash
command
echo $?    # print exit status
```

### Pipeline Status

In bash, `$PIPESTATUS` array holds all exit codes:

```bash
false | true
echo ${PIPESTATUS[@]}    # 1 0
```

---

## Command Chaining

### Run if Previous Succeeded (&&)

```bash
mkdir new_dir && cd new_dir
```

### Run if Previous Failed (||)

```bash
cd directory || echo "Directory not found"
```

### Run Regardless (;)

```bash
command1; command2; command3
```

### Combined

```bash
make && make install || echo "Build failed"
```

---

## Subshells

Group commands in parentheses:

```bash
(cd /tmp && ls) | wc -l
```

Current directory unchanged after.

---

## Practical Examples

### Find Largest Files

```bash
du -ah . | sort -rh | head -20
```

### Monitor Log for Errors

```bash
tail -f /var/log/syslog | grep --line-buffered "error"
```

### Backup with Progress

```bash
tar cf - directory/ | pv | gzip > backup.tar.gz
```

### Process CSV

```bash
cat data.csv | tail -n +2 | cut -d ',' -f 2 | sort | uniq -c
```

Skip header, extract field 2, count unique values.

### Clean Build

```bash
make clean && make all 2>&1 | tee build.log
```

---

## Debugging Pipelines

### See Intermediate Results

```bash
command1 | tee /dev/stderr | command2
```

Shows intermediate output on screen.

### Test Each Stage

```bash
# Stage 1
cat file.txt

# Add stage 2
cat file.txt | grep "pattern"

# Add stage 3
cat file.txt | grep "pattern" | sort
```

---

## Exercises

### Exercise 1: Basic Redirection
```bash
# Write date to file
date > today.txt
cat today.txt

# Append another line
echo "Log entry" >> today.txt
cat today.txt
```

### Exercise 2: Pipes
```bash
# Count words in a file
cat /etc/passwd | wc -l

# Find most common shell
cut -d ':' -f 7 /etc/passwd | sort | uniq -c | sort -rn
```

### Exercise 3: Error Handling
```bash
# Redirect errors
ls nonexistent 2> errors.txt
cat errors.txt

# Discard errors
ls nonexistent 2> /dev/null
```

### Exercise 4: Tee and xargs
```bash
# Pipeline with tee
echo "test" | tee file.txt | wc -c

# xargs example
echo "file1 file2 file3" | xargs touch
ls file*
```

---

## Key Takeaways

1. `>` writes, `>>` appends
2. `2>` redirects errors
3. `|` pipes output to next command
4. `&&` runs next if success, `||` if failure
5. `tee` splits output to file and stdout
6. `xargs` builds commands from input

---

## Next Module

In Module 8, you'll configure your shell environment - variables, aliases, and configuration files.
