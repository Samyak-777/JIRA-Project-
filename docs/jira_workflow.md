# Client-Server Socket Programming Assignment
A comprehensive implementation of client-server socket programming demonstrating multiple server architectures for arithmetic calculator functionality using TCP/IPv4 protocols.

##  Overview

This project implements a client-server system where clients can send arithmetic expressions to servers for evaluation. The assignment demonstrates four different server architectures:

1. **Single-client sequential server** (server1.py)
2. **Multi-threaded concurrent server** (server2.py)  
3. **Select-based multiplexing server** (server3.py)
4. **Echo server with select** (server4.py)

All servers communicate using TCP sockets with IPv4 addressing and provide real-time arithmetic calculation services.

##  Features

### Core Functionality
- ✅ TCP/IPv4 socket communication
- ✅ Arithmetic expression evaluation (+, -, *, /)
- ✅ Multiple server architectures
- ✅ Real-time client-server interaction
- ✅ Command-line interface
- ✅ Graceful error handling

##  Architecture

```
Client ←→ Server Communication Flow

1. Server starts listening on specified IP:PORT
2. Client connects to server
3. Client sends arithmetic expression
4. Server evaluates and returns result
5. Process repeats until client disconnects
```

### Server Types Comparison

| Server | Architecture | Concurrency | Use Case |
|--------|-------------|-------------|----------|
| Server1 | Single Process | Sequential | Simple, resource-limited |
| Server2 | Multi-threaded | Parallel | Medium load, thread-safe |
| Server3 | Select-based | Multiplexed | High concurrency, efficient |
| Server4 | Select + Echo | Multiplexed | Testing, demonstration |

##  File Structure

```
socket-programming-assignment/
├── client.py              # Client application
├── server1.py            # Single-client server
├── server2.py            # Multi-threaded server
├── server3.py            # Select-based calculator server
├── server4.py            # Select-based echo server
└── BT23CSE028_report.pdf/
    ├── screenshots/      # Test output screenshots
    └── overview      # Comprehensive assignment report
```


##  Running

### Download
```bash
# Download ZIP and extract
cd socket-programming-assignment
```

## Quick Start

1. **Start a Server** (choose one):
```bash
# Single-client server
python server1.py 127.0.0.1 5001

# Multi-threaded server
python server2.py 127.0.0.1 5002

# Select-based calculator
python server3.py 127.0.0.1 5003

# Echo server
python server4.py 127.0.0.1 5004
```

2. **Connect Client(s)**:
```bash
# In a new terminal
python client.py 127.0.0.1 5001
```

3. **Test Calculations**:
```
Please enter the message to the server: 22 + 44
Server replied: 66

Please enter the message to the server: 10 / 2
Server replied: 5

Please enter the message to the server: 3.5 * 2
Server replied: 7
```

### Command Line Arguments

**Server Syntax:**
```bash
python serverX.py <IP_ADDRESS> <PORT>
```

**Client Syntax:**
```bash
python client.py <SERVER_IP> <SERVER_PORT>
```

**Examples:**
```bash
# Local testing
python server1.py 127.0.0.1 5000
python client.py 127.0.0.1 5000

# Network testing
python server2.py 192.168.1.100 8080
python client.py 192.168.1.100 8080
```

## 🧪 Test Cases

### Basic Arithmetic Operations

| Input | Expected Output | Status |
|-------|----------------|--------|
| `9 + 8` | `17` | ✅ Pass |
| `22 + 44` | `66` | ✅ Pass |
| `15 - 5` | `10` | ✅ Pass |
| `4 * 7` | `28` | ✅ Pass |
| `10 / 2` | `5` | ✅ Pass |
| `3.5 + 2.1` | `5.6` | ✅ Pass |

### Error Handling

| Input | Expected Output | Status |
|-------|----------------|--------|
| `10 / 0` | `Error: Division by zero` | ✅ Pass |
| `abc + def` | `Error: Invalid expression format` | ✅ Pass |
| `5 +` | `Error: Invalid expression format` | ✅ Pass |
| `* 3` | `Error: Invalid expression format` | ✅ Pass |

### Concurrency Testing

