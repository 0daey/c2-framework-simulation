# main.py
import sys
import os

# Add current directory to path
base_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(base_dir)

from server.handler import Handler
from agent.agent import C2Agent

def main():
    if len(sys.argv) < 2:
        print("C2 Framework Launcher")
        print("Usage: python main.py [server|agent]")
        return

    role = sys.argv[1].lower()
    if role == "server":
        print("[*] Starting C2 Server...")
        handler = Handler("0.0.0.0", 8080)
        handler.start()
    elif role == "agent":
        print("[*] Starting C2 Agent...")
        agent = C2Agent("localhost", 8080)
        if agent.connect():
            agent.run()
    else:
        print(f"[!] Invalid role: {role}. Use 'server' or 'agent'.")

if __name__ == "__main__":
    main()
