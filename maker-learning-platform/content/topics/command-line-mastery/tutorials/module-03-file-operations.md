# Module 3: File Operations

**Concepts Covered**: 56-95
**Estimated Time**: 40-50 minutes

---

## Creating Files and Directories

### Create Empty File

```bash
touch newfile.txt
```

Creates file or updates timestamp if exists.

Windows:
```cmd
type nul > newfile.txt
# or in PowerShell
New-Item newfile.txt
```

### Create File with Content

```bash
echo "Hello World" > hello.txt
```

### Create Directory

```bash
mkdir projects
```

### Create Nested Directories

```bash
mkdir -p projects/web/frontend
```

Creates all intermediate directories.

Windows:
```cmd
mkdir projects\web\frontend
```

---

## Copying Files

### Copy Single File

```bash
cp source.txt destination.txt
```

### Copy to Directory

```bash
cp file.txt backup/
```

### Copy Directory (Recursive)

```bash
cp -r project/ project_backup/
```

Windows:
```cmd
copy source.txt destination.txt
xcopy /E /I project project_backup
```

---

## Moving and Renaming

### Move File

```bash
mv file.txt Documents/
```

### Rename File

```bash
mv oldname.txt newname.txt
```

Same command - just depends on whether destination is different location or same location with different name.

### Move and Rename

```bash
mv file.txt Documents/renamed.txt
```

Windows:
```cmd
move file.txt Documents\
ren oldname.txt newname.txt
```

---

## Deleting Files

### Delete File

```bash
rm file.txt
```

### Delete Multiple Files

```bash
rm file1.txt file2.txt file3.txt
```

### Delete with Confirmation

```bash
rm -i file.txt
```

Asks before deleting.

### Force Delete

```bash
rm -f file.txt
```

No warnings, no prompts.

Windows:
```cmd
del file.txt
```

---

## Deleting Directories

### Delete Empty Directory

```bash
rmdir empty_folder
```

### Delete Directory with Contents

```bash
rm -r folder/
```

**Warning**: This is permanent! No recycle bin.

### Force Delete Directory

```bash
rm -rf folder/
```

Use with extreme caution!

Windows:
```cmd
rmdir /S /Q folder
```

---

## Safe Deletion Practices

1. **Double-check paths** before `rm -r`
2. **Use `-i` flag** for interactive confirmation
3. **Test with `ls` first**: `ls folder/*` before `rm folder/*`
4. **Avoid `rm -rf /`** - never run this!
5. **Consider trash utilities**: `trash-cli` moves to trash instead

---

## File Permissions (Unix)

### Understanding Permission String

```
-rwxr-xr-x 1 user group 4096 Jan 15 10:00 script.sh
```

Breaking down `-rwxr-xr-x`:
- Position 1: Type (`-` file, `d` directory, `l` link)
- Positions 2-4: Owner permissions (rwx)
- Positions 5-7: Group permissions (r-x)
- Positions 8-10: Others permissions (r-x)

### Permission Types

- **r** (read): View contents
- **w** (write): Modify contents
- **x** (execute): Run as program

### Viewing Permissions

```bash
ls -l file.txt
```

---

## Changing Permissions

### Symbolic Mode

```bash
chmod u+x script.sh    # add execute for user
chmod g-w file.txt     # remove write for group
chmod o=r file.txt     # set others to read only
chmod a+r file.txt     # add read for all
```

### Numeric Mode

Each permission has a value:
- r = 4
- w = 2
- x = 1

Add them up for each category:
```bash
chmod 755 script.sh    # rwxr-xr-x
chmod 644 file.txt     # rw-r--r--
chmod 600 secret.txt   # rw-------
```

Common patterns:
- **755**: Executable files
- **644**: Regular files
- **600**: Private files

---

## Changing Ownership

```bash
chown user:group file.txt
chown -R user:group folder/
```

Requires root/sudo permissions.

---

## Windows File Attributes

```cmd
attrib +h file.txt    # hidden
attrib +r file.txt    # read-only
attrib -h file.txt    # unhide
```

---

## File Information

### File Size

```bash
ls -lh file.txt
# -rw-r--r-- 1 user group 2.3M Jan 15 10:00 file.txt
```

### Disk Usage

```bash
du -sh folder/          # size of folder
du -sh *                 # size of each item
du -h --max-depth=1     # one level deep
```

### Free Space

```bash
df -h
```

Shows available space on all drives.

---

## Symbolic Links

Links are like shortcuts:

### Create Symbolic Link

```bash
ln -s /path/to/original link_name
```

### Example

```bash
ln -s ~/projects/myapp/config.json ~/.config/myapp.json
```

Now `~/.config/myapp.json` points to the original.

### View Links

```bash
ls -l
# lrwxrwxrwx 1 user group 32 Jan 15 10:00 link -> /path/to/original
```

---

## Wildcards

### Match Any Characters

```bash
ls *.txt          # all .txt files
rm temp_*         # all files starting with temp_
cp *.jpg images/  # copy all JPGs
```

### Match Single Character

```bash
ls file?.txt      # file1.txt, file2.txt, etc.
```

### Match Range

```bash
ls file[1-3].txt  # file1.txt, file2.txt, file3.txt
ls [abc]*.txt     # files starting with a, b, or c
```

---

## Exercises

### Exercise 1: Create Project Structure
```bash
mkdir -p project/{src,tests,docs}
touch project/README.md
touch project/src/main.py
ls -R project
```

### Exercise 2: Safe Copy Practice
```bash
echo "important data" > original.txt
cp original.txt backup.txt
ls -l *.txt
```

### Exercise 3: Permission Changes
```bash
touch script.sh
ls -l script.sh         # check permissions
chmod +x script.sh      # make executable
ls -l script.sh         # verify change
```

### Exercise 4: Wildcard Operations
```bash
touch test{1,2,3}.txt
ls test*.txt
mv test*.txt backup/
```

---

## Key Takeaways

1. `mkdir -p` creates nested directories
2. `cp -r` copies directories recursively
3. `mv` both moves and renames
4. `rm -r` deletes directories (careful!)
5. Use `chmod` for permissions (755, 644)
6. Wildcards (`*`, `?`) match multiple files

---

## Next Module

In Module 4, you'll learn to view and read file contents using cat, less, head, tail, and other tools.
