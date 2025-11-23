# Module 4: Viewing and Reading Files

**Concepts Covered**: 96-125
**Estimated Time**: 30-40 minutes

---

## Displaying File Contents

### Show Entire File

```bash
cat file.txt
```

Short for "concatenate" - prints file to terminal.

### Concatenate Multiple Files

```bash
cat file1.txt file2.txt file3.txt
```

### With Line Numbers

```bash
cat -n file.txt
```

Windows:
```cmd
type file.txt
```

---

## Paging Through Files

For large files, use a pager:

### less (Recommended)

```bash
less largefile.txt
```

Navigation in less:
- **Space/PgDn**: Next page
- **b/PgUp**: Previous page
- **g**: Go to beginning
- **G**: Go to end
- **/pattern**: Search forward
- **?pattern**: Search backward
- **n**: Next search result
- **N**: Previous search result
- **q**: Quit

### more (Older)

```bash
more file.txt
```

Less featured than less!

---

## First and Last Lines

### First Lines

```bash
head file.txt          # first 10 lines
head -n 20 file.txt    # first 20 lines
head -n 5 file.txt     # first 5 lines
```

### Last Lines

```bash
tail file.txt          # last 10 lines
tail -n 20 file.txt    # last 20 lines
```

### Follow Updates (Live)

```bash
tail -f logfile.txt
```

Shows new lines as they're added - great for logs!

Press `Ctrl + C` to stop.

---

## Counting Content

### Word Count

```bash
wc file.txt
# 100  500  3000 file.txt
# lines words bytes
```

### Specific Counts

```bash
wc -l file.txt    # lines only
wc -w file.txt    # words only
wc -c file.txt    # bytes only
wc -m file.txt    # characters
```

### Count Multiple Files

```bash
wc -l *.txt
```

---

## Line Numbering

### Using nl

```bash
nl file.txt
```

More options than `cat -n`:
```bash
nl -b a file.txt    # number all lines including blank
```

---

## Comparing Files

### Basic Diff

```bash
diff file1.txt file2.txt
```

Output shows what changed:
- `<` lines from file1
- `>` lines from file2
- `2c2` means line 2 changed

### Side-by-Side

```bash
diff -y file1.txt file2.txt
```

### Unified Format (for patches)

```bash
diff -u file1.txt file2.txt
```

---

## File Type Information

### Determine File Type

```bash
file document.pdf
# document.pdf: PDF document, version 1.4

file mystery
# mystery: ASCII text
# mystery: ELF 64-bit executable
# mystery: PNG image data
```

### MIME Type

```bash
file --mime-type image.jpg
# image.jpg: image/jpeg
```

---

## File Encoding

Most modern files use UTF-8, but you may encounter others.

### Check Encoding

```bash
file -i file.txt
# file.txt: text/plain; charset=utf-8
```

### Convert Encoding

```bash
iconv -f ISO-8859-1 -t UTF-8 input.txt > output.txt
```

---

## Viewing Binary Files

### Hex Dump

```bash
xxd file.bin | head
hexdump -C file.bin | head
```

### Strings in Binary

```bash
strings executable | grep -i password
```

Extracts readable text from binary files.

---

## Reading Compressed Files

### View Without Extracting

```bash
zcat file.txt.gz
zless file.txt.gz
zgrep "pattern" file.txt.gz
```

---

## Opening with Default App

### Linux

```bash
xdg-open file.pdf
```

### macOS

```bash
open file.pdf
```

### Windows

```cmd
start file.pdf
```

---

## Practical Examples

### View Log File Efficiently

```bash
# Last 50 lines of log
tail -n 50 /var/log/syslog

# Follow log in real-time
tail -f /var/log/syslog

# View in pager with search
less /var/log/syslog
```

### Quick File Inspection

```bash
# What type of file?
file mystery_file

# How big?
ls -lh mystery_file

# First few lines?
head mystery_file

# Count lines?
wc -l mystery_file
```

### Compare Configurations

```bash
diff config.old config.new
# or side-by-side
diff -y config.old config.new | less
```

---

## Exercises

### Exercise 1: File Inspection
```bash
# Download or create a file
echo -e "Line 1\nLine 2\nLine 3\nLine 4\nLine 5" > test.txt

# View with line numbers
cat -n test.txt

# Count lines and words
wc test.txt
```

### Exercise 2: Using less
```bash
# Create larger file
seq 1 100 > numbers.txt

# Open in less
less numbers.txt

# Try: space, b, g, G, /50, q
```

### Exercise 3: Head and Tail
```bash
head -n 3 numbers.txt
tail -n 3 numbers.txt
head -n 20 numbers.txt | tail -n 5  # lines 16-20
```

### Exercise 4: Compare Files
```bash
echo "apple" > file1.txt
echo "orange" > file2.txt
diff file1.txt file2.txt
```

---

## Key Takeaways

1. Use `less` for large files - it's powerful
2. `head` and `tail` for quick peeks
3. `tail -f` for live log monitoring
4. `wc -l` to count lines quickly
5. `diff` to see what changed between files

---

## Next Module

In Module 5, you'll learn to search and find - using find for files and grep for content.
