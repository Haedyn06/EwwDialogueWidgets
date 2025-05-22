def spliword(sentence):
    for i, token in enumerate(sentence):
        if token == "run" or token == "open":
            if "and" in sentence[i+1:]:
                and_index = sentence.index("and", i+1)
                if and_index - 1 >= 0 and and_index + 1 < len(sentence):
                    subprocess.run(["notify-send", "*New Message", f"sure sweetie I can run both {sentence[and_index - 1]} and {sentence[and_index + 1]} for you :3"])
                    subprocess.run([sentence[and_index - 1]])
                    subprocess.run([sentence[and_index + 1]])
                    with open(ResponseFile, "w") as file:
                        file.write(f"sure sweetie I can run both {sentence[and_index - 1]} and {sentence[and_index + 1]} for you :3")
            else:
                if i+1 < len(sentence):
                    subprocess.run(["notify-send", "*New Message", f"sure sweetie I can run {sentence[i+1]} for you :3"])
                    subprocess.run([sentence[i+1]])
                    with open(ResponseFile, "w") as file:
                        file.write(f"sure sweetie I can run {sentence[i+1]} for you :3")


def checksentence(UserInp):
    spliUsrInp = UserInp.split()
    for token in spliUsrInp:
        if token == "run" or token == "open":
            return True
    return False