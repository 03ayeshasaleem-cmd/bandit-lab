import subprocess


def show_directory():
    subprocess.run(["ls", "-la"], check=True)


show_directory()
