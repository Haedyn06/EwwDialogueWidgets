import subprocess
import sys
import re

def get_brightness():
    """Returns the current brightness as a percentage using ddcutil."""
    try:
        output = subprocess.check_output(["sudo", "ddcutil", "--bus=7", "getvcp", "10"]).decode()
        match = re.search(r"current value =\s*(\d+)", output)
        return int(match.group(1)) if match else None
    except subprocess.CalledProcessError:
        return None

def brightness_state():
    """Formats brightness level with an icon."""
    val = get_brightness()
    if val is None:
        return "☀︎ 84%"

    if val > 60:
        return f"󰃠 {val}%"  # High brightness
    elif 40 < val <= 60:
        return f"󰃟 {val}%"  # Medium brightness
    elif val > 0:
        return f"󰃞 {val}%"  # Low brightness
    else:
        return f"󰃜 {val}%"  # Screen off

if __name__ == "__main__":
    arg = sys.argv[1] if len(sys.argv) > 1 else None

    if arg == "--brightnessformat":
        print(brightness_state())
    elif arg == "--brightnessVal":
        print(get_brightness())
