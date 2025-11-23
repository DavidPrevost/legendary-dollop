# Project Foundations - User Experience Simulation

Simulated walkthrough of a user's journey through the Project Foundations subject.

---

## Simulation Setup

**User Persona**: Alex, a hobbyist interested in home automation
- Has some Python experience
- Never used Git properly
- Documentation is weak point
- Using Windows 11

**Starting Point**: Fresh install of the platform

---

## Level 0: Curious

### Step 1: Platform Tour

**Action**: Alex launches the platform for the first time

**Experience**:
- Sees welcome message and main menu
- Navigates to "Explore Subjects"
- Clicks on "Project Foundations"
- Sees it's the recommended starting point

**Feedback**:
- ✅ Clear that this is the starting point
- ⚠️ Need visual indicator that this is the "tutorial" subject
- 📝 Add "Start Here" badge to Project Foundations

### Step 2: Starting Level 0

**Action**: Alex clicks "Start Learning"

**Experience**:
- Sees Module 1: Platform Introduction
- Reads about the platform structure
- Learns about Subjects, Levels, and Projects

**Feedback**:
- ✅ Content is welcoming and clear
- ✅ Good explanation of Subjects vs Topics
- ⚠️ Would benefit from screenshots of actual UI
- 📝 Add screenshots once UI is implemented

### Step 3: Understanding Documentation

**Action**: Continues to Module 2

**Experience**:
- Reads about why documentation matters
- "Documentation as a gift to future-you" resonates
- Minimum viable documentation concept is helpful

**Feedback**:
- ✅ Strong motivation for documentation
- ✅ Practical, not preachy
- ✅ Good balance of why and what

### Step 4: Level 0 Project

**Action**: Starts "Platform Explorer" milestone project

**Experience**:
- Follows guided platform tour
- Sets up maker profile
- Writes reflection on learning goals
- Runs capability detection

**Issues Found**:
- ❌ Profile setup not yet implemented
- ❌ Capability detection exists but no UI for manual input
- ❌ No place to save reflection document

**Feedback**:
- 📝 Need to implement profile setup UI
- 📝 Need file save location for projects
- 📝 Add "Create New Project" command that scaffolds folders

### Step 5: Project Validation

**Action**: Submits project for validation

**Experience**:
- Validator checks for reflection file
- Checks word count
- Checks profile completion

**Feedback**:
- ✅ Validation criteria are clear
- ⚠️ Need better error messages when checks fail
- 📝 Add suggestions for fixing validation failures

---

## Level 1: Explorer

### Step 1: Learning Markdown

**Action**: Starts Module 3

**Experience**:
- Works through Markdown syntax
- Examples are clear and copyable
- Tries code blocks with Python syntax highlighting

**Feedback**:
- ✅ Comprehensive Markdown coverage
- ✅ Good examples throughout
- ⚠️ Would benefit from live preview
- 📝 Consider adding Markdown preview in future GUI

### Step 2: Practice Exercise

**Action**: Attempts practice exercise at end of module

**Experience**:
- Creates document with all required elements
- Not sure where to save it
- Not sure if it's correct

**Issues Found**:
- ❌ No designated place for practice files
- ❌ No way to validate practice (only milestone projects)

**Feedback**:
- 📝 Add practice folder in project directory
- 📝 Consider adding validation for practice exercises
- 📝 Or make clear practice is self-checked

### Step 3: Level 1 Project

**Action**: Starts "Personal README" milestone project

**Experience**:
- Creates PERSONAL_README.md
- Uses all required Markdown elements
- Writes about personal goals and hardware

**Feedback**:
- ✅ Project is useful and personal
- ✅ Requirements are clear
- ✅ Can reuse this on GitHub
- ⚠️ Extension with shields.io badges would be cool but needs network

### Step 4: Project Validation

**Action**: Runs validation on Personal README

**Experience**:
- Checks file exists ✅
- Checks heading levels ✅
- Checks for lists, tables, code blocks ✅
- Checks Markdown syntax ✅

**Feedback**:
- ✅ Validation is thorough
- ✅ Catches missing elements
- 📝 Consider checking for placeholder text ("Lorem ipsum", "TODO")

---

## Level 2: Tinkerer

### Step 1: README and Structure

**Action**: Works through Modules 4 and 5

**Experience**:
- Learns README best practices
- Learns project structure conventions
- Sees Python and JavaScript examples

**Feedback**:
- ✅ Good coverage of both topics
- ✅ Practical conventions that match real projects
- ⚠️ Would benefit from template files to download

### Step 2: Level 2 Project

**Action**: Starts "Project Scaffold" project

**Experience**:
- Chooses "File Organizer" as project idea
- Creates full directory structure
- Writes README with all sections
- Adds LICENSE, .gitignore, CONTRIBUTING, CHANGELOG

**Issues Found**:
- ❌ No way to get LICENSE text (needs to look up)
- ❌ No gitignore templates available
- ❌ Takes longer than expected to write all files

**Feedback**:
- 📝 Add command to generate LICENSE files
- 📝 Add command to generate .gitignore from template
- 📝 Consider providing starter templates
- 📝 Update time estimate to 3-5 hours

### Step 3: Project Validation

**Action**: Validates Project Scaffold

