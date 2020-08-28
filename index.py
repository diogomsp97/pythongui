import tkinter as tk
from tkinter import filedialog, Text
import os

window = tk.Tk()
window.title("GUI - Login Screen")

def openAction():
    print("openAction !!!")

def addAction():
    print("addAction !!!")

def quitAction():
    window.destroy()

canvas = tk.Canvas(window, height=360, width=480, bg="#333333")
canvas.pack()

frame = tk.Frame(window, bg="gray")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

loginBtn = tk.Button(window, text="Add File", padx=10, pady=5, fg="black", bg="gray", command=addAction)
loginBtn.pack()

loginBtn = tk.Button(window, text="Open All", padx=10, pady=5, fg="black", bg="gray", command=openAction)
loginBtn.pack()

quitBtn = tk.Button(window, text="Quit", padx=10, pady=5, fg="black", bg="gray", command=quitAction)
quitBtn.pack()

label = tk.Label(frame, text="Username:", bg="gray")
label.pack()

window.mainloop()
