import json
import subprocess

def runCmd(cmd):
    status = subprocess.run(cmd, shell=True, executable="/bin/bash")
    if status.returncode == 0:
        print(f"\n\nSUCCESS: $ {cmd}\n")
        return True
    print(f"\n\nERROR: $ {cmd}\n")
    return False

def setUpSystem(setUpConfigNums, jsonData):
    try:
        for setUpConfigNum in setUpConfigNums:
            setUpConfigSteps = jsonData[setUpConfigNum]["steps"]

            for setUpConfig in setUpConfigSteps:
                if not runCmd(setUpConfig):
                    return False
        
    except:
        return False
