import subprocess

def commands_install():
    apps = input("What packages do you want installed? Type them with lowercase letter and check the AUR\nif it's available")
    subprocess.call('sudo', 'pacman', '-S', apps, shell=True)