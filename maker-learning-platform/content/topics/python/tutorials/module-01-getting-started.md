# Module 1: Getting Started with Python

**Concepts Covered**: 1-30
**Estimated Time**: 90-120 minutes
**Level**: 0 (Curious)

---

## What is Python?

Python is a high-level programming language that emphasizes readability and simplicity. Perfect for beginners and powerful enough for professionals.

**Why Python for makers?**
- Automate repetitive tasks
- Process and analyze data
- Build tools and utilities
- Control hardware (Raspberry Pi)
- Easy to learn, hard to master

---

## Installing Python

### Check if Python is Installed

```bash
python --version
# or
python3 --version
```

### Installation

- **Windows**: Download from python.org
- **macOS**: Comes pre-installed, or use `brew install python3`
- **Linux**: Usually pre-installed, or `sudo apt install python3`

**Recommendation**: Install Python 3.10 or newer.

---

## The Python Interpreter (REPL)

REPL = Read-Eval-Print Loop - an interactive Python session.

```bash
python3
```

You'll see:
```
>>>
```

Try it:
```python
>>> print("Hello, World!")
Hello, World!
>>> 2 + 2
4
>>> exit()
```

Great for testing ideas quickly!

---

## Your First Script

Create a file `hello.py`:

```python
# This is a comment
print("Hello, World!")
```

Run it:
```bash
python3 hello.py
```

**File extension**: Always use `.py` for Python files.

---

## Comments

```python
# Single-line comment

"""
Multi-line comment
(also called a docstring when used at the start of functions)
"""
```

Use comments to explain *why*, not *what*.

---

## Variables

Store data for later use:

```python
name = "Alice"
age = 25
height = 5.6
is_student = True

print(name)     # Alice
print(age)      # 25
```

### Variable Naming Rules

✅ Good:
```python
user_name = "Bob"
total_count = 10
MAX_SIZE = 100  # Constants in CAPS
```

❌ Bad:
```python
1st_name = "Bad"  # Can't start with number
user-name = "Bad"  # No hyphens
class = "Bad"     # Can't use keywords
```

---

## Python is Dynamically Typed

Variables can change type:

```python
x = 5        # x is an integer
x = "hello"  # now x is a string
```

---

## Basic Data Types

### Integers
```python
count = 42
negative = -10
```

### Floats
```python
price = 19.99
pi = 3.14159
```

### Strings
```python
name = "Alice"
message = 'Hello'
multiline = """This is
a multi-line
string"""
```

### Booleans
```python
is_active = True
is_complete = False
```

### None
```python
result = None  # Represents "no value"
```

---

## Checking Types

```python
x = 42
print(type(x))  # <class 'int'>

name = "Alice"
print(type(name))  # <class 'str'>
```

---

## Type Conversion

```python
# String to int
age = int("25")

# Int to string
age_str = str(25)

# String to float
price = float("19.99")

# Anything to bool
bool(0)        # False
bool(1)        # True
bool("")       # False
bool("hello")  # True
```

---

## Arithmetic Operators

```python
a = 10
b = 3

print(a + b)   # 13  (addition)
print(a - b)   # 7   (subtraction)
print(a * b)   # 30  (multiplication)
print(a / b)   # 3.333... (division)
print(a // b)  # 3   (integer division)
print(a % b)   # 1   (modulo/remainder)
print(a ** b)  # 1000 (exponentiation)
```

### Operator Precedence

```python
result = 2 + 3 * 4  # 14 (not 20)
# Multiplication before addition

# Use parentheses to be clear:
result = (2 + 3) * 4  # 20
```

---

## String Operations

### Concatenation
```python
first = "Hello"
last = "World"
full = first + " " + last  # "Hello World"
```

### Multiplication
```python
dashes = "-" * 10  # "----------"
```

### F-strings (Formatted Strings)
```python
name = "Alice"
age = 25

# The modern way:
message = f"My name is {name} and I'm {age} years old"
print(message)

# You can use expressions:
print(f"In 5 years, I'll be {age + 5}")
```

---

## Getting User Input

```python
name = input("What's your name? ")
print(f"Hello, {name}!")

# Input is always a string!
age = input("How old are you? ")
age = int(age)  # Convert to integer
print(f"Next year you'll be {age + 1}")
```

---

## Basic Program Structure

```python
# 1. Imports (if needed)
import math

# 2. Constants
PI = 3.14159

# 3. Functions (we'll learn these later)
def calculate_area(radius):
    return PI * radius ** 2

# 4. Main code
if __name__ == "__main__":
    r = float(input("Enter radius: "))
    area = calculate_area(r)
    print(f"Area: {area}")
```

The `if __name__ == "__main__":` part means "only run this if we're running this file directly."

---

## Virtual Environments (Quick Intro)

Virtual environments keep project dependencies separate.

```bash
# Create virtual environment
python3 -m venv myenv

# Activate it
source myenv/bin/activate  # Linux/Mac
myenv\Scripts\activate     # Windows

# Now install packages just for this project
pip install requests

# Deactivate when done
deactivate
```

We'll cover this more in Module 8.

---

## Code Style: PEP 8

PEP 8 is Python's style guide. Key points:

- Use 4 spaces for indentation (not tabs)
- Lines should be < 80 characters
- Use lowercase_with_underscores for variables
- Add spaces around operators: `x = 1` not `x=1`
- Blank lines between functions

Most editors can auto-format to PEP 8.

---

## Exercises

### Exercise 1: Hello You
Write a program that asks for your name and greets you.

```python
name = input("What's your name? ")
print(f"Hello, {name}!")
```

### Exercise 2: Calculator
```python
a = float(input("First number: "))
b = float(input("Second number: "))
print(f"{a} + {b} = {a + b}")
print(f"{a} * {b} = {a * b}")
```

### Exercise 3: Temperature Converter
```python
celsius = float(input("Temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C = {fahrenheit}°F")
```

### Exercise 4: Mad Libs
```python
noun = input("Enter a noun: ")
verb = input("Enter a verb: ")
adjective = input("Enter an adjective: ")

story = f"The {adjective} {noun} decided to {verb}."
print(story)
```

---

## Common Mistakes

❌ **Forgetting quotes around strings**
```python
name = Alice  # Error! Needs quotes
name = "Alice"  # Correct
```

❌ **String + number**
```python
age = 25
print("I am " + age)  # Error!
print("I am " + str(age))  # Correct
print(f"I am {age}")  # Even better
```

❌ **Using = instead of ==**
```python
if x = 5:  # Error! This is assignment
if x == 5:  # Correct! This is comparison
```

---

## Key Takeaways

1. Python emphasizes readability
2. Variables don't need type declarations
3. Use f-strings for string formatting
4. `input()` always returns a string
5. Follow PEP 8 style guidelines
6. Use the REPL to experiment

---

## Next Module

In Module 2, you'll master strings and text manipulation - essential for processing data and building tools.
