# Module 2: Strings and Text

**Concepts Covered**: 31-60
**Estimated Time**: 90-120 minutes
**Level**: 0 (Curious)

---

## String Basics

Strings are sequences of characters.

```python
# Single or double quotes - no difference
name = 'Alice'
message = "Hello, World!"

# Triple quotes for multi-line
description = """This is a
multi-line string that
spans several lines"""
```

---

## String Indexing

Access individual characters by position (starting at 0):

```python
word = "Python"

print(word[0])  # 'P'
print(word[1])  # 'y'
print(word[5])  # 'n'

# Negative indexing (from the end)
print(word[-1])  # 'n' (last character)
print(word[-2])  # 'o'
```

---

## String Slicing

Extract substrings:

```python
text = "Hello, World!"

print(text[0:5])    # 'Hello'
print(text[7:12])   # 'World'
print(text[:5])     # 'Hello' (start to 5)
print(text[7:])     # 'World!' (7 to end)
print(text[-6:])    # 'World!' (last 6 chars)
print(text[::2])    # 'Hlo ol!' (every 2nd char)
print(text[::-1])   # '!dlroW ,olleH' (reverse)
```

Slicing: `[start:stop:step]`

---

## String Length

```python
text = "Python"
print(len(text))  # 6
```

---

## Common String Methods

### Case Conversion
```python
text = "Hello World"

print(text.upper())      # 'HELLO WORLD'
print(text.lower())      # 'hello world'
print(text.title())      # 'Hello World'
print(text.capitalize()) # 'Hello world'
```

### Whitespace Removal
```python
text = "  Hello  "

print(text.strip())   # 'Hello'
print(text.lstrip())  # 'Hello  '
print(text.rstrip())  # '  Hello'
```

### Split and Join
```python
# Split string into list
sentence = "Python is awesome"
words = sentence.split()  # ['Python', 'is', 'awesome']

# Split by delimiter
data = "apple,banana,cherry"
fruits = data.split(',')  # ['apple', 'banana', 'cherry']

# Join list into string
words = ['Python', 'is', 'fun']
sentence = ' '.join(words)  # 'Python is fun'
```

### Replace
```python
text = "Hello World"
new_text = text.replace("World", "Python")
# 'Hello Python'

# Replace all occurrences
text = "apple apple apple"
new_text = text.replace("apple", "orange")
# 'orange orange orange'
```

### Find and Index
```python
text = "Hello World"

# find returns index or -1
pos = text.find("World")  # 6
pos = text.find("xyz")    # -1

# index returns index or raises error
pos = text.index("World")  # 6
# pos = text.index("xyz")  # ValueError!
```

### Startswith and Endswith
```python
filename = "report.pdf"

if filename.endswith(".pdf"):
    print("PDF file")

if filename.startswith("report"):
    print("Report file")
```

### Count
```python
text = "Mississippi"
print(text.count('s'))  # 4
print(text.count('ss')) # 2
```

---

## String Formatting

### Old Style (%)
```python
name = "Alice"
age = 25
text = "My name is %s and I'm %d" % (name, age)
```

### format() Method
```python
name = "Alice"
age = 25
text = "My name is {} and I'm {}".format(name, age)
text = "My name is {0} and I'm {1}".format(name, age)
text = "My name is {n} and I'm {a}".format(n=name, a=age)
```

### F-strings (Modern, Best)
```python
name = "Alice"
age = 25

# Basic usage
text = f"My name is {name} and I'm {age}"

# Expressions
text = f"Next year I'll be {age + 1}"

# Formatting numbers
price = 19.99
text = f"Price: ${price:.2f}"  # 'Price: $19.99'

# Alignment
text = f"{name:>10}"  # '     Alice' (right-aligned, width 10)
text = f"{name:<10}"  # 'Alice     ' (left-aligned)
text = f"{name:^10}"  # '  Alice   ' (centered)
```

---

## Escape Characters

```python
# Newline
print("Hello\nWorld")
# Hello
# World

# Tab
print("Name:\tAlice")  # Name:    Alice

# Quote in string
text = "He said, \"Hello\""

# Backslash
path = "C:\\Users\\Alice"
```

---

## Raw Strings

