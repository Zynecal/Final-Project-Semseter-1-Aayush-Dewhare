import tkinter as tk
from tkinter import PhotoImage

def newWindow():

    window = tk.Tk()
    window.geometry('900x750')

    window.title('TaskFlow - Interactive Homework Tracker')

    tk.Label(window, text="Title",font=("Arial", 16)).pack()

    logo_img = PhotoImage(file="")


    window.mainloop()

newWindow()