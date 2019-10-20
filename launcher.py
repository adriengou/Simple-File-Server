import os

python_path = os.path.join(os.getcwd(), "venv\\Scripts\\python.exe")
script_path = os.path.join(os.getcwd(), "simple_file_server.py")
command = f"{python_path} {script_path}"
os.system(command)