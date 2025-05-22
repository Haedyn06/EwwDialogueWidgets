from pynput import keyboard
import subprocess

selected = 0
max_index = 4

def update():
    subprocess.run(["eww", "update", f"PowerSelected={selected}"])

def run_selected_action():
    actions = [
        ["systemctl", "poweroff"],
        ["systemctl", "reboot"],
        ["systemctl", "suspend"],
        ["hyprctl", "dispatch", "exit"],
        ["loginctl", "lock-session"]
    ]
    subprocess.run(actions[selected])

def on_press(key):
    global selected
    if key == keyboard.Key.up:
        selected = (selected - 1) % (max_index + 1)
        update()
    elif key == keyboard.Key.down:
        selected = (selected + 1) % (max_index + 1)
        update()
    elif key == keyboard.Key.enter:
        run_selected_action()

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
