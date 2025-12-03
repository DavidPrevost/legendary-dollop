# Command Line Mastery - Concept List

Total concepts: 380
Organized into 12 modules covering terminal fundamentals through advanced automation.

---

## Module 1: Terminal Fundamentals (Concepts 1-25)

1. What is a terminal/console
2. Terminal vs shell distinction
3. Common shells (Bash, Zsh, PowerShell, CMD)
4. Opening terminal on Windows
5. Opening terminal on macOS
6. Opening terminal on Linux
7. Terminal window anatomy
8. Command prompt structure
9. Cursor and text entry
10. Command execution (Enter key)
11. Case sensitivity differences
12. Command history navigation (up/down arrows)
13. Clearing the screen (clear/cls)
14. Exiting the terminal
15. Multiple terminal windows/tabs
16. Terminal vs GUI tradeoffs
17. When to use terminal
18. Terminal emulators
19. Default shell configuration
20. Shell prompt customization basics
21. Terminal color schemes
22. Font and size settings
23. Copy and paste in terminal
24. Keyboard shortcuts overview
25. Tab completion introduction

---

## Module 2: Navigation Basics (Concepts 26-55)

26. File system hierarchy concept
27. Root directory
28. Home directory
29. Current working directory
30. Print working directory (pwd)
31. Directory listing (ls/dir)
32. Listing with details (ls -l)
33. Showing hidden files (ls -a)
34. Human-readable sizes (ls -h)
35. Change directory (cd)
36. Absolute paths
37. Relative paths
38. Parent directory (..)
39. Current directory (.)
40. Home directory shortcut (~)
41. Previous directory (cd -)
42. Path separators (/ vs \)
43. Spaces in paths
44. Special characters in paths
45. Path autocomplete with Tab
46. Navigating deep directories
47. Directory stack (pushd/popd)
48. Creating bookmarks/aliases for directories
49. Understanding PATH environment variable
50. Which command to find executables
51. Where command (Windows)
52. Locating installed programs
53. Common directory locations
54. Temporary directories
55. User vs system directories

---

## Module 3: File Operations (Concepts 56-95)

56. Creating empty files (touch)
57. Creating files with content (echo >)
58. Creating directories (mkdir)
59. Creating nested directories (mkdir -p)
60. Copying files (cp/copy)
61. Copying directories (cp -r)
62. Moving files (mv/move)
63. Renaming files (mv)
64. Deleting files (rm/del)
65. Deleting directories (rm -r/rmdir)
66. Force deletion (rm -f)
67. Interactive deletion (rm -i)
68. Safe deletion practices
69. Recovering deleted files (limitations)
70. File permissions concept (Unix)
71. Read permission
72. Write permission
73. Execute permission
74. Owner, group, others
75. Viewing permissions (ls -l)
76. Changing permissions (chmod)
77. Numeric permission notation
78. Symbolic permission notation
79. Changing ownership (chown)
80. Windows file attributes
81. Hidden files and folders
82. Read-only files
83. File timestamps
84. Modifying timestamps
85. File size checking
86. Disk usage (du)
87. Free disk space (df)
88. Symbolic links
89. Hard links
90. Creating links (ln)
91. Following links
92. File type identification
93. File extensions importance
94. Batch file operations
95. Wildcard introduction (*)

---

## Module 4: Viewing and Reading Files (Concepts 96-125)

96. Displaying file contents (cat/type)
97. Concatenating multiple files
98. Paging through files (less/more)
99. Less navigation commands
100. Searching within less
101. First lines of file (head)
102. Last lines of file (tail)
103. Specifying line count
104. Following file updates (tail -f)
105. Line numbering (cat -n/nl)
106. Word count (wc)
107. Character count
108. Line count
109. Byte count
110. Viewing binary files (xxd/hexdump)
111. File encoding (UTF-8, ASCII)
112. Handling different encodings
113. Viewing compressed files (zcat)
114. Comparing files (diff)
115. Side-by-side comparison
116. Unified diff format
117. Patch files concept
118. Checking file type (file command)
119. MIME types
120. Viewing file metadata
121. Extended attributes
122. Reading configuration files
123. Syntax highlighting in terminal
124. Pagers and their options
125. Opening files in default application

---

## Module 5: Searching and Finding (Concepts 126-165)

