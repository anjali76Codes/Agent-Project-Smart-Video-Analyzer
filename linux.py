import subprocess
import os
import platform

# Function to handle shell command execution based on OS
def run_command(command):
    system_platform = platform.system().lower()
    
    if system_platform == "windows":
        # Windows-specific command handling
        try:
            if command.strip().lower() == "pwd":
                return os.getcwd()
            elif command.strip().lower().startswith("mkdir "):
                dir_name = command.strip().split("mkdir ", 1)[1]
                os.makedirs(dir_name, exist_ok=True) 
                return f"Directory '{dir_name}' created successfully."
            elif command.strip().lower().startswith("touch "):
                file_name = command.strip().split("touch ", 1)[1]
                with open(file_name, 'w') as f:
                    pass  # Create empty file
                return f"File '{file_name}' created successfully."
            elif command.strip().lower().startswith("del "):
                file_name = command.strip().split("del ", 1)[1]
                os.remove(file_name)
                return f"File '{file_name}' deleted successfully."
            elif command.strip().lower().startswith("copy "):
                args = command.strip().split("copy ", 1)[1]
                return subprocess.getoutput(f"copy {args}")
            elif command.strip().lower() == "dir":
                return subprocess.getoutput("dir")
            elif command.strip().lower() == "cls":
                # Clear the terminal screen on Windows
                subprocess.run("cls", shell=True)
                return "Terminal screen cleared."
            elif command.strip().lower().startswith("echo "):
                text = command.strip().split("echo ", 1)[1]
                return text
            elif command.strip().lower() == "tasklist":
                return subprocess.getoutput("tasklist")
            elif command.strip().lower() == "systeminfo":
                return subprocess.getoutput("systeminfo")
            elif command.strip().lower() == "ipconfig":
                return subprocess.getoutput("ipconfig")
            elif command.strip().lower().startswith("ping "):
                address = command.strip().split("ping ", 1)[1]
                return subprocess.getoutput(f"ping {address}")
            elif command.strip().lower() == "shutdown":
                return subprocess.getoutput("shutdown /s /f /t 0")
            elif command.strip().lower() == "chkdsk":
                return subprocess.getoutput("chkdsk")
            elif command.strip().lower() == "sfc /scannow":
                return subprocess.getoutput("sfc /scannow")
            elif command.strip().lower() == "get-process":
                return subprocess.getoutput("powershell Get-Process")
            elif command.strip().lower().startswith("rmdir "):
                dir_name = command.strip().split("rmdir ", 1)[1]
                return subprocess.getoutput(f"rmdir {dir_name}")
            else:
                return subprocess.getoutput(command)
        except Exception as e:
            return f"Error executing command on Windows: {str(e)}"
    
    else:
        # Unix/Linux (or macOS) systems
        try:
            if command.strip().lower() == "pwd":
                return subprocess.getoutput("pwd")
            elif command.strip().lower().startswith("mkdir "):
                dir_name = command.strip().split("mkdir ", 1)[1]
                return subprocess.getoutput(f"mkdir -p {dir_name}")
            elif command.strip().lower().startswith("touch "):
                file_name = command.strip().split("touch ", 1)[1]
                return subprocess.getoutput(f"touch {file_name}")
            elif command.strip().lower().startswith("rm "):
                file_name = command.strip().split("rm ", 1)[1]
                return subprocess.getoutput(f"rm {file_name}")
            elif command.strip().lower().startswith("cp "):
                args = command.strip().split("cp ", 1)[1]
                return subprocess.getoutput(f"cp {args}")
            elif command.strip().lower() == "ls":
                return subprocess.getoutput("ls -l")
            elif command.strip().lower().startswith("rmdir "):
                dir_name = command.strip().split("rmdir ", 1)[1]
                return subprocess.getoutput(f"rmdir {dir_name}")
            elif command.strip().lower().startswith("echo "):
                text = command.strip().split("echo ", 1)[1]
                return subprocess.getoutput(f"echo {text}")
            elif command.strip().lower() == "date":
                return subprocess.getoutput("date")
            elif command.strip().lower() == "top":
                return subprocess.getoutput("top -n 1")
            elif command.strip().lower() == "df":
                return subprocess.getoutput("df -h")
            elif command.strip().lower() == "free":
                return subprocess.getoutput("free -h")
            elif command.strip().lower() == "ps":
                return subprocess.getoutput("ps aux")
            elif command.strip().lower() == "ifconfig":
                return subprocess.getoutput("ifconfig")
            elif command.strip().lower().startswith("ping "):
                address = command.strip().split("ping ", 1)[1]
                return subprocess.getoutput(f"ping {address}")
            elif command.strip().lower() == "shutdown":
                return subprocess.getoutput("shutdown -h now")
            elif command.strip().lower() == "uname -a":
                return subprocess.getoutput("uname -a")
            elif command.strip().lower() == "htop":
                return subprocess.getoutput("htop")
            elif command.strip().lower().startswith("tar -czvf "):
                args = command.strip().split("tar -czvf ", 1)[1]
                return subprocess.getoutput(f"tar -czvf {args}")
            elif command.strip().lower().startswith("mv "):
                args = command.strip().split("mv ", 1)[1]
                return subprocess.getoutput(f"mv {args}")
            elif command.strip().lower() == "clear":
                return subprocess.getoutput("clear")
            else:
                return subprocess.getoutput(command)
        except Exception as e:
            return f"Error executing command on Unix-based system: {str(e)}"

# Streamlit UI setup
import streamlit as st

st.title("Linux & Windows Shell with Phi + Streamlit")

# Command input from user
user_input = st.text_input("Enter a Linux or Windows command:")

if st.button("Run Command"):
    if user_input.strip() == "":
        st.warning("Please enter a command.")
    else:
        with st.spinner("Running command..."):
            result = run_command(user_input.strip())
            if result:
                st.subheader("Output:")
                st.code(result, language="bash")  # Display the output in terminal-like format
            else:
                st.error("Error in executing the command.")
