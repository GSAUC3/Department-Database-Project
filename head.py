from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

class header:

    def __init__(self, root, title, dept, resolution, siz):
        self.root = root
        # self.dept = dept
        self.root.title(title)
        # self.res=resolution
        self.root.geometry(resolution)

        load = Image.open("img/culogo.png")
        load = load.resize((120, 120), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)
        img = Label(self.root, image=render)
        img.image = render
        img.grid(row=0, column=0)
        Label(self.root, text=dept, font='Ariel ' + str(siz),bg="#4c0296",fg="white", bd=5,relief=GROOVE,pady=15,padx=260
              ).grid(row=0, column=1, columnspan=14, pady=0, padx=0)