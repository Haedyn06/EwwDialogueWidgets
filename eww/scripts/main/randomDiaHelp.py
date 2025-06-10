import random

Dialogues = [
    "Is There Something I can Help You With?", 
    "How May I Assist You Master?", 
    "Oh Master, Are You Having Trouble With Something?", 
    "Master, What Are You Looking For?"
    ]


with open("/home/haedyn06/.config/eww/temp/helpTemp.txt", "w") as tempHelp:
    tempHelp.write(random.choice(Dialogues))