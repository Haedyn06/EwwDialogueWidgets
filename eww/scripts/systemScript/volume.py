import subprocess
import sys
import re

def setVol(value):
    """Set system volume to a specific percentage"""
    subprocess.run(["pactl", "set-sink-volume", "@DEFAULT_SINK@", f"{value}%"], check=True)

if len(sys.argv) > 1:
    val = int(sys.argv[1].strip()) 
    setVol(val) 
    volState()
else:
    raise ValueError("No volume value provided")


