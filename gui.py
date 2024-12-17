import tkinter as tk
from tkinter import PhotoImage
from tkinter import Label
from PIL import Image, ImageTk
import os

def newWindow():

    window = tk.Tk()
    window.geometry('900x750')

    window.title('TaskFlow - Interactive Homework Tracker')

    title = tk.Label(
        window, 
        text="Assignment Tracker",
        font=("Calibri", 30),
        justify="left"
    )

    title.pack(pady=10, padx=10, anchor="w")
    title.pack(pady=75)

    assignment_heading = tk.Label(
        window, 
        text="Assignments:",
        font=("Calibri", 20),
        justify="left",
        fg ="red"
    )

    assignment_heading.pack(pady=10,padx=10, anchor="w")
    assignment_heading.pack(pady=5)

    image_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'logo.png')
    #logo_img = PhotoImage(file = "")
    img = Image.open(image_path)

    img_tk = ImageTk.PhotoImage(img)

    # Create a label and display the image
    label = tk.Label(window, image=img_tk)
    label.pack()

    # Keep a reference to the image object to prevent it from being garbage collected
    label.image = img_tk


    window.mainloop()

newWindow()