Useful for paths and regex:

```python
# Regular string (escapes processed)
path = "C:\\Users\\Alice\\Documents"

# Raw string (escapes ignored)
path = r"C:\Users\Alice\Documents"
```

---

## String Immutability

Strings cannot be modified in place:

```python
text = "Hello"
# text[0] = 'h'  # Error! Can't modify

# Create new string instead
text = 'h' + text[1:]  # 'hello'
```

---

## String Comparison

```python
a = "apple"
b = "banana"

print(a == b)   # False
print(a < b)    # True (alphabetical)
print(a != b)   # True

# Case-insensitive comparison
a = "Hello"
b = "hello"
print(a.lower() == b.lower())  # True
```

---

## Membership Testing

```python
text = "Python is awesome"

print("Python" in text)      # True
print("Java" in text)        # False
print("Java" not in text)    # True
```

---

## String Iteration

```python
for char in "Python":
    print(char)
# P
# y
# t
# h
# o
# n
```

---

## Regular Expressions (Intro)

For complex pattern matching:

```python
import re

text = "My email is alice@example.com"

# Search for pattern
match = re.search(r'\w+@\w+\.\w+', text)
if match:
    print(match.group())  # 'alice@example.com'

# Find all matches
text = "Call 555-1234 or 555-5678"
numbers = re.findall(r'\d{3}-\d{4}', text)
# ['555-1234', '555-5678']

# Replace with pattern
text = "Price: $19.99"
new_text = re.sub(r'\$[\d.]+', '$25.00', text)
# 'Price: $25.00'
```

Common regex patterns:
- `\d` - digit
- `\w` - word character
- `\s` - whitespace
- `.` - any character
- `*` - 0 or more
- `+` - 1 or more
- `?` - 0 or 1
- `{n}` - exactly n times

---

## Practical Examples

### Extract Domain from Email
```python
email = "alice@example.com"
domain = email.split('@')[1]
print(domain)  # 'example.com'
```

### Clean User Input
```python
name = input("Name: ").strip().title()
```

### Parse CSV Line
```python
line = "Alice,25,Engineer"
name, age, job = line.split(',')
```

### Build URL
```python
base = "https://api.example.com"
endpoint = "users"
user_id = 123
url = f"{base}/{endpoint}/{user_id}"
# 'https://api.example.com/users/123'
```

### Word Count
```python
text = "Python is fun and Python is powerful"
words = text.lower().split()
python_count = words.count('python')  # 2
```

---

## Exercises

### Exercise 1: Name Formatter
```python
full_name = input("Enter full name: ")
formatted = full_name.strip().title()
print(f"Formatted: {formatted}")
```

### Exercise 2: Email Validator
```python
email = input("Email: ")
if '@' in email and '.' in email:
    print("Valid format")
else:
    print("Invalid format")
```

### Exercise 3: Reverse Words
```python
sentence = "Python is awesome"
words = sentence.split()
reversed_words = ' '.join(reversed(words))
print(reversed_words)  # 'awesome is Python'
```

### Exercise 4: Count Vowels
```python
text = input("Enter text: ")
vowels = "aeiouAEIOU"
count = sum(1 for char in text if char in vowels)
print(f"Vowel count: {count}")
```

### Exercise 5: Extract Hashtags
```python
tweet = "Learning #Python is #awesome #coding"
import re
hashtags = re.findall(r'#\w+', tweet)
print(hashtags)  # ['#Python', '#awesome', '#coding']
```

---

## Common Patterns

### Check if string is numeric
```python
text = "12345"
if text.isdigit():
    print("All digits")
```

### Remove punctuation
```python
import string
text = "Hello, World!"
clean = text.translate(str.maketrans('', '', string.punctuation))
# 'Hello World'
```

### Pad with zeros
```python
number = 42
padded = str(number).zfill(5)  # '00042'
```

---

## Key Takeaways

1. Strings are immutable - operations create new strings
2. Use f-strings for formatting (modern Python)
3. String methods return new strings
4. Learn regex for complex text processing
5. Always validate/clean user input
6. Use `in` for simple pattern checking

---

## Next Module

In Module 3, you'll learn about Lists - Python's most versatile data structure for storing collections.
