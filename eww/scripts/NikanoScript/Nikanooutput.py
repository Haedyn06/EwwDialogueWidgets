import os

NakanoOutput   = os.path.expanduser("~/.config/eww/scripts/NikanoScript/NikaOut.txt")

with open(NakanoOutput, "r") as file:
    content = "\n".join(line.strip() for line in file)  # Removes extra spaces
print(content)
