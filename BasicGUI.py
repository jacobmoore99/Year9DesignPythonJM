import tkinter as tk

print ("Start Program")
root = tk.Tk() #builds your main window

#widget is an element in a GUI
#button, textbox, slider, input box, image
#step 1: construct the widget

btn1 = tk.Button(root, width = 10, height = 3)
#step 2: configure the widget
btn1.config(text = "I am a button")
#step 3: place the widget - pack(), grid()
btn1.pack()

output = tk.Text(root, width = 100, height = 20)
output.config()
output.pack();

root.mainloop()

print ("END PROGRAM")