# Python - Milestone Projects

Each level concludes with a practical project that produces useful, reusable output.

---

## Level 0: Text Statistics Tool

**Project**: Build a text analysis utility

### Description
Create a script that analyzes text files and provides statistics like word count, character count, most common words, and average word length. Outputs a formatted report.

### Deliverables
1. Python script (text_stats.py)
2. Sample text file to analyze
3. Generated statistics report

### Skills Demonstrated
- Reading files
- String manipulation
- List operations
- Dictionary for word counting
- Formatted output

### Success Criteria
- Counts total words, characters, lines
- Finds top 10 most common words
- Calculates average word length
- Handles different file inputs
- Produces readable formatted output

### Estimated Time
60-90 minutes

---

## Level 1: Personal Expense Tracker

**Project**: Build a command-line expense tracker

### Description
Create an application that tracks expenses with categories, dates, and amounts. Data is stored in a JSON file. Provides add, list, and summary functions.

### Deliverables
1. Python script (expense_tracker.py)
2. Data file (expenses.json)
3. Usage documentation

### Skills Demonstrated
- Dictionaries for data structure
- JSON file read/write
- Functions for organization
- Control flow for menu
- Date handling
- Error handling

### Success Criteria
- Add expenses with amount, category, date
- List expenses with filtering
- Show summary by category
- Persist data between runs
- Handle invalid input gracefully

### Estimated Time
90-120 minutes

---

## Level 2: Contact Book Application

**Project**: Build an OOP-based contact manager

### Description
Create a contact book using classes to model contacts and the contact book. Supports add, search, edit, delete operations with data persistence.

### Deliverables
1. Python module (contact_book/)
2. Contact and ContactBook classes
3. CSV export/import
4. CLI interface

### Skills Demonstrated
- Class design
- Special methods (__str__, __repr__)
- File I/O (JSON and CSV)
- Module organization
- Search functionality

### Success Criteria
- Contact class with name, phone, email
- ContactBook with CRUD operations
- Search by name (partial match)
- Export to CSV
- Import from CSV
- Data persistence

### Estimated Time
120-150 minutes

---

## Level 3: Weather Dashboard

**Project**: Build an API-powered weather information tool

### Description
Create a CLI tool that fetches weather data from a public API and displays current conditions and forecasts. Includes caching and error handling.

### Deliverables
1. Python script (weather.py)
2. Configuration for API key
3. Cached data storage
4. Logging setup

### Skills Demonstrated
- HTTP requests
- API consumption
- JSON parsing
- Error handling (network, API)
- Caching
- Logging
- argparse CLI

### Success Criteria
- Fetch current weather by city
- Display temperature, humidity, conditions
- Show 5-day forecast (optional)
- Cache results to reduce API calls
- Handle network errors gracefully
- Log operations for debugging

### Estimated Time
120-180 minutes

---

## Level 4: File Organizer with Tests

**Project**: Build a tested file organization tool

### Description
Create a file organizer that sorts files by type, date, or custom rules. Include comprehensive tests and type hints for production quality.

### Deliverables
1. Python package (file_organizer/)
2. Core organizer module
3. Configuration system
4. Test suite (pytest)
5. Type annotations
6. Documentation

### Skills Demonstrated
- Testing with pytest
- Type hints
- Package structure
- Configuration handling
- File operations
- Mocking for tests
- Documentation

### Success Criteria
- Organizes files by extension/date
- Configurable rules
- Dry-run mode
- Test coverage > 80%
- Type hints on all functions
- Handles edge cases (permissions, symlinks)

### Estimated Time
180-240 minutes

---

## Project Progression

| Level | Project | Core Skills | Output |
|-------|---------|-------------|--------|
| 0 | Text Statistics | Strings, lists, files | Analysis report |
| 1 | Expense Tracker | Dicts, JSON, functions | Tracking app |
| 2 | Contact Book | OOP, modules, CSV | Contact manager |
| 3 | Weather Dashboard | APIs, errors, logging | Weather CLI |
| 4 | File Organizer | Testing, types, packaging | Production tool |

---

## Real-World Application

All projects solve genuine maker problems:

- **Text Statistics**: Analyze notes, logs, or documents
- **Expense Tracker**: Personal finance tracking
- **Contact Book**: Manage project contacts
- **Weather Dashboard**: Daily information check
- **File Organizer**: Tame downloads folder

---

## Extension Ideas

Each project can be extended:

- **Text Statistics**: Add sentiment analysis, keyword extraction
- **Expense Tracker**: Add budgets, charts, monthly reports
- **Contact Book**: Add groups, import from vCard
- **Weather Dashboard**: Add GUI, alerts, multiple locations
- **File Organizer**: Add watch mode, undo, custom rules
