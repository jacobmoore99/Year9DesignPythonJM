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

scrollbar = Scrollbar(root)
scrollbar.pack( side = RIGHT, fill = Y )

mylist = Listbox(root, yscrollcommand = scrollbar.set )
for line in range(100):
	mylist.insert(END, "This is line number " + str(line))


mylist.pack( side = LEFT, fill = BOTH )
scrollbar.config( command = mylist.yview )

root.mainloop()

print ("END PROGRAM")