126. Finding files by name (find/dir /s)
127. Find command syntax
128. Searching by file type
129. Searching by size
130. Searching by time modified
131. Searching by permissions
132. Executing commands on found files
133. Combining find conditions
134. Excluding directories
135. Searching text in files (grep)
136. Case-insensitive search (grep -i)
137. Recursive search (grep -r)
138. Showing line numbers (grep -n)
139. Showing context lines (grep -B/-A/-C)
140. Inverting match (grep -v)
141. Counting matches (grep -c)
142. Showing only filenames (grep -l)
143. Regular expressions basics
144. Literal vs regex patterns
145. Anchors (^ and $)
146. Character classes
147. Quantifiers (*, +, ?)
148. Alternation (|)
149. Grouping
150. Extended regex (grep -E/egrep)
151. Fixed string search (grep -F/fgrep)
152. Searching command output
153. Combining grep with other commands
154. Ripgrep (rg) as modern alternative
155. Silver Searcher (ag)
156. Fuzzy finding (fzf)
157. Locate command and database
158. Updating locate database
159. Which vs whereis vs type
160. Searching in compressed files
161. Searching specific file types
162. Performance considerations
163. Building search patterns
164. Saving search results
165. Searching and replacing

---

## Module 6: Text Processing (Concepts 166-205)

