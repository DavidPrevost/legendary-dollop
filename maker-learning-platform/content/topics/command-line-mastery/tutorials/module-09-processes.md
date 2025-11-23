# Module 9: Job Control and Processes

**Concepts Covered**: 266-295
**Estimated Time**: 40-50 minutes

---

## What is a Process?

A process is a running program. Each has:
- **PID**: Process ID (unique number)
- **Owner**: User who started it
- **Resources**: Memory, CPU time

---

## Viewing Processes

### Basic List

```bash
ps
```

Shows your processes in current terminal.

### All User Processes

```bash
ps aux
```

Columns:
- USER: Owner
- PID: Process ID
- %CPU: CPU usage
- %MEM: Memory usage
- COMMAND: What's running

### Process Tree

```bash
pstree
ps auxf    # forest view
```

---

## Interactive Process Viewers

### top

```bash
top
```

Real-time view of processes. Commands:
- `q`: Quit
- `k`: Kill process
- `M`: Sort by memory
- `P`: Sort by CPU
- `h`: Help

### htop (Better top)

```bash
htop
```

More user-friendly, with colors and easier navigation.

---

## Foreground and Background

### Run in Background

```bash
long_command &
```

Returns prompt immediately.

### View Background Jobs

```bash
jobs
```

### Bring to Foreground

```bash
fg        # most recent job
fg %1     # job number 1
```

### Send to Background

1. Press `Ctrl + Z` (suspends current process)
2. Run `bg` (resumes in background)

---

## Stopping Processes

### Cancel Current Command

`Ctrl + C` - Sends SIGINT (interrupt)

### Suspend Current Command

`Ctrl + Z` - Sends SIGTSTP (stop)

Resume with `fg` or `bg`.

---

## Killing Processes

### By PID

```bash
kill 12345       # graceful termination (SIGTERM)
kill -9 12345    # force kill (SIGKILL)
```

### By Name

```bash
killall firefox
pkill firefox
```

### Kill Signals

| Signal | Number | Description |
|--------|--------|-------------|
| SIGTERM | 15 | Graceful termination (default) |
| SIGKILL | 9 | Force kill (cannot be ignored) |
| SIGHUP | 1 | Hang up |
| SIGINT | 2 | Interrupt (Ctrl+C) |

```bash
kill -15 12345    # same as kill 12345
kill -TERM 12345  # same thing
```

---

## Process Priority

### View Priority

In `ps` or `top`, look at NI (nice) column.
- Range: -20 (highest) to 19 (lowest)
- Default: 0

### Start with Priority

```bash
nice -n 10 command    # lower priority
```

### Change Running Process

```bash
renice 10 -p 12345    # lower priority
sudo renice -10 -p 12345  # higher priority (needs root)
```

---

## Persistent Processes

### nohup

Keep running after logout:

```bash
nohup long_command &
```

Output goes to `nohup.out`.

### disown

Remove from job table:

```bash
long_command &
disown
```

---

## Terminal Multiplexers

### screen

```bash
screen              # start session
# Ctrl+A, D         # detach
screen -r           # reattach
```

### tmux

```bash
tmux                # start session
# Ctrl+B, D         # detach
tmux attach         # reattach
```

These let you:
- Run processes that survive disconnection
- Have multiple windows/panes
- Share sessions

---

## Resource Monitoring

### CPU and Memory

```bash
top
htop
```

### Disk I/O

```bash
iotop      # requires root
iostat
```

### Network Connections

```bash
netstat -tuln    # listening ports
ss -tuln         # modern replacement
```

### Memory Details

```bash
free -h
cat /proc/meminfo
```

---

## Process Limits

View limits:
```bash
ulimit -a
```

Set limits:
```bash
ulimit -n 4096    # max open files
```

---

## Cron Jobs

Schedule recurring tasks.

### Edit Crontab

```bash
crontab -e
```

### Cron Format

```
* * * * * command
│ │ │ │ │
│ │ │ │ └── Day of week (0-7)
│ │ │ └──── Month (1-12)
│ │ └────── Day of month (1-31)
│ └──────── Hour (0-23)
└────────── Minute (0-59)
```

### Examples

```bash
# Every day at 2am
0 2 * * * /home/user/backup.sh

# Every hour
0 * * * * /home/user/check.sh

# Every 15 minutes
*/15 * * * * /home/user/task.sh

# Monday at 9am
0 9 * * 1 /home/user/weekly.sh
```

### List Cron Jobs

```bash
crontab -l
```

---

## Wait for Processes

### wait Command

```bash
command1 &
command2 &
wait    # wait for all background jobs
echo "All done"
```

### Wait for Specific PID

```bash
long_command &
PID=$!
wait $PID
echo "Process $PID finished"
```

---

## Practical Examples

### Find Memory Hogs

```bash
ps aux --sort=-%mem | head -10
```

### Find CPU Hogs

```bash
ps aux --sort=-%cpu | head -10
```

### Kill All by Name

```bash
pkill -f "python script.py"
```

### Monitor Specific Process

```bash
watch -n 1 "ps aux | grep firefox"
```

### Run Until Complete

```bash
nohup ./long_task.sh > task.log 2>&1 &
echo $!    # save PID
```

---

## Exercises

### Exercise 1: View Processes
```bash
# See your processes
ps

# See all with details
ps aux | head -20

# Interactive view
top    # press q to quit
```

### Exercise 2: Background Jobs
```bash
# Start background job
sleep 100 &

# View jobs
jobs

# Bring to foreground and cancel
fg
# Ctrl+C
```

### Exercise 3: Process Control
```bash
# Start process
sleep 300 &
PID=$!

# Check it's running
ps aux | grep $PID

# Kill it
kill $PID
```

### Exercise 4: Priorities
```bash
# Run with low priority
nice -n 10 sleep 60 &

# Check priority
ps -o pid,ni,comm
```

---

## Key Takeaways

1. `ps aux` shows all processes
2. `&` runs commands in background
3. `Ctrl+Z` suspends, `bg`/`fg` resumes
4. `kill` sends signals; `-9` forces termination
5. `nohup` and tmux for persistent processes
6. `crontab` schedules recurring tasks

---

## Next Module

In Module 10, you'll learn shell scripting - automating tasks with scripts.
