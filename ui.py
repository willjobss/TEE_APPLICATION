"""
    this is the ui of the scure file and the inscure file
    and the inscure file needs a key to access; while the 
    scure file can be accessed
    
    and first the accessor needs to login
    
    and the application codes' savety is garenteed by the
    secure hash algorithm, so it is very safe
    
"""
from tkinter import *
import os
import sys
from PIL import Image, ImageTk

font1=('Garamond',12)
font2=('Candara Light',18)
color1="peachpuff"
color2="skyblue"
color3="lightcoral"
color4="mediumpurple"
directory1=r'F:\集创赛\file\scure_filefolder'
directory2=r'F:\集创赛\file\inscure_filefolder'
dirs1 = os.listdir( directory1 )
dirs2 = os.listdir( directory2 )
"""
    something to do is to add the photos into the button
"""
#photo = ImageTk.PhotoImage(file="image\photo.png")

class AccessInital:
    def __init__(self):
        self.root = Tk()
        self.root['bg']='peachpuff'
        self.root.title("log in system")
        self.root.geometry("500x300")
        self.t = Label(self.root,text="key",width=5,height=2,font=('Garamond',20),bg=color1)
        self.t.place(x=10,y=20)
        global v1 
        v1 = StringVar()
        self.t2=Entry(self.root,textvariable = v1,width=50)
        self.t2.place(x=100,y=40)
        self.t3=Button(self.root,text="sure",command=self.check1,width=10,height=2,bg=color3,highlightthickness=0)
        self.t3.place(x=150,y=100)
        self.t4=Button(self.root,text="quit",command=self.root.quit,width=10,height=2,bg=color2,highlightthickness=0)
        self.t4.place(x=300,y=100)
        self.root.mainloop()
        
    def check1(self):
        if(v1.get()=='1'):
            self.root.destroy()
            app=MyApp()
        
