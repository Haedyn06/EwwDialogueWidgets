import subprocess
import sys
import re

def getVolume():
    """Returns the current system volume as a percentage (PulseAudio)"""
    output = subprocess.check_output(["pactl", "get-sink-volume", "@DEFAULT_SINK@"]).decode()
    match = re.search(r"(\d+)%", output)
    return int(match.group(1)) if match else None

def volState():
    val = getVolume()
    if val is None:
        print("--")
        return

    if val > 60:
        return f"󰕾  {val}%"  # High volume
    elif val < 40 and val > 0:
        return f"🔈 {val}%"  # Low volume
    elif val == 0:
        return f"󰖁  {val}%"  # Muted
    else:
        return f"󰖀  {val}%"  # Medium volume


if __name__ == "__main__":

    arg = sys.argv[1] if len(sys.argv) > 1 else None

    if arg == "--volformat":
        print(volState())
    elif arg == "--volVal":
        print(getVolume())

