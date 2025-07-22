import os
import sys
import subprocess
import musiccmd
import re


#################
### VARIABLES ###
#################

usrInp = " ".join(sys.argv[1:]).strip()
lowusrInp = " ".join(sys.argv[1:]).strip().lower()
lowinp = usrInp.lower()
# lowusrInp = usrInp.strip().lower()
lowsplitInp = lowusrInp.split()


openCode = {
    "/home/haedyn06/.config/hypr/": ["hypr", "hyp", "hyper"],
    "/home/haedyn06/.config/rofi/dotThemes": ["rofi"],
    "/home/haedyn06/.config/waybar/": ["waybar"],
    "/home/haedyn06/.config/eww/": ["eww"],
    "/home/haedyn06/.config/swaync/": ["notify"],
    "/usr/share/sddm/": ["login"],
    "/home/haedyn06/Programs/CorePrograms/SystemPrograms/": ["systemcore"],
    "/home/haedyn06/Programs/CorePrograms/notTesting/": ["nottesting"],
    "/home/haedyn06/Programs/CorePrograms/Extensions/": ["systemext"]
}
codePaths = {codes: f"{key}" for key, values in openCode.items() for codes in values}

goApps = {
    "Obsidian": ["notes", "note"],
    "Dolphin": ["file", "dolphin"],
    "Spotify": ["music", "spotify", "listen", "song"],
    "Gimp": ["art", "edit", "gimp", "draw"],
    "Teams": ["team", "teams", "work", "meeting"],
    "Virutalbox": ["vbox", "vm", "virtual", "emulate"],
    "Discord": ["discord", "chat", "message", "contact"],
}
appPaths = {apps: f"{key}" for key, values in goApps.items() for apps in values}

openApps = {
    "chromium": ["browser", "web", "chrome", "google"],
    "firefox": ["firefox", "web2"],
    "alacritty": ["terminal", "alacritty", "term", "cmd"],
    "code": ["code", "vs", "vscode", "coding"]
}
applicationsPaths = {application: f"{key}" for key, values in openApps.items() for application in values}

###############
### METHODS ###
###############



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


##################
### EXECUTIONS ###
##################

if usrInp:
    print(lowsplitInp)

    #Music Controls
    match lowinp:
        case "play" | "stop":
            musiccmd.togglePlay()
        case "repeat":
            musiccmd.repeatTrack()
        case "next":
            musiccmd.nextTrack()
        case "loop":
            musiccmd.toggleLoop()
        case "shuffle":
            musiccmd.toggleShuffle()
        case _:
            if lowinp in codePaths:
                path = os.path.expanduser(codePaths[lowinp])
                subprocess.run(["code", path])
            elif lowinp in appPaths:
                openApp(appPaths[lowinp])
            elif lowinp in applicationsPaths:
                subprocess.run(applicationsPaths[lowinp])
            else:
                try:
                    subprocess.run(usrInp, shell=True, check=True)
                except subprocess.CalledProcessError as e:
                    subprocess.run(["notify-send", "*Error", "Invalid Request"])

    subprocess.run(["eww", "close", "cmdBar"])





# import musiccmd  # ✅ Now it should work

# musiccmd
# import sys
# import os
# script_dir = os.path.dirname(os.path.abspath(__file__))
# sys.path.append(script_dir)
# sys.path.append(os.path.abspath(os.path.join(script_dir, "..")))