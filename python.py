import tkinter as tk
from tkinter import ttk
from time_1 import time



root = tk.Tk()
root.geometry("500x500")
root.title("UNIT CONVERTER TOOL")

# Load the custom theme
root.tk.call("source", "Azure-ttk-theme-main/azure.tcl")
root.tk.call("set_theme", "dark")

label = tk.Label(root, text="THIS IS A TOOL TO CONVERT UNITS", font=('Arial', 18))
label.grid( column=0, columnspan=2, padx=40, pady=40)

# Set a fixed width and external padding for all buttons
button_style = {'style': 'Accent.TButton', 'padding': 20, 'width': 20,}

button1 = ttk.Button(root, text='UNIT CONVERSION', **button_style)
button1.grid(row=1,  pady=(0, 10))

button2 = ttk.Button(root, text='TIME CONVERSION', **button_style, command=time)
button2.grid(row=2,  pady=(0, 10))

button3 = ttk.Button(root, text='CURRENCY CONVERSION', **button_style)
button3.grid(row=3, pady=(0, 10))

button4 = ttk.Button(root, text='TEMPERATURE CONVERSION', **button_style)
button4.grid(row=4,)

root.mainloop()