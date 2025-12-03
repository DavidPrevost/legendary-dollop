# Module 11: Networking Commands

**Concepts Covered**: 331-360
**Estimated Time**: 40-50 minutes

---

## Network Basics

### Check Your IP Address

Linux:
```bash
ip addr show
hostname -I
```

macOS:
```bash
ifconfig
```

Windows:
```cmd
ipconfig
```

### Hostname

```bash
hostname
```

---

## DNS Resolution

### nslookup

```bash
nslookup google.com
```

### dig (More Detailed)

```bash
dig google.com
dig google.com +short    # just the IP
dig google.com MX        # mail servers
```

---

## Testing Connectivity

### ping

```bash
ping google.com
ping -c 4 google.com    # 4 packets only
```

Windows:
```cmd
ping -n 4 google.com
```

### traceroute

Shows network path:

```bash
traceroute google.com
```

Windows:
```cmd
tracert google.com
```

---

## Port and Connection Info

### netstat

```bash
netstat -tuln           # listening ports
netstat -an             # all connections
```

### ss (Modern netstat)

```bash
ss -tuln                # listening ports
ss -tp                  # TCP with process names
```

### Check Specific Port

```bash
ss -tuln | grep :80
```

---

## Downloading Files

### curl

Versatile tool for transferring data.

#### Basic Download

```bash
curl https://example.com
curl -o file.html https://example.com    # save to file
curl -O https://example.com/file.zip     # keep filename
```

#### Follow Redirects

```bash
curl -L https://example.com
```

#### Show Headers

```bash
curl -I https://example.com    # headers only
curl -i https://example.com    # headers + body
```

#### Download with Progress

```bash
curl -# -O https://example.com/large.zip
```

#### Resume Download

```bash
curl -C - -O https://example.com/large.zip
```

---

### wget

Alternative downloader.

```bash
wget https://example.com/file.zip
wget -c https://example.com/file.zip    # resume
wget -r https://example.com             # recursive
```

---

## HTTP Methods with curl

### GET (Default)

```bash
curl https://api.example.com/users
```

### POST

```bash
curl -X POST -d "name=John" https://api.example.com/users
```

### JSON POST

```bash
curl -X POST \
    -H "Content-Type: application/json" \
    -d '{"name": "John"}' \
    https://api.example.com/users
```

### PUT

```bash
curl -X PUT -d "name=Jane" https://api.example.com/users/1
```

### DELETE

```bash
curl -X DELETE https://api.example.com/users/1
```

---

## SSH - Secure Shell

### Basic Connection

```bash
ssh user@hostname
ssh user@192.168.1.100
```

### Specify Port

```bash
ssh -p 2222 user@hostname
```

### Run Command Remotely

```bash
ssh user@hostname "ls -la"
```

---

## SSH Key Authentication

More secure than passwords.

### Generate Key Pair

```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
```

Creates:
- `~/.ssh/id_ed25519` (private key - keep secret!)
- `~/.ssh/id_ed25519.pub` (public key - share this)

### Copy to Server

```bash
ssh-copy-id user@hostname
```

Or manually add public key to server's `~/.ssh/authorized_keys`.

### Connect with Key

```bash
ssh -i ~/.ssh/id_ed25519 user@hostname
```

---

## File Transfer

### SCP (Secure Copy)

```bash
# Upload
scp file.txt user@hostname:/path/

# Download
scp user@hostname:/path/file.txt ./

# Directory
scp -r folder/ user@hostname:/path/
```

### SFTP

Interactive file transfer:

```bash
sftp user@hostname
```

Commands:
- `ls`, `cd`: Browse remote
- `lls`, `lcd`: Browse local
- `get file`: Download
- `put file`: Upload
- `quit`: Exit

---

## SSH Config

Simplify connections with `~/.ssh/config`:

```
Host myserver
    HostName 192.168.1.100
    User admin
    Port 2222
    IdentityFile ~/.ssh/id_ed25519

Host dev
    HostName dev.example.com
    User developer
```

Now connect with:
```bash
ssh myserver
ssh dev
```

---

## SSH Tunneling

### Local Port Forward

Access remote service locally:

```bash
ssh -L 8080:localhost:80 user@hostname
```

Now `localhost:8080` connects to remote port 80.

### Remote Port Forward

Expose local service to remote:

```bash
ssh -R 8080:localhost:3000 user@hostname
```

---

## Network Troubleshooting

### Workflow

1. **Check local interface**: `ip addr` / `ifconfig`
2. **Ping gateway**: `ping 192.168.1.1`
3. **Ping external**: `ping 8.8.8.8`
4. **DNS resolution**: `dig google.com`
5. **Trace route**: `traceroute google.com`

### Common Issues

- No IP: DHCP issue
- Can't ping gateway: Network config
- Can't ping 8.8.8.8: Routing issue
- DNS fails: DNS server issue

---

## Practical Examples

### Check if Port is Open

```bash
curl -s -o /dev/null -w "%{http_code}" http://localhost:8080
```

### Download and Extract

```bash
curl -L https://example.com/app.tar.gz | tar xzf -
```

### API Testing

```bash
curl -s https://api.github.com/users/octocat | jq .name
```

### Multiple File Download

```bash
curl -O https://example.com/[1-10].jpg
```

---

## Exercises

### Exercise 1: Basic Networking
```bash
# Check your IP
ip addr show | grep inet

# Ping test
ping -c 3 google.com

# DNS lookup
dig google.com +short
```

### Exercise 2: curl Practice
```bash
# Download page
curl -o google.html https://google.com

# Check headers
curl -I https://httpbin.org/get

# POST data
curl -X POST -d "test=data" https://httpbin.org/post
```

### Exercise 3: SSH (if available)
```bash
# Generate key
ssh-keygen -t ed25519

# View public key
cat ~/.ssh/id_ed25519.pub
```

### Exercise 4: Port Checking
```bash
# List listening ports
ss -tuln

# Check specific port
ss -tuln | grep :22
```

---

## Key Takeaways

1. `ping` and `traceroute` for connectivity testing
2. `curl` for downloading and API calls
3. `ssh` for secure remote access
4. Use SSH keys instead of passwords
5. `scp` or `sftp` for file transfer
6. `~/.ssh/config` for connection shortcuts

---

## Next Module

In Module 12, you'll learn advanced topics - command substitution, expansions, and terminal customization.
