from tkinter import *
from pynput import keyboard
from tkinter import messagebox as tkMessageBox
import os
import subprocess
import sys
root = Tk()

def press_callback(key):
        o = '{}'.format(key)
        value=str((x.get(ACTIVE)))
        # print(o)
        if o == 'Key.enter':
                #uncomment to debug
                # print("pressed ",value)
                if value == 'scratch-pad':
                        theKill(2)
                        os.system('gedit')
                        theKill(0)
        if o == "'q'":
                print("exit")
                theKill(0)

def theKill(x):
        if x == 0:
                root.destroy()
                exit()
        if x == 1:
                exit()
        if x == 2:
                root.destroy()
def items(t):
      l = keyboard.Listener(on_press=press_callback)
      l.start()
      for item in t:
        x.insert(END, item)        

root.title("Muggle")
root.eval('tk::PlaceWindow %s center' %
          root.winfo_pathname(root.winfo_id()))
root.attributes('-alpha', 0)  # transparent window
x = Listbox(root)       
s = ["notify","scratch-pad"]
items(s)


x.pack()



frame = Frame(root, width=200, height=200)
frame.pack()
root.mainloop()
