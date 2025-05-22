#!/usr/bin/env python3
import subprocess
import json
import sys

# Default player (Spotify)
player = "spotify"
# image_path = os.path.expanduser("~/.cache/spotify_album.jpg")

if len(sys.argv) > 2 and sys.argv[1] == "--player":
    player = sys.argv[2]


def get_music_info():
    try:
        artist = subprocess.check_output(
            ["playerctl", "-p", player, "metadata", "xesam:artist"],
            stderr=subprocess.DEVNULL
        ).decode("utf-8").strip()

        title = subprocess.check_output(
            ["playerctl", "-p", player, "metadata", "xesam:title"],
            stderr=subprocess.DEVNULL
        ).decode("utf-8").strip()

        return f"{artist} - {title}"
    except subprocess.CalledProcessError:
        return "- - - - - -"

def get_status():
    try:
        status = subprocess.check_output(
            ["playerctl", "-p", "spotify", "status"], stderr=subprocess.DEVNULL
        ).decode("utf-8").strip()
        return status
    except subprocess.CalledProcessError:
        return "- - - - -"


def get_progress():
    try:

        position = float(subprocess.check_output(
            ["playerctl", "-p", "spotify", "position"], stderr=subprocess.DEVNULL
        ).decode("utf-8").strip())  
        length = int(subprocess.check_output(
            ["playerctl", "-p", "spotify", "metadata", "mpris:length"], stderr=subprocess.DEVNULL
        ).decode("utf-8").strip()) // 1000000 


        progress_percent = int((position / length) * 100)
        return progress_percent  
    except (subprocess.CalledProcessError, ValueError, ZeroDivisionError):
        return 0  

def get_text_progress_bar(bar_length=25):
    try:

        position = float(subprocess.check_output(
            ["playerctl", "-p", "spotify", "position"], stderr=subprocess.DEVNULL
        ).decode("utf-8").strip())

        length = int(subprocess.check_output(
            ["playerctl", "-p", "spotify", "metadata", "mpris:length"], stderr=subprocess.DEVNULL
        ).decode("utf-8").strip()) // 1000000

        progress = int((position / length) * bar_length)
        

        bar = "█" * progress + "░" * (bar_length - progress)
        
        # Format time in MM:SS
        minutes = int(position) // 60
        seconds = int(position) % 60
        total_minutes = int(length) // 60
        total_seconds = int(length) % 60
        time_display = f"\n{minutes:02}:{seconds:02} / {total_minutes:02}:{total_seconds:02}"

        return f"{bar} {time_display}"  # Final output
    except (subprocess.CalledProcessError, ValueError, ZeroDivisionError):
        return "- - - - - - - - - - - - - - - - - - -"

# def get_spotify_album_art():
#     try:
#         # Run playerctl command to get album art URL
#         result = subprocess.run(
#             ["playerctl", "-p", "spotify", "metadata", "mpris:artUrl"],
#             capture_output=True, text=True, check=True
#         )
#         url = result.stdout.strip()

#         # If the URL is valid, download the album art
#         if url.startswith("http"):
#             response = requests.get(url, stream=True)
#             if response.status_code == 200:
#                 with open(image_path, "wb") as f:
#                     for chunk in response.iter_content(1024):
#                         f.write(chunk)

#         # Print image path for EWW
#         print(image_path)

#     except subprocess.CalledProcessError:
#         print("")


if __name__ == "__main__":
    arg = sys.argv[1] if len(sys.argv) > 1 else None

    if arg == "--musicInf":
        print(get_music_info())

    elif arg == "--musicStat":
        status = get_status()
        if status == "Playing":
            print("❚❚")
        else:
            print("▶")
    
    elif arg == "--musicBar":
        # print(get_progress())
        print(get_text_progress_bar())