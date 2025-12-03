# Core Principles

These principles are **immutable**. Every feature, decision, and line of code must align with these values. When principles conflict, earlier principles take precedence.

---

## 1. Breadth Over Depth (Initially)

**We celebrate generalists who can tackle any project.**

The maker who can write a Python script, configure a Docker container, set up a network, and solder a sensor is more empowered than one who only knows advanced algorithms. Start wide, go deep where interest leads.

### In Practice
- Initial skill trees emphasize variety over mastery
- "Good enough" is celebrated when it solves the problem
- Cross-domain projects are highlighted over single-skill deep dives
- Depth is available but not required

---

## 2. Practical Over Perfect

**Working code that solves real problems beats pristine code that doesn't ship.**

We're not training people to pass code reviews at FAANG companies. We're helping people automate their lives. If it works and they understand it, it's good code.

### In Practice
- Projects prioritize "does it work?" over "is it elegant?"
- Best practices are taught as improvements, not prerequisites
- Technical debt is acceptable when it ships something useful
- Refactoring is a skill taught separately from building

---

## 3. Flexible Paths

**Non-linear progression based on interests and hardware.**

There is no "right" order to learn things. Someone with a Raspberry Pi starts differently than someone with just a laptop. Someone interested in home automation takes a different path than someone interested in data analysis.

### In Practice
- No forced prerequisites for most content
- Hardware-aware recommendations
- Interest-based path suggestions
- Skip what you know, dive into what you need

---

## 4. Integration Focus

**Real projects combine multiple skills.**

The best maker projects don't fit in one category. A plant watering system needs sensors, code, networking, and maybe a web dashboard. We optimize for these integration moments.

### In Practice
- Integration milestones unlock special projects
- Skill trees show connection points between domains
- "Capstone" projects require multiple skill areas
- The platform rewards breadth with interesting challenges

---

## 5. Accessibility First

**Start with just a laptop, scale up as desired.**

You shouldn't need to buy hardware to start learning. Every skill tree has a laptop-only entry point. Hardware expands possibilities but isn't required.

### In Practice
- All core languages work on any laptop (Python, HTML/CSS, Bash)
- Simulators and emulators before physical hardware
- Cloud-free by default (no accounts required to start)
- Hardware projects clearly marked with requirements

---

## 6. User Agency

**No gatekeeping. Users choose their path.**

We provide recommendations, not requirements. If someone wants to jump into advanced networking before learning Python basics, that's their choice. We'll warn them, but we won't stop them.

### In Practice
- All content accessible (with difficulty warnings)
- Recommendations are suggestions, not gates
- Users can mark skills as "known" and skip content
- No forced assessments or checkpoints

---

## 7. Scalable Architecture

**Build foundations that support both hobbyist exploration AND professional depth.**

Today's architecture must accommodate tomorrow's features without rewrites. Every system should handle simple hobbyist use cases AND complex professional scenarios.

### In Practice
- Data models include fields for future depth tracking
- APIs designed for extensibility
- Skill levels are continuous, not discrete
- Progress systems track both breadth and depth metrics

---

## 8. Progressive Complexity

**The same skill can be learned at "tinkerer" through "professional" levels.**

Python for automating your home is different from Python for production systems. Both are valid. The platform supports the full spectrum without forcing either path.

### In Practice
- Each skill has multiple depth levels
- Tinkerer content is complete and useful on its own
- Professional content builds on tinkerer foundations
- Users choose their target depth per skill

---

## Principle Conflicts

When principles conflict, use this priority order:
1. Accessibility First (can they even use this?)
2. User Agency (did they choose this?)
3. Practical Over Perfect (does it work?)
4. The rest as contextually appropriate

### Example Conflict Resolution
**Scenario**: Should we require Docker knowledge before teaching Kubernetes?

- **Principle 6 (User Agency)**: No, let them try
- **Principle 3 (Flexible Paths)**: No, maybe they learn differently
- **Principle 2 (Practical Over Perfect)**: Maybe, if it helps them succeed
- **Resolution**: Make it a strong recommendation with clear warnings, but don't gate the content

---

## Using These Principles

When making ANY decision about the platform:

1. Identify which principles apply
2. Check for conflicts
3. Use priority order to resolve
4. Document the reasoning in ARCHITECTURE_DECISIONS.md if significant

These principles are the constitution of this platform. Features change, technology changes, but these principles remain constant.