| Test | Server1 | Server2 | Server3 | Server4 |
|------|---------|---------|---------|---------|
| Single Client | ✅ | ✅ | ✅ | ✅ |
| Multiple Clients | ❌ (By design) | ✅ | ✅ | ✅ |
| Concurrent Operations | ❌ | ✅ | ✅ | ✅ |

##  Server Architectures

### Server1: Sequential Single-Client
```python
# Handles one client at a time
while True:
    client, addr = server_socket.accept()
    handle_client(client)  # Blocks until client disconnects
```

**Characteristics:**
- Simple implementation
- Low resource usage
- Sequential client processing
- Second client gets connection error

### Server2: Multi-threaded
```python
# Creates thread per client
while True:
    client, addr = server_socket.accept()
    thread = threading.Thread(target=handle_client, args=(client,))
    thread.start()
```

**Characteristics:**
- Concurrent client handling
- Thread-per-client model
- Higher resource usage
- True parallelism

### Server3: Select-based Multiplexing
```python
# Single process, multiple clients
ready_sockets, _, _ = select.select(socket_list, [], [])
for socket in ready_sockets:
    if socket == server_socket:
        # New connection
    else:
        # Handle existing client
```

**Characteristics:**
- Event-driven architecture
- Single process
- Efficient resource utilization
- Scalable to many connections

### Server4: Echo Server
```python
# Echoes messages back to clients
message = client_socket.recv(1024)
echo_response = f"Echo: {message.decode()}"
client_socket.send(echo_response.encode())
```

**Characteristics:**
- Demonstrates select() usage
- Simple echo functionality
- Multiple client support
- Testing/debugging tool

##  Special Features

### 1. Advanced Error Handling
```python
def evaluate_expression(expression):
    try:
        pattern = r'^(\d+(?:\.\d+)?)\s*([+\-*/])\s*(\d+(?:\.\d+)?)$'
        match = re.match(pattern, expression)
        
        if not match:
            return "Error: Invalid expression format"
        
        # Safe evaluation without eval()
        # Division by zero checking
        # ... more validation
```

### 2. Socket Resource Management
```python
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

try:
    # Server operations
finally:
    server_socket.close()  # Guaranteed cleanup
```

### 3. Professional Logging
```python
print(f"Connected with client {client_address} socket number {client_socket.fileno()}")
print(f"Client socket {client_socket.fileno()} sent message: {message}")
print(f"Sending reply: {result}")
```

### 4. Cross-platform Compatibility
- Windows: Full support with proper error codes
- Linux: Native select() support
- macOS: BSD socket implementation

##  Troubleshooting

### Common Issues

#### "Address already in use" Error
**Problem:** Port is occupied by previous process
**Solution:**
```bash
# Windows
netstat -ano | findstr :5000
taskkill /PID <PID> /F

# Linux/macOS  
lsof -i :5000
kill -9 <PID>

# Alternative: Use different port
python server1.py 127.0.0.1 5001
```

#### Connection Refused
**Problem:** Server not running or wrong IP/port
**Solution:**
- Verify server is running
- Check IP address and port number
- Ensure firewall allows connections
- Try localhost (127.0.0.1) for local testing

#### Client Hangs/No Response
**Problem:** Server crashed or network issue
**Solution:**
- Restart server
- Check server terminal for error messages
- Use Ctrl+C to terminate and restart
- Verify network connectivity


##  Screenshots

### Server1 Output

### Client Output

### Multi-client Testing (Server2)
```
$ python server2.py 127.0.0.1 5002
Server2 (Multi-threaded) started on 127.0.0.1:5002
Server2 listening for connections...
Connected with client ('127.0.0.1', 54322) socket number 5
Connected with client ('127.0.0.1', 54323) socket number 6
Client socket 5 sent message: 10 + 20
Client socket 6 sent message: 5 * 6
Sending reply to socket 5: 30
Sending reply to socket 6: 30
```

### Error Handling Example
```
Please enter the message to the server: 10 / 0
Server replied: Error: Division by zero

Please enter the message to the server: hello world
Server replied: Error: Invalid expression format. Use: number operator number
```

