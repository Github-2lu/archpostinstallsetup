import sysCheck
import installer
import json

setUpFileLoc = "reqSteps.json"

def createInstallerDict(jsonData):
    installerDict = {}
    for installerNum in jsonData:
        installerDict[installerNum] = jsonData[installerNum]["name"]

    return installerDict

def displayerInstallerDict(installerDict):
    for installerNum in installerDict:
        print(f"{installerNum} : {installerDict[installerNum]}")

def checkInputNums(installerNums, jsonData):
    if(installerNums == "0"):
        # install all softwares
        return jsonData.keys()
    else:
        installerNumsArr = installerNums.strip().split(" ")

        for installerNum in installerNumsArr:
            if installerNum not in jsonData:
                print(f"ERROR: Wrong Input: {installerNum}")
                return []
        
        return installerNumsArr

def confirmInstall(jsonData, installerNumsArr):
    print("\nFollowing packages will be installed")
    for installerNum in installerNumsArr:
        print(f"{installerNum} : {jsonData[installerNum]["name"]}")
    ans = input('''\n\n Do you want to continue.....[y/n]: ''')

    if ans.lower() == "y":
        return True
    return False

if __name__ == '__main__':    
    print("######## This is a post install setup file for arch linux ##################")

    if(sysCheck.totalCheck()):
        with open(setUpFileLoc, "r") as file:
            jsonData = json.load(file)

        installerDict = createInstallerDict(jsonData)
        displayerInstallerDict(installerDict)

        installerNums = input("\n\nEnter the numbers with space which part you want to setUp and then press Enter:   ")

        installerNumsArr = checkInputNums(installerNums, jsonData)

        if(confirmInstall(jsonData, installerNumsArr)):
            installer.setUpSystem(installerNumsArr, jsonData)