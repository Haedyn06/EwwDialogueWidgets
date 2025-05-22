import subprocess
import sys

def set_brightness(value):
    """Set brightness using ddcutil."""
    try:
        subprocess.run(["sudo", "ddcutil", "--bus=7", "--noverify", "--sleep-multiplier=0.1", "setvcp", "10", str(value)], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error setting brightness: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        brightness = int(sys.argv[1].strip())
        if 0 <= brightness <= 100:
            set_brightness(brightness)
        else:
            print("Brightness must be between 0 and 100.")
    else:
        raise ValueError("No brightness value provided")
