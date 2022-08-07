import tkinter as tk
from tkinter import Label, ttk,  messagebox as mb
from tokenize import Name
from unicodedata import name
import webbrowser
import json
import time
import keyboard
import sys
from text2s import text2speech
text1 = "We welcome you to the Void. \n You are about to embark on a journey full of mysteries, adventures, and consequently, rewards. \n But be forewarned - the upcoming series of events may affect you for life. \n Click on next to encounter the first task."
def link(um):
    webbrowser.open_new_tab(um)
def rickroll():
    mb.showinfo(title = "Awaiting..", message = "Click ok to proceed")
    link("https://drive.google.com/file/d/1Er5l5iT1-04JzHV3081CfWegTNV1KpVs/view?usp=sharing")    
win= tk.Tk()
win.geometry("700x350")
def showLabel():
    label = Label(win, text = text1, font = ("Times New Roman", 12), justify= 'left').pack()
    label.place()
def showButton():
    button = ttk.Button(win, text= "Next", command=rickroll).pack(pady= 20)
    button.place()
# Add an optional Label widget
Label(win, text= "Greetings!", font= ('Big John', 22), justify= 'center').pack(pady= 30)
win.after(2000, showLabel)
# Create a Button to display the message
win.after(5000, showButton)
win.mainloop()
