import tkinter as tk
from tkinter import *

print ("Start Program")
master = tk.Tk() #builds main window

master.title ("Slope/Distance Calculator")

w = Label(master, text="Slope/Distance Calculator", fg="red", font=("Arial", 30))
w.grid(row = 0, column = 0, columnspan = 9, sticky = "NESW")

w1 = Label(master, text="x1=", fg="red", font=("Arial", 18))
w1.grid(row = 1, column = 0)

variable = StringVar(master)
variable.set("0") # default value

w2 = OptionMenu(master, variable, "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10")
w2.config(bg = "red")
w2.grid(row = 1, column = 1)

w3 = Label(master, text="x2=", fg="red", font=("Arial", 18))
w3.grid(row = 1, column = 2)

variable = StringVar(master)
variable.set("0") # default value

w4 = OptionMenu(master, variable, "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10")
w4.config(bg = "red")
w4.grid(row = 1, column = 3)

w5 = Label(master, text="y1=", fg="red", font=("Arial", 18))
w5.grid(row = 1, column = 4)

variable = StringVar(master)
variable.set("0") # default value

w6 = OptionMenu(master, variable, "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10")
w6.config(bg = "red")
w6.grid(row = 1, column = 5)

w7 = Label(master, text="y2=", fg="red", font=("Arial", 18))
w7.grid(row = 1, column = 6)

variable = StringVar(master)
variable.set("0") # default value

w8 = OptionMenu(master, variable, "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10")
w8.config(bg = "red")
w8.grid(row = 1, column = 7)

btn1 = tk.Button(master, width = 10, height = 2)
#step 2: configure the widget
btn1.config(text = "Result", font=("Anton", 18, "bold"), highlightbackground = "grey")
#step 3: place the widget - pack(), grid()
btn1.grid(row = 1, column = 8)

btn2 = tk.Button(master, width = 30, height = 2)
#step 2: configure the widget
btn2.config(text = "Slope", font=("Anton", 18, "bold"), highlightbackground = "green")
#step 3: place the widget - pack(), grid()
btn2.grid(row = 2, column = 0, columnspan = 5)

btn3 = tk.Button(master, width = 30, height = 2)
#step 2: configure the widget
btn3.config(text = "Distance", font=("Anton", 18, "bold"), highlightbackground = "blue")
#step 3: place the widget - pack(), grid()
btn3.grid(row = 2, column = 5, columnspan = 4)

w9 = Label(master, text="Slope formula:", fg="green", font=("Arial", 18))
w9.grid(row = 3, column = 0, columnspan = 2)

w10 = Label(master, text="Distance formula:", fg="blue", font=("Arial", 18))
w10.grid(row = 3, column = 5, columnspan = 2)

output = tk.Text(master, width = 60, height = 20)
output.config(bg = "green")
output.grid(row = 4, column = 0, columnspan = 5)

output = tk.Text(master, width = 60, height = 20)
output.config(bg = "blue")
output.grid(row = 4, column = 5, columnspan = 5)

mainloop()