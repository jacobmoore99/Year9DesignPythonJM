import tkinter as tk
from tkinter import *

print ("Start Program")
master = tk.Tk() #builds main window

master.title ("Slope/Distance Calculator")

w = Label(master, text="Slope/Distance Calculator", fg="red", font=("Arial", 30))
w.grid(row = 0, column = 0, columnspan = 9, sticky = "NESW")

w = Label(master, text="x1=", fg="red", font=("Arial", 18))
w.grid(row = 1, column = 0)

variable = StringVar(master)
variable.set("0") # default value

w = OptionMenu(master, variable, "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10")
w.config(bg = "red")
w.grid(row = 1, column = 1)

w = Label(master, text="x2=", fg="red", font=("Arial", 18))
w.grid(row = 1, column = 2)

variable = StringVar(master)
variable.set("0") # default value

w = OptionMenu(master, variable, "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10")
w.config(bg = "red")
w.grid(row = 1, column = 3)

w = Label(master, text="y1=", fg="red", font=("Arial", 18))
w.grid(row = 1, column = 4)

variable = StringVar(master)
variable.set("0") # default value

w = OptionMenu(master, variable, "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10")
w.config(bg = "red")
w.grid(row = 1, column = 5)

w = Label(master, text="y2=", fg="red", font=("Arial", 18))
w.grid(row = 1, column = 6)

variable = StringVar(master)
variable.set("0") # default value

w = OptionMenu(master, variable, "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10")
w.config(bg = "red")
w.grid(row = 1, column = 7)

btn1 = tk.Button(master, width = 10, height = 2)
#step 2: configure the widget
btn1.config(text = "Result")
#step 3: place the widget - pack(), grid()
btn1.grid(row = 1, column = 8)

btn2 = tk.Button(master, width = 30, height = 2)
#step 2: configure the widget
btn2.config(text = "Slope", fg="green", font=("Anton", 18))
#step 3: place the widget - pack(), grid()
btn2.grid(row = 2, column = 0, columnspan = 5)

btn3 = tk.Button(master, width = 30, height = 2)
#step 2: configure the widget
btn3.config(text = "Distance", fg="blue", font=("Anton", 18))
#step 3: place the widget - pack(), grid()
btn3.grid(row = 2, column = 5, columnspan = 4)

mainloop()