**Experience**:
- All files checked ✅
- README sections checked ✅
- License validity checked ✅
- Changelog format checked ✅

**Feedback**:
- ✅ Comprehensive validation
- ⚠️ "No placeholder text" check would be helpful
- 📝 Add check for "TODO", "TBD", "Lorem" in files

---

## Level 3: Builder

### Step 1: Planning Modules

**Action**: Works through Modules 6, 7, 8

**Experience**:
- Learns problem statements and goals
- Learns user stories and acceptance criteria
- Learns estimation techniques

**Feedback**:
- ✅ Very practical planning guidance
- ✅ MoSCoW and estimation are well-explained
- ⚠️ Lots of new concepts—may feel overwhelming
- 📝 Consider splitting into smaller chunks

### Step 2: Level 3 Project

**Action**: Starts "Project Planner" project

**Experience**:
- Chooses "Home Dashboard" as project to plan
- Writes problem statement
- Creates user stories with acceptance criteria
- Breaks down into tasks
- Estimates time

**Feedback**:
- ✅ Excellent practice for planning skills
- ✅ No code required—focuses on planning
- ✅ Produces useful artifact for future project
- ⚠️ Time consuming—may take 4-6 hours not 3-5

### Step 3: Project Validation

**Action**: Validates Project Planner

**Experience**:
- All sections checked ✅
- User story format validated ✅
- Pattern counting works ✅

**Feedback**:
- ⚠️ Manual checks are numerous—needs clear checklist
- 📝 Consider checklist UI for manual validation
- 📝 Update time estimate to 4-6 hours

---

## Level 4: Maker

### Step 1: Technical Documentation

**Action**: Works through Modules 9, 10, 11

**Experience**:
- Learns architecture documentation
- Learns ADR format
- Learns API documentation
- Learns docs-as-code approach

**Feedback**:
- ✅ Professional-grade content
- ✅ ADR format is clear and useful
- ✅ Good transition to "applying everything"
- ⚠️ This is advanced—appropriate for Level 4

### Step 2: Level 4 Project

**Action**: Starts "Documentation Suite" project

**Experience**:
- Uses Project Scaffold from Level 2
- Creates architecture doc with diagram
- Writes two ADRs
- Documents API (mock for learning)
- Creates configuration docs
- Maintains changelog

**Feedback**:
- ✅ Capstone project brings everything together
- ✅ Results in portfolio-worthy documentation
- ⚠️ Most time-consuming project—may take 5-7 hours
- 📝 Update time estimate to 5-7 hours

### Step 3: Final Validation

**Action**: Validates Documentation Suite

**Experience**:
- All files checked ✅
- ADR format validated ✅
- Changelog format validated ✅

**Feedback**:
- ✅ Completion feels like a real achievement
- 📝 Add certificate or badge for completing the subject

---

## Overall UX Assessment

### Strengths
1. **Content quality** - Tutorials are comprehensive and clear
2. **Progressive difficulty** - Levels build on each other well
3. **Practical projects** - Every project produces something useful
4. **Validation system** - Automated checks provide clear feedback

### Issues to Address

#### Critical
1. **Missing infrastructure** - Profile setup, project folders not implemented
2. **Template files** - No LICENSE/gitignore templates available
3. **Project workspace** - No clear place for user's project files

#### Important
1. **Time estimates** - Several projects underestimated
2. **Practice exercises** - No validation or storage for practice
3. **Manual validation** - Needs better UI for checking manual criteria

#### Nice to Have
1. **Screenshots** - UI screenshots once implemented
2. **Live preview** - Markdown preview in GUI
3. **Completion rewards** - Badges or certificates

---

## Recommended Changes

### For Pass 9 (Incorporate Feedback)

1. **Update time estimates**:
   - Level 2: 2-4 hours → 3-5 hours
   - Level 3: 3-5 hours → 4-6 hours
   - Level 4: 4-6 hours → 5-7 hours

2. **Add placeholder checks** to validation:
   - Detect "TODO", "TBD", "Lorem ipsum", "example.com"

3. **Create helper commands**:
   - `maker new-project <name>` - creates project folder structure
   - `maker add-license <type>` - adds LICENSE file
   - `maker add-gitignore <language>` - adds .gitignore

4. **Clarify practice exercises**:
   - State they are self-checked
   - Suggest saving in `practice/` folder

5. **Add completion tracking**:
   - Badge or message when subject is complete
   - Summary of skills gained

---

## User Journey Duration

**Estimated total time for Subject 1: Project Foundations**

| Level | Original Estimate | Revised Estimate |
|-------|-------------------|------------------|
| 0: Curious | 1-2 hours | 1-2 hours |
| 1: Explorer | 2-3 hours | 2-3 hours |
| 2: Tinkerer | 2-4 hours | 3-5 hours |
| 3: Builder | 3-5 hours | 4-6 hours |
| 4: Maker | 4-6 hours | 5-7 hours |
| **Total** | **12-20 hours** | **15-23 hours** |

---

## Conclusion

The Project Foundations subject provides a solid learning experience with comprehensive content and practical projects. The main gaps are in supporting infrastructure (profile, project workspace, templates) which will be addressed in platform development.

The tutorials and validation systems are ready for use. User experience will improve significantly once the GUI is implemented.
