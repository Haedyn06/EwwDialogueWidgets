import subprocess

def togglePlay():
    subprocess.run(["playerctl", "-p", "spotify", "play-pause"])

def nextTrack():
    subprocess.run(["playerctl", "next"])

def repeatTrack():
    subprocess.run(["playerctl", "previous"])

def toggleLoop():
    loop_status = subprocess.run(["playerctl", "loop"], capture_output=True, text=True).stdout.strip()
    new_loop = "None" if loop_status == "Playlist" else "Playlist"
    subprocess.run(["playerctl", "loop", new_loop])

def toggleShuffle():
    shuffle_status = subprocess.run(["playerctl", "shuffle"], capture_output=True, text=True).stdout.strip()
    new_shuffle = "off" if shuffle_status == "on" else "on"
    subprocess.run(["playerctl", "shuffle", new_shuffle])

def setVolume(level):
    subprocess.run(["playerctl", "volume", str(level)])