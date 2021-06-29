from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

class header:

    def __init__(self, root, title, dept, resolution, siz):
        self.root = root
        
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



            #   ------------------------tree view-----------------------------
    def disp(self,coll):
        self.tree=ttk.Treeview(self.root,height=23,selectmode='extended')
        self.tree['columns']= coll
        # ('name','reg','roll','sem','cor','sex')
        self.tree.column('#0',width=0,stretch=NO)
        self.tree.column(coll[0],anchor=W,width=200)
        self.tree.column(coll[1],anchor=W,width=250)
        self.tree.column(coll[2],anchor=W,width=250)
        self.tree.column(coll[3],anchor=W,width=200)
        self.tree.column(coll[4],anchor=W,width=200)
        self.tree.column(coll[5],anchor=W,width=100)

        self.tree.heading('#0',text=None)
        self.tree.heading(coll[0],text='Full Name',anchor=W)
        self.tree.heading(coll[1],text='University Registration Number',anchor=W)
        self.tree.heading(coll[2],text='University Roll Number',anchor=W)
        self.tree.heading(coll[3],text='Current Semester',anchor=W)
        self.tree.heading(coll[4],text='Course',anchor=W)
        self.tree.heading(coll[5],text='Sex',anchor=W)
        self.tree['show']='headings'
        self.tree.grid(row=4,column=0,rowspan=10,columnspan=12,padx=0,pady=7)
