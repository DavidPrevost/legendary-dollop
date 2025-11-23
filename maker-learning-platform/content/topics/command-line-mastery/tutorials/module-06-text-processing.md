# Module 6: Text Processing

**Concepts Covered**: 166-205
**Estimated Time**: 50-60 minutes

---

## Sorting Data

### Basic Sort

```bash
sort file.txt
```

Sorts lines alphabetically.

### Numeric Sort

```bash
sort -n numbers.txt
```

### Reverse Sort

```bash
sort -r file.txt
sort -rn numbers.txt  # reverse numeric
```

### Sort by Column

```bash
sort -k 2 data.txt       # by 2nd field
sort -k 2n data.txt      # numeric 2nd field
sort -k 2,2 -k 1,1 data.txt  # by 2nd, then 1st
```

### Sort with Custom Delimiter

```bash
sort -t ',' -k 2 data.csv    # comma-delimited
sort -t ':' -k 3n /etc/passwd  # colon-delimited
```

### Unique Sort

```bash
sort -u file.txt    # sort and remove duplicates
```

---

## Removing Duplicates

### Basic Uniq

```bash
uniq file.txt    # removes consecutive duplicates
```

**Important**: uniq only removes *consecutive* duplicates. Sort first!

```bash
sort file.txt | uniq
```

### Count Duplicates

```bash
sort file.txt | uniq -c
```

Output:
```
      3 apple
      1 banana
      2 orange
```

### Show Only Duplicates

```bash
sort file.txt | uniq -d
```

### Show Only Unique Lines

```bash
sort file.txt | uniq -u
```

---

## Extracting Columns

### Cut by Delimiter

```bash
cut -d ',' -f 1 data.csv     # first field
cut -d ',' -f 1,3 data.csv   # fields 1 and 3
cut -d ',' -f 2-4 data.csv   # fields 2 through 4
```

### Cut by Character Position

```bash
cut -c 1-10 file.txt    # characters 1-10
cut -c 5- file.txt      # character 5 to end
```

### Example: Extract Usernames

```bash
cut -d ':' -f 1 /etc/passwd
```

---

## Joining and Pasting

### Paste Columns

```bash
paste file1.txt file2.txt
```

Joins files side by side with tabs.

```bash
paste -d ',' file1.txt file2.txt   # comma delimiter
```

### Join on Common Field

```bash
join file1.txt file2.txt
```

Files must be sorted on join field.

---

## Character Translation

### Translate Characters

```bash
tr 'a-z' 'A-Z' < file.txt    # lowercase to uppercase
tr 'A-Z' 'a-z' < file.txt    # uppercase to lowercase
tr ' ' '_' < file.txt         # spaces to underscores
```

### Delete Characters

```bash
tr -d '0-9' < file.txt       # remove all digits
tr -d '\r' < file.txt        # remove carriage returns
```

### Squeeze Repeats

```bash
tr -s ' ' < file.txt         # multiple spaces to single
tr -s '\n' < file.txt        # remove blank lines
```

---

## Stream Editor (sed)

### Substitution

```bash
sed 's/old/new/' file.txt        # first occurrence per line
sed 's/old/new/g' file.txt       # all occurrences
sed 's/old/new/gi' file.txt      # case-insensitive
```

### In-Place Editing

```bash
sed -i 's/old/new/g' file.txt    # Linux
sed -i '' 's/old/new/g' file.txt # macOS
```

### Delete Lines

```bash
sed '/pattern/d' file.txt      # delete matching lines
sed '5d' file.txt              # delete line 5
sed '1,10d' file.txt           # delete lines 1-10
```

### Print Specific Lines

```bash
sed -n '5p' file.txt           # print line 5
sed -n '5,10p' file.txt        # print lines 5-10
sed -n '/pattern/p' file.txt   # print matching lines
```

### Multiple Operations

```bash
sed -e 's/a/b/' -e 's/c/d/' file.txt
```

---

## AWK Processing

Awk is a powerful text processing language.

### Basic Field Processing

```bash
awk '{print $1}' file.txt        # first field
awk '{print $2, $1}' file.txt    # reorder fields
awk '{print $NF}' file.txt       # last field
```

### With Patterns

```bash
awk '/error/ {print}' file.txt   # lines matching error
awk '$3 > 100 {print $1}' file.txt  # where field 3 > 100
```

### Field Separator

```bash
awk -F ',' '{print $1}' data.csv
awk -F ':' '{print $1}' /etc/passwd
```

### Built-in Variables

- `$0`: Entire line
- `$1`, `$2`...: Fields
- `NF`: Number of fields
- `NR`: Line number
- `FS`: Field separator

### Arithmetic

```bash
awk '{sum += $1} END {print sum}' numbers.txt
awk '{sum += $1} END {print sum/NR}' numbers.txt  # average
```

### Formatting Output

```bash
awk '{printf "%-10s %5d\n", $1, $2}' file.txt
```

---

## Other Useful Tools

### Reverse Lines

```bash
tac file.txt          # reverse line order
rev file.txt          # reverse each line's characters
```

### Shuffle Lines

```bash
shuf file.txt
```

### Split Files

```bash
split -l 1000 bigfile.txt part_    # 1000 lines per file
split -b 100m bigfile.bin part_    # 100MB per file
```

### Remove Blank Lines

```bash
grep -v '^$' file.txt
sed '/^$/d' file.txt
```

---

## Common Pipeline Patterns

### Top N of Something

```bash
# Top 10 most common words
tr ' ' '\n' < file.txt | sort | uniq -c | sort -rn | head -10
```

### Extract and Count

```bash
# Count HTTP status codes
cut -d ' ' -f 9 access.log | sort | uniq -c | sort -rn
```

### Filter and Transform

```bash
# Get usernames of users with bash shell
grep '/bin/bash$' /etc/passwd | cut -d ':' -f 1
```

### Data Cleanup

```bash
# Remove trailing whitespace
sed 's/[[:space:]]*$//' file.txt
```

---

## Exercises

### Exercise 1: Sort and Count
```bash
cat > fruits.txt << 'EOF'
apple
banana
apple
orange
banana
apple
EOF

sort fruits.txt | uniq -c | sort -rn
```

### Exercise 2: Extract Data
```bash
cat > data.csv << 'EOF'
Alice,25,Engineer
Bob,30,Designer
Carol,28,Manager
EOF

# Get names only
cut -d ',' -f 1 data.csv

# Get ages and sort
cut -d ',' -f 2 data.csv | sort -n
```

### Exercise 3: Transform Text
```bash
echo "hello world" | tr 'a-z' 'A-Z'
echo "  too   many   spaces  " | tr -s ' '
```

### Exercise 4: Awk Processing
```bash
cat > sales.txt << 'EOF'
Jan 100
Feb 150
Mar 200
EOF

# Sum all sales
awk '{sum += $2} END {print "Total:", sum}' sales.txt
```

---

## Key Takeaways

1. Always `sort` before `uniq`
2. `cut` extracts columns; `-d` sets delimiter
3. `sed 's/old/new/g'` for substitution
4. `awk '{print $1}'` for field processing
5. Pipes chain these tools into powerful pipelines

---

## Next Module

In Module 7, you'll master pipes and redirection - the foundation of Unix power.
