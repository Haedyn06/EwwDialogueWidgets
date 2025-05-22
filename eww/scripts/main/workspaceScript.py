#!/usr/bin/env python3
import subprocess
import re

clientOut = subprocess.check_output(["hyprctl", "clients"], text=True).splitlines()

def appList(workspacenum, app):
    appWorkspace = []
    for i, line in enumerate(clientOut):
        if re.search(fr"workspace: {workspacenum} ", line):
            for j in range(i, min(i + 8, len(clientOut))):
                if "class:" in clientOut[j]:
                    appClass = clientOut[j].split(":")[1].strip()
                    appWorkspace.append(appClass)
    print(f"Apps in workspace {workspacenum}: {', '.join(appWorkspace) if appWorkspace else 'None'}")
    if app in appWorkspace:
        print("Over Here")
        return True
    else:
        print("Not here")
        return False


def findApp(ApptoOpen):
    for i in range(1, 11):
        check = appList(i, ApptoOpen)

        if check == True:
            subprocess.run(["hyprctl", "dispatch", "workspace", str(i)])
            return True
        else:
            continue
    return False

def openApp(ApptoOpen):
    if findApp(ApptoOpen):
        print(f"{ApptoOpen} found in workspace")    
    else:
        print(f"{ApptoOpen} not found in any workspace")    
        subprocess.Popen(ApptoOpen.lower(), shell=True)



if __name__ == "__main__":
    openApp("Spotify")
