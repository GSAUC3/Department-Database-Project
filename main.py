from tkinter import *
from tkinter import ttk
from ttkbootstrap import *
from PIL import ImageTk, Image
from tkinter import messagebox
import csv
import head
import json


class window:

    def __init__(self, root, title, dept, resolution, siz):
        self.root = root
        self.dept = dept
        self.title=title
        self.res=resolution
        self.siz=siz
        head.header(self.root,self.title,self.dept,self.res,self.siz)
        

        # header menu bar--------------------------------
        menu = Menu(self.root)
        self.file = Menu(menu)
        self.file.add_command(label='New')
        self.file.add_command(label='Open')
        self.file.add_command(label='Save')
        self.file.add_separator()
        self.file.add_command(label='Exit', command=self.root.quit)
        menu.add_cascade(label='File', menu=self.file)
        self.edit = Menu(menu)
        self.edit.add_command(label='Undo')
        menu.add_cascade(label='Edit', menu=self.edit)
        self.root.config(menu=menu)
       # right click popup--------------------------------
        self.men = Menu(self.root, tearoff=False)
        self.men.add_command(label='Refresh Table')
        self.men.add_command(label='Clear Entry Fields')
        self.men.add_command(label='Clear Table')
        self.men.add_separator()
        self.men.add_command(
            label='Insert', command= self.insert)
        self.men.add_command(label='Show All')
        self.men.add_separator()
        self.men.add_command(label='Exit Database', command=self.root.quit)
        self.root.bind('<Button-3>', self.popup)

        #    ------------------------name-----------------------------
        self.nam=StringVar()
        ttk.Label(self.root,text='Full Name').grid(row=1,column=0,padx=5)
        ttk.Entry(self.root,width=25,textvariable=self.nam).grid(row=1,column=1,pady=5,padx=5)
          #    ------------------------reg no-----------------------------

        self.regno=StringVar()
        ttk.Label(self.root,text='Registration Number').grid(row=1,column=2,padx=5)
        ttk.Entry(self.root,width=25,textvariable=self.regno).grid(row=1,column=3,pady=5,padx=5)
         #    ------------------------roll no-----------------------------
        self.rollno=StringVar()
        ttk.Label(self.root,text='Roll number').grid(row=1,column=4,padx=5)
        ttk.Entry(self.root,width=25,textvariable=self.rollno).grid(row=1,column=5,pady=5,padx=5)
          #    ------------------------course-----------------------------
        
        self.korse=['B.Tech','M.Tech']
        ttk.Label(self.root,text='Course').grid(row=2,column=0,pady=5,padx=5)
        self.k0=ttk.Combobox(self.root,values=self.korse,width=23)
        self.k0.grid(row=2,column=1,padx=5)
        self.k0['state']='readonly'
        self.k0.set(self.korse[0])
        self.k0.bind("<<ComboboxSelected>>",self.mORb)

       #    ------------------------semester-----------------------------

        ttk.Label(self.root,text='Semester').grid(row=2,column=2,pady=5,padx=5)
        self.btech=['B1','B2','B3','B4','B5','B6','B7','B8']
        self.mtech=['M1','M2','M3','M4']
        

        self.k1=ttk.Combobox(self.root,values=self.btech,width=23)
        self.k1.grid(row=2,column=3,padx=5)
        self.k1['state']='readonly'
       #    ------------------------sex-----------------------------

        ttk.Label(self.root,text='Sex').grid(row=2,column=4,pady=5,padx=5)
        self.gender=['-','Female','Male','Others']
        
        self.kg=ttk.Combobox(self.root,values=self.gender,width=23)
        self.kg.grid(row=2,column=5,padx=5)
        self.kg['state']='readonly'
        
       #    ------------------------tree view-----------------------------
        self.tree=ttk.Treeview(self.root,height=23,selectmode='extended')
        self.tree['columns']=('name','reg','roll','sem','cor','sex')

        self.tree.column('#0',width=0,stretch=NO)
        self.tree.column('name',anchor=W,width=200)
        self.tree.column('reg',anchor=W,width=250)
        self.tree.column('roll',anchor=W,width=250)
        self.tree.column('sem',anchor=W,width=200)
        self.tree.column('cor',anchor=W,width=200)
        self.tree.column('sex',anchor=W,width=100)

        self.tree.heading('#0',text=None)
        self.tree.heading('name',text='Full Name',anchor=W)
        self.tree.heading('reg',text='University Registration Number',anchor=W)
        self.tree.heading('roll',text='University Roll Number',anchor=W)
        self.tree.heading('sem',text='Current Semester',anchor=W)
        self.tree.heading('cor',text='Course',anchor=W)
        self.tree.heading('sex',text='Sex',anchor=W)
        self.tree['show']='headings'
        self.tree.grid(row=4,column=0,rowspan=10,columnspan=12,padx=0,pady=7)

        self.tree.bind("<ButtonRelease-1>",self.dhor)
          # --BUTTONs-------------------------
        ttk.Button(self.root,text='Insert info',width=20,command=self.insert).grid(row=1,column=9)
        ttk.Button(self.root,text='Update info',style='info.Outline.TButton',width=20).grid(row=2,column=9)

        ttk.Button(self.root,text='Refresh',width=15,padding=10).grid(row=4,column=12)
        ttk.Button(self.root,text='Clear Table',width=15,padding=10).grid(row=5,column=12)
        ttk.Button(self.root,text='Clear Entry Fields',width=15,padding=10).grid(row=6,column=12)
        ttk.Button(self.root,text='',width=15,padding=10).grid(row=7,column=12)
        ttk.Button(self.root,text='Delete Record',style='danger.TButton',width=15,padding=10).grid(row=4,column=13)
        ttk.Button(self.root,text='View All info',width=15,padding=10).grid(row=5,column=13)
        ttk.Button(self.root,text='Enter Marks',style='success.TButton',width=15,padding=10,command=lambda:self.marks(self.title,self.dept,self.res,self.siz)).grid(row=6,column=13)
        ttk.Button(self.root,text='',width=15,padding=10).grid(row=7,column=13)

        #    search bar---------
        Label(self.root,text='Search within Database',font='Helvetica 18').grid(row=1,column=11,columnspan=3)
        self.nebo=StringVar()
        choose =['Full Name','Semester','Registration number','Roll number','Sex','Course']
        search_y=ttk.Combobox(self.root,value=choose,width=31,textvariable=self.nebo)
        search_y['state'] = 'readonly'
        self.nebo.set('Search By...')
        search_y.grid(row=2,column=11,columnspan=2,padx=10)
        ttk.Entry(self.root,width=33).grid(row=3,column=11,columnspan=2,pady=5,padx=5)
        ttk.Button(self.root,text='SEARCH',padding=20,width=15).grid(row=2,rowspan=2,column=13,pady=1)

        # function for the treeview
    def dhor(self,e):
        self.rollno.set('')
        self.regno.set('')
        self.nam.set('')
        self.kg.set('')
        selected=self.tree.focus()
        val=self.tree.item(selected,'val')
        self.rollno.set(val[2])
        self.regno.set(val[1])
        self.nam.set(val[0])
        self.kg.set(val[5])
        self.k1.set(val[3])
        self.k0.set(val[4])
        
        pass
     
    def insert(self):
        # name reg roll sem course sex
        self.tree.insert(parent='',index='end',values=(self.nam.get(),self.regno.get(),self.rollno.get(),self.k1.get(),self.k0.get(),self.kg.get()))
       

      # RIGHT CLICK SIDE POPUP MENU 
    def popup(self,e):
        self.men.tk_popup(e.x_root,e.y_root)

     # binding the two drop boxes (metch and btech) with their respective semester 
    def mORb(self,e):
        if self.k0.get() == 'B.Tech':
            self.k1.config(values=self.btech)
            self.k1.current(0)
        else:
            self.k1.config(values=self.mtech)
            self.k1.current(0)
    # 2nd window for marks
    def marks(self,t,d,r,s):
      
      def mtob(e):
        if l0.get() == 'B.Tech':
            l1.config(values=self.btech)
            l1.current(0)
        else:
            l1.config(values=self.mtech)
            l1.current(0)
        pass
      win=Toplevel()
      # self.root,self.title,self.dept,self.res,self.siz

      win.title('OOE Database')
      head.header(win,t,d,r,s)
      ttk.Label(win,text='Course').grid(row=2,column=0,pady=5,padx=5)
      l0=ttk.Combobox(win,values=self.korse,width=23)
      l0.grid(row=2,column=1,padx=5)
      l0['state']='readonly'
      l0.set(self.korse[0])
      l0.bind("<<ComboboxSelected>>",mtob)
      ttk.Label(win,text='Semester').grid(row=2,column=2,pady=5,padx=5)
      
        

      l1=ttk.Combobox(win,values=self.btech,width=23)
      l1.grid(row=2,column=3,padx=5)
      l1['state']='readonly'
     


      pass
       

if __name__ == '__main__':
    win=Style(theme='cosmo').master
 # make the necessary changes for your won depertment here, that includes title,
 #  name of the dept,font size, and resolution / size of the window
    title='OOE Database'                

    department='Department Of Optics and Photonics'
    resolution = '1600x900'
    siz='40' #font size

    header=window(win,title,department,resolution,siz)
    
    win.mainloop()

    # ['lumen', 'pulse', 'litera', 'minty', 'flatly', 'superhero', 'solar', 'alt', 
    # 'yeti', 'journal', 'vista', 'default', 'classic', 'sandstone', 'cyborg', 'united', 
    # 'xpnative', 'clam', 'winnative', 'cosmo', 'darkly']
