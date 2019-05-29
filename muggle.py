import tkinter
import keyboard
from tkinter import messagebox as tkMessageBox
import os
import subprocess

window = tkinter.Tk()
# to rename the title of the window
window.title("Muggle")
# pack is used to show the object in the window
window.geometry("150x300")
label = tkinter.Label(window, text = "Launch").pack()
#window.withdraw()
window.mainloop()

root = Tk()


def ocWin():
   print("ocWin") 


def center_window(width=300, height=200):
    # get screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # calculate position x and y coordinates
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))


def close_window():
    exit(0)
    #keyboard.press_and_release('q')

def key(event):
    if event.char == 'q':
        close_window()
        print("pressed", repr(event.char))

def on_select(event,x):
        y = ["notes","guake","scratch-pad"]
        for i in range(len(x)):
                print(y[x])
                return 1 #os.system(y[x])
        

def list():
        listItems = ["notes","terminal","scratch-pad"]#create items for list
        x = Listbox(root)       
        x.bind('<<ListboxSelect>>', on_select)

        for i in range(len(listItems)):
                x.insert('end',listItems[i])
        x.pack()


def callback(event):
    frame.focus_set()
    print("clicked at", event.x, event.y)



