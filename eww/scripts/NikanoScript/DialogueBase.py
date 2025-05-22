import os
import sys
import subprocess
import random
NakanoOutput   = os.path.expanduser("~/.config/eww/scripts/NikanoScript/NikaOut.txt")
NakanoBlush   = os.path.expanduser("~/.config/eww/AscChar/NakanoBlush.txt")
NakanoExp   = os.path.expanduser("~/.config/eww/AscChar/NakanoExp.txt")
NakanoFlirt   = os.path.expanduser("~/.config/eww/AscChar/NakanoFlirt.txt")
NakanoGrab   = os.path.expanduser("~/.config/eww/AscChar/NakanoGrab.txt")
NakanoKneel   = os.path.expanduser("~/.config/eww/AscChar/NakanoKneel.txt")
NakanoLay   = os.path.expanduser("~/.config/eww/AscChar/NakanoLay.txt")
NakanoListen   = os.path.expanduser("~/.config/eww/AscChar/NakanoListen.txt")
NakanoPoint   = os.path.expanduser("~/.config/eww/AscChar/NakanoPoint.txt")
NakanoPonder   = os.path.expanduser("~/.config/eww/AscChar/NakanoPonder.txt")
NakanoShy   = os.path.expanduser("~/.config/eww/AscChar/NakanoShy.txt")
NakanoBend   = os.path.expanduser("~/.config/eww/AscChar/NakanoBend.txt")
NakanoCute   = os.path.expanduser("~/.config/eww/AscChar/NakanoCute.txt")
NakanoDom   = os.path.expanduser("~/.config/eww/AscChar/NakanoDom.txt")
NakanoLay2   = os.path.expanduser("~/.config/eww/AscChar/NakanoLay2.txt")
NakanoMelon   = os.path.expanduser("~/.config/eww/AscChar/NakanoMelon.txt")
NakanoOops   = os.path.expanduser("~/.config/eww/AscChar/NakanoOops.txt")
NakanoSleep   = os.path.expanduser("~/.config/eww/AscChar/NakanoSleep.txt")
NakanoWee   = os.path.expanduser("~/.config/eww/AscChar/NakanoWee.txt")

AsciiFiles = [NakanoBlush, NakanoExp, NakanoFlirt, NakanoGrab, NakanoKneel, NakanoWee, NakanoLay, NakanoListen, NakanoPoint, NakanoPonder, NakanoShy, NakanoBend, NakanoCute, NakanoDom, NakanoLay2, NakanoMelon, NakanoOops, NakanoSleep]

randomFile = random.choice(AsciiFiles)

try:
    with open(randomFile, "r") as infile:
        content = infile.read()

    with open(NakanoOutput, "w") as outfile:
        outfile.write(content)

    print(f"Contents of {randomFile} written to {NakanoOutput}")

except FileNotFoundError:
    print(f"Error: {randomFile} not found.")
except Exception as e:
    print(f"Unexpected error: {e}")