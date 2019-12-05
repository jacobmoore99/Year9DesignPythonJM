import tkinter as tk
from tkinter import *
from tkinter import messagebox
import math

print ("Start Program")
master = tk.Tk() #builds main window

def runMeSlope():
	print("RUNNING")

	slope = (int(y2.get())-int(y1.get()))/(int(x2.get())-int(x1.get()))
	results = ("Slope =" + "(" +str(y2.get()) + "-" +str(y1.get()) + ") / (" +str(x2.get()) + "-" +str(x1.get()) + ")\nSlope =" +str((int(y2.get())-int(y1.get()))) + "/" +str((int(x2.get())-int(x1.get()))) + "\nSlope =" + str(slope))
	text1.insert(tk.END,results + "\n\n")

def runMeDistance():
	print("RUNNING")

	distance = math.sqrt(((int(y2.get())-int(y1.get())) * (int(y2.get())-int(y1.get()))) + ((int(x2.get())-int(x1.get())) * (int(x2.get())-int(x1.get()))))
	resultd = ("Distance =" + "√(" +str(x2.get()) + "-" +str(x1.get()) + ")2 + (" +str(y2.get()) + "-" +str(y1.get()) + ")2" "\nDistance =" + str(distance))
	text2.insert(tk.END,resultd + "\n\n")

def runMeResult():
	print("RUNNING")

	x1.set("0")
	x2.set("0")
	y1.set("0")
	y2.set("0")

def on_closing():
	print("Closing program...")
	if messagebox.askokcancel("Quit", "Do you want to quit?"):

		master.destroy()

def checkSelect():
	state = checkvar.get()

	if state == 1:
		print("High Contrast")
		master.config(bg = "black")
		w.config(bg = "black")
		w1.config(bg = "black")
		w3.config(bg = "black")
		w5.config(bg = "black")
		w7.config(bg = "black")
		w9.config(bg = "black")
		w10.config(bg = "black")
		check.config(fg = "white", bg = "black")
	else:
		print("Low Constrast")
		master.config(bg = "white")
		w.config(bg = "white")
		w1.config(bg = "white")
		w2.config(bg = "red")
		w3.config(bg = "white")
		w4.config(bg = "red")
		w5.config(bg = "white")
		w6.config(bg = "red")
		w7.config(bg = "white")
		w8.config(bg = "red")
		w9.config(bg = "white")
		w10.config(bg = "white")
		check.config(fg = "black", bg = "white")

master.title ("Slope/Distance Calculator")

w = Label(master, text="Slope/Distance Calculator", fg="red", font=("Arial", 30))
w.grid(row = 0, column = 0, columnspan = 9, sticky = "NESW")

w1 = Label(master, text="x1=", fg="red", font=("Arial", 18))
w1.grid(row = 1, column = 0)

x1 = StringVar(master)
x1.set("2") # default value

w2 = OptionMenu(master, x1, "-10", "-9", "-8", "-7", "-6", "-5", "-4", "-3", "-2", "-1", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10")
w2.config(bg = "red")
w2.grid(row = 1, column = 1)

w3 = Label(master, text="x2=", fg="red", font=("Arial", 18))
w3.grid(row = 1, column = 2)

x2 = StringVar(master)
x2.set("1") # default value

w4 = OptionMenu(master, x2, "-10", "-9", "-8", "-7", "-6", "-5", "-4", "-3", "-2", "-1", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10")
w4.config(bg = "red")
w4.grid(row = 1, column = 3)

w5 = Label(master, text="y1=", fg="red", font=("Arial", 18))
w5.grid(row = 1, column = 4)

y1 = StringVar(master)
y1.set("2") # default value

w6 = OptionMenu(master, y1, "-10", "-9", "-8", "-7", "-6", "-5", "-4", "-3", "-2", "-1", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10")
w6.config(bg = "red")
w6.grid(row = 1, column = 5)

w7 = Label(master, text="y2=", fg="red", font=("Arial", 18))
w7.grid(row = 1, column = 6)

y2 = StringVar(master)
y2.set("1") # default value

w8 = OptionMenu(master, y2, "-10", "-9", "-8", "-7", "-6", "-5", "-4", "-3", "-2", "-1", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10")
w8.config(bg = "red")
w8.grid(row = 1, column = 7)

btn1 = tk.Button(master, width = 10, height = 2)
#step 2: configure the widget
btn1.config(text = "Reset", font=("Anton", 18, "bold"), highlightbackground = "grey", command = runMeResult)
#step 3: place the widget - pack(), grid()
btn1.grid(row = 1, column = 8)

btn2 = tk.Button(master, width = 30, height = 2)
#step 2: configure the widget
btn2.config(text = "Slope", font=("Anton", 18, "bold"), highlightbackground = "green", command = runMeSlope)
#step 3: place the widget - pack(), grid()
btn2.grid(row = 2, column = 0, columnspan = 5)

btn3 = tk.Button(master, width = 30, height = 2)
#step 2: configure the widget
btn3.config(text = "Distance", font=("Anton", 18, "bold"), highlightbackground = "blue", command = runMeDistance)
#step 3: place the widget - pack(), grid()
btn3.grid(row = 2, column = 5, columnspan = 4)

w9 = Label(master, text="Slope formula:", fg="green", font=("Arial", 18))
w9.grid(row = 3, column = 0, columnspan = 2)

w10 = Label(master, text="Distance formula:", fg="blue", font=("Arial", 18))
w10.grid(row = 3, column = 5, columnspan = 2)

slope = (int(y2.get())-int(y1.get()))/(int(x2.get())-int(x1.get()))
distance = math.sqrt(((int(y2.get())-int(y1.get())) * (int(y2.get())-int(y1.get()))) + ((int(x2.get())-int(x1.get())) * (int(x2.get())-int(x1.get()))))

text1 = tk.Text(master, width = 60, height = 20)
text1.config(bg = "green", font=("Times", 14))
text1.insert(tk.END, "Slope = (y2-y1)/(x2-x1)\n\n")
text1.grid(row = 4, column = 0, columnspan = 5)

text2 = tk.Text(master, width = 60, height = 20)
text2.config(bg = "blue", font=("Times", 14))
text2.insert(tk.END, "Distance = √(x2-x1)2 + (y2-y1)2\n\n")
text2.grid(row = 4, column = 5, columnspan = 5)

checkvar = tk.IntVar()
check = tk.Checkbutton(master, text = "High Contrast", variable = checkvar, command = checkSelect)
check.config(anchor = tk.W)
check.grid(row = 5, column = 0, columnspan = 2)

master.protocol("WM_DELETE_WINDOW", on_closing)

mainloop()

print("End Program")