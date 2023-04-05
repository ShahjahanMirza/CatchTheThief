import tkinter as tk
from tkinter import *
from tkinter import messagebox as mb

import main

print("hello")
running = True


while running:
    res = mb.askquestion("play?")

    if res == "yes":
        main()
    else:
        running = False


# Driver's code
root = tk.Tk()
canvas = tk.Canvas(root, width=200, height=200)

canvas.pack()


canvas.create_window(100, 100)

root.mainloop()
