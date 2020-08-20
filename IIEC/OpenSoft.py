import os
print("\nWelcome back my favourate human.\nHope you had a great day.\n")
p = input("How can I help you?: ");
posword = ["run", "execute", "start", "launch", "open", "want", "have"]
negewords =["not", "dont"]
check = False
checkchrome = False
checkpaint = False


for i in posword:
    if i in p:
        check = True

chrome =["search", "surfing", "find", "know", "mail", "send", "watch", "learn", "tutorial"]
paint = ["paint", "colour", "color", "draw", "happy", "say"]

for i in chrome:
    if i in p:
        checkchrome = True
    
for i in paint:
    if i in p:
        checkpaint = True

if check:
    if(checkchrome):
        os.system("start chrome")
    elif("editor" in p or "notepad" in p or "list" in p):
        os.system("start notepad")
    elif(checkpaint):
        os.system("start mspaint")
    elif("code" in p or "work" in p or "concept"):
        os.system("start code.exe")

else:
    print("Hmm. Something went wrong.")