class MyApp:
    def __init__(self):
        
        self.root = Tk()
        self.root['bg']='peachpuff'
        self.root.title("My *GUI")
        self.root.geometry("800x494") 
        self.t = Label(self.root,text="something",width=20,height=2,font=font1,bg=color1)
        self.t.grid(row=0,column=0)
        
        self.t3=Button(self.root,text="ok",command=self.check,width=10,height=2)
        self.t3.grid(row=2,column=2)
        self.t3.destroy()
        
        Button(self.root,text="scure",command=self.openscurefile,width=10,height=2,bg=color3,highlightthickness=0).grid(row=0,column=1)
        Button(self.root,text="inscure",command=self.openinscurefile,width=10,height=2,bg=color3,highlightthickness=0).grid(row=1,column=1)
        Button(self.root,text="quit UI",command=self.root.quit,width=10,height=2,bg=color2,highlightthickness=0).grid(row=2,column=1)
        """
            here is the function to save the file into the original directory
        """
        self.savebutton=Button(self.root,text="save",command=self.save,width=10,height=2,bg=color4,highlightthickness=0)
        self.savebutton.place(x=670,y=110)
        self.savebutton.destroy()
        
        self.t2 = Label(self.root,text="the statement of the file",width=60,height=2,anchor=W,font=font1,bg=color1)
        self.t2.grid(row=0,column=2)
        
        self.t4 = Label(self.root,text="the content of the text is:",font=font1,bg=color1)
        self.t4.grid(row=3,column=0)
        
        self.t5 = Text(self.root,width=50,height=10,font=font2)
        self.t5.grid(row=4,column=0,columnspan=3)
        self.list1=[0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.list2=[0,0,0,0,0,0,0,0,0,0,0,0]
        num1=0
        
        for files1 in dirs1:
            num1+=1
            
            self.list1[num1-1]=Button(self.root,text=files1,command=lambda file1=dirs1[num1-1]:self.openscurefile1(files1),width=10,height=2,bg=color1,highlightthickness=0)
            self.list1[num1-1].place(x=250+num1*80,y=60)
            self.list1[num1-1].destroy()
        num2=0
        for files2 in dirs2:
            num2+=1
            
            self.list2[num2-1]=Button(self.root,text=files2,command=lambda file2=dirs2[num2-1]:self.openinscurefile2(file2),width=10,height=2,bg=color1,highlightthickness=0)
            self.list2[num2-1].place(x=250+num2*80,y=60)
            self.list2[num2-1].destroy()    
            
        self.root.mainloop()
        if(self.root.winfo_exists()):
            self.root.destroy()
       
       
    def openscurefile(self):
        self.savebutton=Button(self.root,text="save",command=self.save,width=10,height=2,bg=color4,highlightthickness=0)
        self.savebutton.place(x=670,y=110)
        if(self.list2[0].winfo_exists()):
            n=0
            for fi in dirs2:
                self.list2[n].destroy()
                n=n+1
        self.t2["text"]="you are accessing the scure file"
        """
            os.system("explorer.exe...") is to open the filefolder which we may don't want to use
        """
        # os.system("explorer.exe %s" % directory1)
        """
            and we choose the replacement method as below
        """
        if(not self.list1[0].winfo_exists()):
            num=0
            for files1 in dirs1:
                num+=1
                self.list1[num-1]=Button(self.root,text=files1,command=lambda file1=dirs1[num-1]:self.openscurefile1(file1),width=10,height=2,bg=color1,highlightthickness=0)
                self.list1[num-1].place(x=250+num*80,y=60)
        
        if(self.t3.winfo_exists()):
            self.e.destroy()
            self.t3.destroy()
            self.c=0
            
        f= open("F:/集创赛/file/scurefile1.txt",'r')
        a=f.readlines()
        self.t4["text"]="the content of the scure text1 is:"
        self.t5.delete('1.0','end')
        self.t5.insert('1.0',a)
        f.close()
    def openinscurefile(self):
        if(self.savebutton.winfo_exists()):
            self.savebutton.destroy()
        if(self.list1[0].winfo_exists()):
            n=0
            for fi in dirs1:
                self.list1[n].destroy()
                n=n+1
        self.t5.delete('1.0','end')
        
        self.t2["text"]="inscure file, you need to enter the key"
        if(not self.t3.winfo_exists()):
            global v 
            v = StringVar()
        
            self.e = Entry(self.root,textvariable = v,width=50)
            self.e.grid(row=1,column=2)
            self.t3=Button(self.root,text="ok",command=self.check,width=10,height=2)
            self.t3.grid(row=2,column=2)
        
    def check(self):
        
        if(v.get()=='111'):
            """
                os.system("explorer.exe...") is to open the filefolder which we may don't want to use
            """
            #os.system("explorer.exe %s" % directory2)
            """
                and we choose the replacement method as below
            """
            self.t2["text"]="you access the inscure file successfully"
            self.savebutton=Button(self.root,text="save",command=self.save,width=10,height=2,bg=color4,highlightthickness=0)
            self.savebutton.place(x=670,y=110)
            if(self.e.winfo_exists()):
                self.e.destroy()
                self.t3.destroy()
            if(not self.list2[0].winfo_exists()):
                num=0
                for files2 in dirs2:
                    num+=1
                    self.list2[num-1]=Button(self.root,text=files2,command=lambda file2=dirs2[num-1]:self.openinscurefile2(file2),width=10,height=2,bg=color1,highlightthickness=0)
                    self.list2[num-1].place(x=250+num*80,y=60)
            
            f= open("F:/集创赛/file/inscurefile2.txt",'r')
            a=f.readlines()
            self.t4["text"]="the content of the inscure text2 is:"
            self.t5.delete('1.0','end')
            self.t5.insert('1.0',a)
            f.close()
    def openscurefile1(self,name):
        filename=name
        global filedirectory
        filedirectory="F:\集创赛\\file\\scure_filefolder"
        filedirectory=filedirectory+"\\"+filename
        f2= open(filedirectory,'r')
        a=f2.readlines()
        self.t4["text"]="the content of the inscure text is:"
        self.t5.delete('1.0','end')
        self.t5.insert('1.0',a)
        f2.close()
    def openinscurefile2(self,name):
        filename=name
        global filedirectory
        filedirectory="F:\集创赛\\file\\inscure_filefolder"
        filedirectory=filedirectory+"\\"+filename
        f2= open(filedirectory,'r')
        a=f2.readlines()
        self.t4["text"]="the content of the inscure text is:"
        self.t5.delete('1.0','end')
        self.t5.insert('1.0',a)
        f2.close()
    def save(self):
        a=str(self.t5.get(1.0, END))
        path=filedirectory
        if(path[0]=='F'):
            f= open(path,'w')
            f.write(a)
            f.close()
inital=AccessInital()
