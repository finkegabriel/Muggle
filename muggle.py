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
                print("pressed ",value)
                if value == 'terminal':
                        os.system('lxterminal')
                theKill()

        if o == "'q'":
                print("exit")
                root.destroy()
                exit()
def theKill():
        root.destroy()
        exit()
def items(t):
      l = keyboard.Listener(on_press=press_callback)
      l.start()
      for item in t:
        x.insert(END, item)        

root.title("Muggle")
root.eval('tk::PlaceWindow %s center' %
          root.winfo_pathname(root.winfo_id()))
root.attributes('-alpha', .6)  # transparent window
x = Listbox(root)       
s = ["notes","terminal","scratch-pad"]
items(s)


x.pack()



frame = Frame(root, width=200, height=200)
frame.pack()
root.mainloop()
