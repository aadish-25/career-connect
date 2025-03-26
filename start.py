import subprocess
import os
import webbrowser
import threading

# Define the backend directory
backend_dir = os.path.join(os.getcwd(), "Back-end")

# Function to run scripts
def run_scripts():
    subprocess.run(["python", os.path.join(backend_dir, "finalScore.py")], check=True)
    subprocess.run(["python", os.path.join(backend_dir, "exel_to_json.py")], check=True)

# Run scripts and open the frontend
def start():
    try:
        run_scripts()
        webbrowser.open("http://127.0.0.1:5500/Front-end/index.html")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    start()
