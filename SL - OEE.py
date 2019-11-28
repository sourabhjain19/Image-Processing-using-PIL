# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 15:26:33 2018

@author: LENOVO
"""
from tkinter.filedialog import askopenfilename
from tkinter import *
import tkinter.messagebox
from PIL import Image

def click():
    
    im1=im.transpose(Image.FLIP_TOP_BOTTOM)
    im1.show()
    def save1():
        y=[]
        y=(filename).split(".")
        im1.save(y[0]+"_flip_top."+y[1])
        tkinter.messagebox.showinfo("Saved"," Saved as "+y[0]+"_flip_top."+y[1])
    Button18 = Button(window,text="Save",command=save1,font="Times 12").grid(row=7,column=1,sticky=E)
    
def click1():
    
    im1=im.transpose(Image.FLIP_LEFT_RIGHT)
    def save2():
        y=[]
        y=(filename).split(".")
        im1.save(y[0]+"_flip_left."+y[1])
        tkinter.messagebox.showinfo("Saved"," Saved as "+y[0]+"_flip_left."+y[1])
    im1.show()
    Button12 = Button(window,text="Save",font="Times 12",command=save2).grid(row=8,column=1,sticky=E)
    
def click3():
    
    im1=im.transpose(Image.TRANSPOSE)
    def save3():
        y=[]
        y=(filename).split(".")
        im1.save(y[0]+"_transpose."+y[1])
        tkinter.messagebox.showinfo("Saved"," Saved as "+y[0]+"_transpose."+y[1])
    im1.show()
    Button13 = Button(window,text="Save",font="Times 12",command=save3).grid(row=6,column=1,sticky=E)
    
def click4():
    
    im1=im.transpose(Image.ROTATE_90)
    def save4():
        y=[]
        y=(filename).split(".")
        im1.save(y[0]+"_rotate_90."+y[1])
        tkinter.messagebox.showinfo("Saved"," Saved as "+y[0]+"_rotate_90."+y[1])
    im1.show()
    Button14 = Button(window,text="Save",font="Times 12",command=save4).grid(row=9,column=1,sticky=E)

def click5():
    
    im1=im.transpose(Image.ROTATE_180)
    def save5():
        y=[]
        y=(filename).split(".")
        im1.save(y[0]+"_rotate_180."+y[1])
        tkinter.messagebox.showinfo("Saved"," Saved as "+y[0]+"_rotate_180."+y[1])
    im1.show()
    Button15 = Button(window,text="Save",font="Times 12",command=save5).grid(row=10,column=1,sticky=E)

def click6():
    
    im1=im.transpose(Image.ROTATE_270)
    def save6():
        y=[]
        y=(filename).split(".")
        im1.save(y[0]+"_rotate_270."+y[1])
        tkinter.messagebox.showinfo("Saved"," Saved as "+y[0]+"_rotate_270."+y[1])
    im1.show()
    Button16 = Button(window,text="Save",font="Times 12",command=save6).grid(row=11,column=1,sticky=E)

def path1():
    
    if((entry1.get()) =="" or (entry2.get()) == ""):
        tkinter.messagebox.showerror("Error",message="Please enter the values")
        return
    if((entry1.get()).isalpha() or (entry2.get()).isalpha()):
        tkinter.messagebox.showerror("Error",message="Please enter the numeric values")
        return
    if(int(entry1.get()) > 2000 or int(entry2.get()) > 2000):
        tkinter.messagebox.showerror("Error",message="Image size out of range !\nMaximum size for both width and height is 2000 pixels")
        return
    if(int(entry1.get()) < 0 or int(entry2.get()) < 0):
        tkinter.messagebox.showerror("Error",message="Image size out of range !\nMinimum size for both width and height is 1 pixels")
        return
    im1=im.resize((int(entry1.get()),int(entry2.get())))
    def save7():
        y=[]
        y=(filename).split(".")
        im1.save(y[0]+"_size_"+entry1.get()+"x"+entry2.get()+"."+y[1])
        tkinter.messagebox.showinfo("Saved"," Saved as "+y[0]+"_size_"+entry1.get()+"x"+entry2.get()+"."+y[1])
    im1.show()
    Button17 = Button(window,text="Save",font="Times 12",command=save7).grid(row=15,column=1,sticky=NE)
    
def click7():
    
    label3 = Label(window,text="Enter the size in pixels( Width * Height )",font="Times 12").grid(row=13,column=1,columnspan=(3),sticky=W)
    global entry1,entry2
    entry1=Entry(window,width=10)
    entry1.grid(row=14,column=1,sticky=NW)
    label12=Label(window,text="X",width=6).grid(row=14,column=1,sticky=N)
    entry2=Entry(window,width=10)
    entry2.grid(row=14,column=1,sticky=NE)
    
    Button11 = Button(window,text="Done",command=path1,font="Times 12").grid(row=15,column=1,sticky=NW)

def loadtemplate(): 
       
        global filename
        filename = tkinter.filedialog.askopenfilename(filetypes = (("Image files", "*.jpg;*.png;*.bmp;*.gif"),("All files", "*")))
    
        entry=Label(window,text=filename,width=65,font="Times 12")
  
        entry.grid(row=1,column=2)

def path():
    
    global im
    answer = tkinter.messagebox.askquestion("Alert",message=" Is this the required path : - \n"+filename)
    if(answer=='no'):
        return;
   
    
    im=Image.open(filename)
    
    img=im.resize((800,500),Image.ANTIALIAS)
    img.save("sample.png")
    
    photo= PhotoImage(file = "sample.png")
        
    label =Label(window,image=photo,height=500,width=800)
    label.image=photo
    label.grid(row=6,rowspan=(9),column=2,columnspan=3,pady=30)
    
    
    label3 = Label(window,text="The Various operations that can be performed on the Image are : ",font="Times 12").grid(row=4,columnspan=(3),sticky=W,pady=20)
    
    Button2 = Button(window,text="1.Transpose",font="Times 12",command=click3).grid(row=6,column=1,sticky=W)
    Button3 = Button(window,text="2.Flip(Top-Bottom)",font="Times 12",command=click).grid(row=7,column=1,sticky=W)
    Button4 = Button(window,text="3.Flip(Left-Right)",font="Times 12",command=click1).grid(row=8,column=1,sticky=W)
    Button5 = Button(window,text="4.Rotate 90 Degree",font="Times 12",command=click4).grid(row=9,column=1,sticky=W)
    Button6 = Button(window,text="5.Rotate 180 Degree",font="Times 12",command=click5).grid(row=10,column=1,sticky=W)
    Button7 = Button(window,text="6.Rotate 270 Degree",font="Times 12",command=click6).grid(row=11,column=1,sticky=W)
    Button8 = Button(window,text="7.Resize",font="Times 12",command=click7).grid(row=12,column=1,sticky=W)
    Button9 = Button(window,text="Quit",font="Times 12",command=window.destroy).grid(row=15,column=4,sticky=SE)
                    
    
window=Tk()
window.title("Image Processing")
window.geometry("1980x1080")
image=PhotoImage(file="Theme.png")

labeli=Label(image=image)

labeli.image=image
labeli.place(x=0,y=0,relwidth=1.0,relheight=1.0,anchor=NW)

label1 = Label(window,text="                                                                                          Welcome to KLE TECH Image processing Page                                                                                        ",fg="yellow",bg="darkblue",font="Times 18 bold",anchor=CENTER).grid(row=0,columnspan=(6),sticky=N)
         
label2 = Label(window,text="Enter the image location",font="Times 14").grid(row=1,columnspan=(2),pady=20,sticky=W)

Label10=Label(window,width=65,text="Please Browse for the location of Image",font="Times 12").grid(row=1,column=2)

Button10 = Button(window,text="Done",command=path,font="Times 12").grid(row=1,column=5)

Button(window, text = "Browse", command = loadtemplate,font="Times 12").grid(row=1,column=4,sticky=E)
 
window.mainloop()