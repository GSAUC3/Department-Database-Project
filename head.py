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


    def Tview(self,**kwargs):
           #   ------------------------tree view-----------------------------
        self.coll=kwargs['coll']
        self.texts=kwargs['texts']
        self.tree=ttk.Treeview(self.root,height=23,selectmode='extended')
        self.tree['columns']= self.coll
        # ('name','reg','roll','sem','cor','sex')
        self.tree.column('#0',width=0,stretch=NO)
        self.tree.heading('#0',text=None)

        i=0
        while i <len(self.coll):
            self.tree.column(self.coll[i],anchor=W,width=kwargs['mota'])
            
            self.tree.heading(self.coll[i],text=self.texts[i],anchor=W)
            i+=1
            
        self.tree['show']='headings'
        self.tree.grid(row=kwargs['row'],column=0,rowspan=10,columnspan=12,padx=0,pady=7)

    def marks_view(self,guru,**score):
        self.guru=guru
        # Label(self.guru,text="Registration number",bg="lime").grid(row=5,column=0)
        pass

    def marks_clean(self,guru):

        # x=1
        for i in range(11):
            Label(guru,text='\t').grid(row=5,column=i+1)
            # x+=1
        pass