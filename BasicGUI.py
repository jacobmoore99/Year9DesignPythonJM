import tkinter as tk
from tkinter import *

print ("Start Program")
root = tk.Tk() #builds your main window
root.title ("Tkinter Practice")
#widget is an element in a GUI
#button, textbox, slider, input box, image
#step 1: construct the widget

btn1 = tk.Button(root, width = 100, height = 3)
#step 2: configure the widget
btn1.config(text = "First Attempt At a Button")
#step 3: place the widget - pack(), grid()
btn1.pack()

output = tk.Text(root, width = 100, height = 20)
output.config()
output.pack();

variable = StringVar(root)
variable.set("Jacob") # default value

w = OptionMenu(root, variable, "Jacob", "Thomas", "Moore", "Po", "Gratis")
w.pack()

root.mainloop()

print ("END PROGRAM")