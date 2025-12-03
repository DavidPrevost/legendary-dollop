# Python - Concept List

Total concepts: 450
Organized into 15 modules covering fundamentals through automation and integration.

---

## Module 1: Getting Started (Concepts 1-30)

1. What is Python
2. Python 2 vs Python 3
3. Installing Python
4. Python interpreter (REPL)
5. Running Python scripts
6. Python file extension (.py)
7. Print function
8. Comments (# and docstrings)
9. Code indentation importance
10. Python style guide (PEP 8)
11. Variables
12. Variable naming rules
13. Dynamic typing
14. Basic data types overview
15. Integers
16. Floats
17. Strings
18. Booleans
19. None type
20. Type checking (type())
21. Type conversion (int, str, float)
22. Basic arithmetic operators
23. Operator precedence
24. String concatenation
25. String multiplication
26. F-strings (formatted strings)
27. Input from user
28. Basic program structure
29. IDE vs text editor
30. Virtual environments intro

---

## Module 2: Strings and Text (Concepts 31-60)

31. String creation (quotes)
32. Single vs double quotes
33. Triple quotes (multiline)
34. String indexing
35. Negative indexing
36. String slicing
37. String length (len)
38. String methods overview
39. upper() and lower()
40. strip(), lstrip(), rstrip()
41. split() method
42. join() method
43. replace() method
44. find() and index()
45. startswith() and endswith()
46. count() method
47. String formatting (%)
48. format() method
49. F-string expressions
50. Escape characters
51. Raw strings
52. String immutability
53. String comparison
54. in operator for strings
55. String iteration
56. Common string patterns
57. Regular expressions intro
58. re.search()
59. re.findall()
60. re.sub()

---

## Module 3: Collections - Lists (Concepts 61-95)

61. List creation
62. List indexing
63. List slicing
64. List mutability
65. Modifying list elements
66. List length
67. append() method
68. extend() method
69. insert() method
70. remove() method
71. pop() method
72. clear() method
73. index() method
74. count() method
75. sort() method
76. sorted() function
77. reverse() method
78. List copying (shallow vs deep)
79. List concatenation
80. List multiplication
81. in operator for lists
82. List iteration
83. Nested lists
84. List comprehensions basic
85. List comprehensions with condition
86. Nested list comprehensions
87. Unpacking lists
88. zip() with lists
89. enumerate() with lists
90. map() with lists
91. filter() with lists
92. any() and all()
93. min() and max()
94. sum() function
95. Common list patterns

---

## Module 4: Collections - Dictionaries and Sets (Concepts 96-130)

96. Dictionary creation
97. Dictionary keys and values
98. Accessing dictionary values
99. get() method
100. Adding/modifying items
101. Removing items (del, pop)
102. keys() method
103. values() method
104. items() method
105. Dictionary iteration
106. in operator for dicts
107. Dictionary comprehensions
108. Nested dictionaries
109. Merging dictionaries
110. Default values (setdefault)
111. fromkeys() method
112. Set creation
113. Set properties (unique, unordered)
114. Adding to sets
115. Removing from sets
116. Set operations (union)
117. Set operations (intersection)
118. Set operations (difference)
119. Set operations (symmetric diff)
120. Set comprehensions
121. Frozen sets
122. Tuples
123. Tuple packing/unpacking
124. Named tuples
125. When to use each collection
126. Collections module overview
127. Counter
128. defaultdict
129. OrderedDict
130. deque

---

## Module 5: Control Flow (Concepts 131-165)

131. Boolean expressions
132. Comparison operators
133. Logical operators (and, or, not)
134. Truthiness and falsiness
135. if statement
136. else clause
137. elif clause
138. Nested conditions
139. Ternary operator
140. for loop
141. Looping over sequences
142. range() function
143. while loop
144. break statement
145. continue statement
146. else clause in loops
147. pass statement
148. Nested loops
149. Loop patterns
150. Iterators concept
151. iter() and next()
152. Custom iterators
153. Generators introduction
154. yield statement
155. Generator expressions
156. Generator benefits
157. match statement (3.10+)
158. Pattern matching
159. Walrus operator (:=)
160. Short-circuit evaluation
161. Chained comparisons
162. Exception basics
163. try/except
164. finally clause
165. raise statement

---

## Module 6: Functions (Concepts 166-210)

166. Function definition
167. Function calling
168. Parameters vs arguments
169. Return statement
170. Multiple return values
171. Default parameters
172. Keyword arguments
173. Positional arguments
174. *args (variable positional)
175. **kwargs (variable keyword)
176. Argument order rules
177. Docstrings
178. Function annotations
179. Scope (local vs global)
180. global keyword
181. nonlocal keyword
182. LEGB rule
183. First-class functions
184. Functions as arguments
185. Functions as return values
186. Lambda functions
187. Lambda use cases
188. Closures
189. Decorators introduction
190. Decorator syntax (@)
191. Writing decorators
192. Decorators with arguments
193. functools.wraps
194. Built-in decorators
195. @property
196. @staticmethod
197. @classmethod
198. Recursion
199. Recursive base case
200. Recursive patterns
201. Memoization
202. Higher-order functions
203. Partial functions
204. Function composition
205. Pure functions
206. Side effects
207. Functional programming concepts
208. map/filter/reduce
209. Operator module
210. Best practices

---

## Module 7: Object-Oriented Programming (Concepts 211-260)

211. OOP concepts overview
212. Classes vs objects
213. Class definition
214. __init__ method
215. self parameter
216. Instance attributes
217. Instance methods
218. Class attributes
219. Accessing attributes
220. Encapsulation concept
221. Private attributes convention
222. Property decorators
223. Getters and setters
224. Inheritance basics
225. Parent and child classes
226. super() function
227. Method overriding
228. Multiple inheritance
229. Method Resolution Order
230. Composition vs inheritance
231. Polymorphism
232. Duck typing
233. Abstract classes
234. ABC module
235. Interfaces concept
236. Magic methods overview
237. __str__ and __repr__
238. __len__ and __bool__
239. __eq__ and __hash__
240. __lt__, __gt__ (comparisons)
241. __add__, __mul__ (operators)
242. __getitem__, __setitem__
243. __iter__ and __next__
244. __call__ method
245. __enter__ and __exit__
246. Context managers
247. with statement
248. Class decorators
249. Metaclasses intro
250. dataclasses module
251. @dataclass decorator
252. Field customization
253. Slots
254. Class methods vs static
255. Factory methods
256. Singleton pattern
257. Observer pattern
258. Strategy pattern
259. Design patterns overview
260. SOLID principles intro

---

## Module 8: Modules and Packages (Concepts 261-290)

261. Module concept
262. import statement
263. from...import
264. import...as (aliasing)
265. __name__ variable
266. if __name__ == "__main__"
267. Module search path
268. sys.path
269. Package concept
270. __init__.py
271. Subpackages
272. Relative imports
273. Absolute imports
274. Circular imports
275. Standard library overview
276. os module
277. sys module
278. datetime module
279. json module
280. pathlib module
281. shutil module
282. subprocess module
283. argparse module
284. logging module
285. configparser module
286. Installing packages (pip)
287. requirements.txt
288. Virtual environments
289. venv module
290. Package managers (pip, poetry)

---

## Module 9: File Handling (Concepts 291-325)

291. Opening files
292. File modes (r, w, a, b)
293. Reading entire file
294. Reading lines
295. readline() and readlines()
296. Writing to files
297. writelines()
298. Closing files
299. with statement for files
300. File paths
301. Absolute vs relative paths
302. pathlib.Path
303. Path operations
304. Checking file existence
305. Directory operations
306. Creating directories
307. Listing directories
308. Walking directories
309. File metadata
310. Temporary files
311. CSV files
312. csv.reader
313. csv.writer
314. csv.DictReader
315. JSON files
316. json.load and dump
317. JSON encoding/decoding
318. Binary files
319. Pickle module
320. Excel files (openpyxl)
321. Configuration files
322. INI files
323. YAML files
324. File compression (zipfile)
325. Best practices

---

## Module 10: Error Handling (Concepts 326-355)

326. Exception types
327. try/except block
328. Catching specific exceptions
329. Multiple except blocks
330. except...as
331. else clause
332. finally clause
333. raise statement
334. Custom exceptions
335. Exception hierarchy
336. Built-in exceptions
337. ValueError
338. TypeError
339. KeyError
340. IndexError
341. FileNotFoundError
342. AttributeError
343. ImportError
344. RuntimeError
345. Exception chaining
346. Context in exceptions
347. Assertions
348. assert statement
349. Debugging with assertions
350. Warnings module
351. Logging exceptions
352. Traceback module
353. Error handling patterns
354. EAFP vs LBYL
355. Best practices

---

## Module 11: Working with Data (Concepts 356-390)

356. Data formats overview
357. Structured vs unstructured
358. JSON handling
359. XML basics
360. HTML parsing
361. BeautifulSoup intro
362. Requests library
363. HTTP methods
364. API concepts
365. REST APIs
366. API authentication
367. Query parameters
368. Response handling
369. Error handling (HTTP)
370. Rate limiting
371. Pagination
372. Data validation
373. Schema validation
374. SQLite basics
375. Creating databases
376. SQL queries in Python
377. sqlite3 module
378. Cursor and connection
379. Parameterized queries
380. ORM concept
381. Database best practices
382. Data serialization
383. Pickle vs JSON
384. CSV processing
385. Data cleaning
386. Regular expressions
387. Date/time handling
388. Timezones
389. Data transformation
390. Common patterns

---

## Module 12: Automation Basics (Concepts 391-420)

391. Automation use cases
392. File organization scripts
393. Batch renaming
394. Backup scripts
395. System information
396. Process automation
397. Scheduled tasks
398. Environment variables
399. Command-line arguments
400. argparse usage
401. Click library intro
402. User input validation
403. Progress indicators
404. Logging setup
405. Log levels
406. Log formatting
407. Notification systems
408. Email sending (smtplib)
409. Desktop notifications
410. Clipboard operations
411. GUI automation intro
412. Screenshots
413. Keyboard/mouse control
414. Web scraping ethics
415. Robots.txt
416. Rate limiting
417. Error recovery
418. Retry logic
419. Script organization
420. Best practices

---

## Module 13: Testing and Debugging (Concepts 421-445)

421. Why test code
422. Test types overview
423. Unit testing concept
424. unittest module
425. Test cases
426. Assertions in tests
427. Test fixtures
428. setUp and tearDown
429. Running tests
430. pytest introduction
431. pytest fixtures
432. Parametrized tests
433. Test coverage
434. Mocking basics
435. unittest.mock
436. Debugging techniques
437. print debugging
438. pdb module
439. Breakpoints
440. IDE debugging
441. Profiling code
442. timeit module
443. Memory profiling
444. Code review practices
445. Documentation testing

---

## Module 14: Advanced Topics (Concepts 446-465)

446. Type hints
447. typing module
448. Generic types
449. Protocol classes
450. Async programming intro
451. async/await
452. asyncio basics
453. Concurrent futures
454. Threading basics
455. Multiprocessing basics
456. GIL explanation
457. Memory management
458. Garbage collection
459. Weak references
460. Context variables
461. Descriptors
462. Import hooks
463. Code inspection
464. AST module
465. Optimization tips

---

## Module 15: Project Integration (Concepts 466-450)

Note: This section overlaps with module 14, representing synthesis.

- Combining concepts for real projects
- Project structure best practices
- Code organization
- Documentation
- Version control integration
- Deployment basics
- Package distribution
- CI/CD concepts
- Code quality tools
- Community resources

---

## Concept Distribution by Level

- **Level 0 (Curious)**: Concepts 1-95 (95 concepts)
  - Getting started, strings, lists basics

- **Level 1 (Explorer)**: Concepts 96-210 (115 concepts)
  - Collections, control flow, functions

- **Level 2 (Tinkerer)**: Concepts 211-325 (115 concepts)
  - OOP, modules, file handling

- **Level 3 (Builder)**: Concepts 326-420 (95 concepts)
  - Error handling, data, automation

- **Level 4 (Maker)**: Concepts 421-465 (45 concepts)
  - Testing, debugging, advanced topics

---

## Prerequisites

- Command Line Mastery (recommended) - for running scripts
- Project Foundations - for documentation practices

## Feeds Into

- Testing Fundamentals - deeper testing concepts
- Databases - SQL integration
- Docker/Compose - containerizing Python apps
