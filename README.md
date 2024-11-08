# Reverse Shell Python Application

This project contains a **Reverse Shell** application written in Python. The application consists of two components:
1. **Client (reverse shell)**: The Python script running on the target machine, which connects back to the attacker's server and executes received commands.
2. **Server**: A Python server that listens for incoming connections and sends commands to the client for execution.

This is typically used for educational purposes, penetration testing, or ethical hacking in a controlled environment with permission.

## Features

- **Reverse Shell**: The client connects back to the server and executes commands on the target machine.
- **Command Execution**: The server sends shell commands, which are executed on the client machine.
- **Directory Change**: The client can change directories using the `cd` command.
- **Command Output**: The server receives and displays the standard output and error from executed commands.

## Requirements

- Python 3.x
- Basic knowledge of networking and socket programming.
  
## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/reverse-shell.git
    cd reverse-shell
    ```

2. No additional dependencies are required since the script uses only standard Python libraries (`socket`, `subprocess`, and `os`).

## Usage

### **Setting Up the Server**

1. **Edit the Server Script:**
   - Modify the `SERVER_IP` and `SERVER_PORT` in the server script (`server.py`) to match your server's IP address and the port you want to listen on.
     - **Example:**
       ```python
       SERVER_IP = '0.0.0.0'  # Listen on all interfaces
       SERVER_PORT = 4444     # Choose a port to listen on
       ```

2. **Run the Server Script:**
   ```bash
   python server.py
