import time
import pyautogui
import tkinter as tk

def screenshot():
    #time.sleep(5);
    name = int(round(time.time()*1000))
    name = "{}.png".format(name)
    img = pyautogui.screenshot(name)
    img.show()

# screenshot()

# To get random file name.
# name = int(random(time.time()*1000))
# name = "{}.png".format(name)

# To save in a given folder
# name = "D:/Python/screenshots/{}.png".format(name)



#-------- MAKE GUI------
root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame, text = "Take Screenshot", command=screenshot)
button.pack(side= tk.LEFT)

close = tk.Button(frame, text = "Quit", command=quit)
close.pack(side= tk.RIGHT)

root.mainloop()