from tkinter import *
#import keyboard
from tkinter import messagebox as tkMessageBox
#import Tkinter
import os
import subprocess

#window = tkinter.Tk()
# to rename the title of the window
#window.title("GUI")
# pack is used to show the object in the window
#label = tkinter.Label(window, text = "Hello World!").pack()
#window.mainloop()
root = Tk()

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


root.title("Muggle")
root.eval('tk::PlaceWindow %s center' %
          root.winfo_pathname(root.winfo_id()))
root.attributes('-alpha', .6)  # transparent window
list()
frame = Frame(root, width=200, height=200)
frame.bind("<Key>", key)
frame.bind("<Button-1>", callback)
frame.pack()
root.mainloop()

