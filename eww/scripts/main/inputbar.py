#!/usr/bin/env python3
import sys
import subprocess

def handle_input():
    if len(sys.argv) > 1:
        user_input = sys.argv[1].strip()  # Get input from EWW

        subprocess.run(["notify-send", "*New Message", user_input])

        if user_input.lower() == "hello":
            subprocess.run(["notify-send", "*New Message", "Oh Hi there how are you? lol."])

        if user_input.lower() == "hello ai mommy":
            subprocess.run(["notify-send", "*New Message", "Hello darling <3    "])



        if user_input.lower() == "wofi":
            subprocess.Popen(["wofi", "--show", "drun"])


        elif user_input.startswith("run "):
            command = user_input[4:]  # Remove "run " prefix
            subprocess.Popen(command, shell=True)

if __name__ == "__main__":
    handle_input()
