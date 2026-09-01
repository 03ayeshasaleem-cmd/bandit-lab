import subprocess

def run_command(command):
    subprocess.run(["ls", "-la"], check=True)