166. Sorting lines (sort)
167. Numeric sort (sort -n)
168. Reverse sort (sort -r)
169. Sorting by column (sort -k)
170. Unique lines (sort -u)
171. Removing duplicates (uniq)
172. Counting duplicates (uniq -c)
173. Showing only duplicates (uniq -d)
174. Cutting columns (cut)
175. Cut by delimiter (cut -d)
176. Cut by character position
177. Joining files (join)
178. Pasting columns (paste)
179. Translating characters (tr)
180. Deleting characters (tr -d)
181. Squeezing repeats (tr -s)
182. Case conversion
183. Stream editor (sed) introduction
184. Sed substitution (s///)
185. Sed global replacement (g flag)
186. Sed in-place editing (-i)
187. Sed address ranges
188. Awk introduction
189. Awk field processing
190. Awk patterns and actions
191. Awk built-in variables
192. Awk arithmetic
193. Column manipulation with awk
194. Formatting output (printf)
195. Reversing lines (tac/rev)
196. Shuffling lines (shuf)
197. Splitting files (split)
198. Combining files (cat)
199. Converting line endings
200. Removing blank lines
201. Adding line numbers
202. Extracting data patterns
203. Transforming data formats
204. Text statistics
205. Character encoding conversion

---

## Module 7: Pipes and Redirection (Concepts 206-235)

206. Standard input (stdin)
207. Standard output (stdout)
208. Standard error (stderr)
209. Output redirection (>)
210. Append redirection (>>)
211. Input redirection (<)
212. Pipes concept (|)
213. Chaining commands with pipes
214. Pipeline efficiency
215. Redirecting stderr (2>)
216. Combining stdout and stderr (2>&1)
217. Discarding output (/dev/null, NUL)
218. Here documents (<<)
219. Here strings (<<<)
220. Tee command (split output)
221. Process substitution
222. Named pipes (FIFOs)
223. Building complex pipelines
224. Debugging pipelines
225. Pipeline exit status
226. Xargs for command building
227. Parallel execution with xargs
228. Limiting xargs arguments
229. Handling special characters in pipes
230. Pipeline performance
231. Buffering in pipes
232. Intermediary files vs pipes
233. Subshells in pipelines
234. Pipeline best practices
235. Common pipeline patterns

---

## Module 8: Environment and Configuration (Concepts 236-265)

236. Environment variables concept
237. Viewing all variables (env/set)
238. Viewing specific variable (echo $VAR)
239. Setting variables temporarily
240. Exporting variables
241. Common environment variables
242. PATH variable in detail
243. Adding to PATH
244. HOME variable
245. USER/USERNAME variable
246. Shell configuration files
247. .bashrc vs .bash_profile
248. .zshrc configuration
249. PowerShell profile
250. Aliases concept
251. Creating aliases
252. Persistent aliases
253. Alias best practices
254. Functions in shell
255. Simple shell functions
256. Functions vs aliases
257. Shell options
258. Setting shell options (set)
259. Startup vs login shells
260. Interactive vs non-interactive
261. Configuration inheritance
262. Per-directory configuration
263. Environment for scripts
264. Debugging configuration issues
265. Resetting configuration

---

## Module 9: Job Control and Processes (Concepts 266-295)

266. Process concept
267. Process ID (PID)
268. Viewing processes (ps)
269. Detailed process list (ps aux)
270. Process tree (pstree)
271. Interactive process viewer (top/htop)
272. Task manager equivalents
273. Foreground vs background
274. Running in background (&)
275. Moving to background (Ctrl+Z, bg)
276. Bringing to foreground (fg)
277. Job listing (jobs)
278. Terminating processes (kill)
279. Kill signals (SIGTERM, SIGKILL)
280. Killing by name (killall/pkill)
281. Process priority (nice/renice)
282. Suspending processes
283. Waiting for processes (wait)
284. Nohup for persistent processes
285. Disowning processes
286. Screen/tmux introduction
287. Session persistence
288. Detaching and reattaching
289. Resource monitoring
290. CPU usage
291. Memory usage
292. Disk I/O
293. Network connections (netstat/ss)
294. Process limits
295. Cron jobs introduction

---

## Module 10: Scripting Basics (Concepts 296-330)

296. What is a shell script
297. Shebang line (#!/bin/bash)
298. Script file creation
299. Making scripts executable
300. Running scripts
301. Script arguments ($1, $2)
302. All arguments ($@, $*)
303. Argument count ($#)
304. Exit status ($?)
305. Conditional execution (&&, ||)
306. If statements
307. Test conditions ([ ])
308. File test operators
309. String comparisons
310. Numeric comparisons
311. Else and elif
312. Case statements
313. For loops
314. While loops
315. Loop control (break, continue)
316. Reading user input
317. Reading from files
318. Writing output
319. Error handling
320. Script debugging (set -x)
321. Strict mode (set -e)
322. Comments in scripts
323. Script organization
324. Reusable functions
325. Script portability
326. Cross-platform considerations
327. PowerShell scripting basics
328. Batch file basics (Windows)
329. Script security
330. Best practices summary

---

## Module 11: Networking Commands (Concepts 331-360)

331. Network interface concept
332. IP addresses basics
333. Checking IP address (ip/ifconfig/ipconfig)
334. Hostname command
335. DNS resolution (nslookup/dig)
336. Testing connectivity (ping)
337. Traceroute/tracert
338. Checking open ports
339. Netstat usage
340. ss command (modern netstat)
341. Downloading files (curl)
342. Curl common options
343. Wget for downloads
344. HTTP methods with curl
345. Sending headers
346. Handling redirects
347. Saving output
348. Downloading multiple files
349. Resume interrupted downloads
350. SSH introduction
351. SSH connection basics
352. SSH key authentication
353. SCP for file transfer
354. SFTP usage
355. SSH tunneling basics
356. Remote command execution
357. SSH config file
358. Network troubleshooting workflow
359. Firewall basics (ufw/iptables)
360. Network monitoring tools

---

## Module 12: Advanced Topics (Concepts 361-380)

361. Command substitution $(...)
362. Arithmetic expansion $((...))
363. Brace expansion {a,b,c}
364. Sequence expansion {1..10}
365. Globbing patterns
366. Extended globbing
367. Quoting rules
368. Single vs double quotes
369. Escape characters
370. ANSI escape codes
371. Terminal colors
372. Progress indicators
373. Interactive prompts
374. Readline shortcuts
375. History expansion
376. Terminal multiplexers deep dive
377. Custom prompt (PS1)
378. Completions customization
379. Shell scripting patterns
380. Command line philosophy

---

## Concept Distribution by Level

- **Level 0 (Curious)**: Concepts 1-55 (55 concepts)
  - Terminal fundamentals and basic navigation

- **Level 1 (Explorer)**: Concepts 56-125 (70 concepts)
  - File operations and viewing files

- **Level 2 (Tinkerer)**: Concepts 126-205 (80 concepts)
  - Searching, finding, and text processing

- **Level 3 (Builder)**: Concepts 206-295 (90 concepts)
  - Pipes, redirection, environment, and processes

- **Level 4 (Maker)**: Concepts 296-380 (85 concepts)
  - Scripting, networking, and advanced topics

---

## Cross-Platform Notes

This subject covers both Unix-like (Bash/Zsh) and Windows (PowerShell/CMD) commands where applicable. Concepts marked with platform-specific commands will show equivalents for both environments.
