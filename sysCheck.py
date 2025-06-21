import platform
import os
import subprocess


def checkIfNotRootUser():
    res = subprocess.run("whoami", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, executable="/bin/bash")
    if(res.stdout.decode("ASCII").strip() == "root"):
        print("ERROR: user is a root user")
        return False
    print("SUCCESS: User is not a root user")
    return True

def checkOsNameAndArch():
    file = open("/etc/os-release", "r")
    osName = file.readlines(1)[0]
    file.close()
    if "Arch Linux" not in osName:
        print("WARNING: OS is not Arch Linux. All Steps may not work")
        return True
    if "x86_64" not in platform.machine():
        print("ERROR: architechture is not x86_64")
        return False
    print("SUCCESS: OS is Arch Linux and arch is: x86_64")
    return True


def deCheck():
    if(os.environ.get("XDG_CURRENT_DESKTOP") != "KDE"):
        print("ERROR: Desktop Environment is not KDE Plasma")
        return False
    print("SUCCESS: Detected KDE Plasma DE")
    return True


def totalCheck():
    if(checkIfNotRootUser() and checkOsNameAndArch() and deCheck()):
        print("Success: System is ready for post install")
        return True
    print("ERROR: System is not applicable for post install")
    return False
