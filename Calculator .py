from tkinter import *
from PIL import Image, ImageTk

root=Tk()
root.geometry('287x495+1000+130')
root.title('Calculator')
#set width and height
canvas=Canvas(root)
canvas2=Canvas(root)
#give this image path. image should be in png format.
#,width=300,height=300
#Example: "C:\\Users\\ASUS\\OneDrive\\Pictures\\image.png"
image=Image.open("py.jpg")
image.thumbnail((500,500))
image=ImageTk.PhotoImage(image)
canvas.create_image(0,0,anchor=NW,image=image)
canvas.place(x=0)
#########
image2=Image.open("py.jpg")
image2.thumbnail((500,500))
image2=ImageTk.PhotoImage(image2)
canvas2.create_image(0,0,anchor=NW,image=image2)
canvas2.place(x=0, y=250)

root.resizable(False,False)
#root.configure(bg='#e64d00')
entry = Entry(root , font='300px' ,bd=13 )
entry.place( x=5, y=20, width='278'  ,height='100' )
#canvas.create_image(0,0,anchor=NW,image=image)
#canvas.pack()

def click(num):
    current= entry.get()
    entry.delete(0,END)   
    entry.insert(0,str(current)+str(num))

def clear():
    entry.delete(0,END)
        
def sub():
    v=entry.get()
    global f_num
    global match
    match="sub"
    try :
        f_num=int(v)
    except :
        pass
    entry.delete(0,END)
      
def add():
    v=entry.get()
    global f_num
    global match
    match="add"
    try :
        f_num=int(v)
    except :
        pass
    entry.delete(0,END)
    
def mlt():
    v=entry.get()
    global f_num
    global match
    match="mlt"
    try :
        f_num=int(v)
    except :
        pass
    entry.delete(0,END)

def dvd():
    v=entry.get()
    global f_num
    global match
    match="dvd"
    try :
        f_num=int(v)
    except :
        pass
    entry.delete(0,END)

def mod():
    v=entry.get()
    global f_num
    global match
    match="mod"
    try :
        f_num=int(v)
    except :
        pass
    entry.delete(0,END)
            
def equal():
    s_num=entry.get()
    entry.delete(0,END)
    try :
        if match=="add":
            entry.insert(0,f_num + int(s_num))    
        if match=="sub":
            entry.insert(0,f_num - int(s_num))
        if match=="mlt":
            entry.insert(0,f_num * int(s_num))    
        if match=="dvd":
            entry.insert(0,f_num / int(s_num))
        if match=="mod":
            entry.insert(0,f_num % int(s_num))    
    except :
        pass

btn1  =Button(root , text="+/-",padx=25, pady=21 ,font='bold' ,activebackground='#0059b3')                           .place(x=5  ,y=420)
btn2  =Button(root , text="0" , padx=24, pady=21 ,font='bold' ,activebackground='#0059b3',command= lambda: click(0)).place(x=70 ,y=420) 
btn3  =Button(root , text="." , padx=26, pady=21 ,font='bold' ,activebackground='#0059b3',command= lambda: click(1)).place(x=135,y=420)
btn4  =Button(root , text="1" , padx=24, pady=21 ,font='bold' ,activebackground='#0059b3',command= lambda: click(1)).place(x=5  ,y=352)
btn5  =Button(root , text="2" , padx=24, pady=21 ,font='bold' ,activebackground='#0059b3',command= lambda: click(2)).place(x=70 ,y=352)
btn6  =Button(root , text="3" , padx=24, pady=21 ,font='bold' ,activebackground='#0059b3',command= lambda: click(3)).place(x=135,y=352)
btn7  =Button(root , text="4" , padx=24, pady=21 ,font='bold' ,activebackground='#0059b3',command= lambda: click(4)).place(x=5  ,y=284)
btn8  =Button(root , text="5" , padx=24, pady=21 ,font='bold' ,activebackground='#0059b3',command= lambda: click(5)).place(x=70 ,y=284)
btn9  =Button(root , text="6" , padx=24, pady=21 ,font='bold' ,activebackground='#0059b3',command= lambda: click(6)).place(x=135,y=284)
btn10 =Button(root , text="7" , padx=24, pady=21 ,font='bold' ,activebackground='#0059b3',command= lambda: click(7)).place(x=5  ,y=213)
btn11 =Button(root , text="8" , padx=24, pady=21 ,font='bold' ,activebackground='#0059b3',command= lambda: click(8)).place(x=70 ,y=213)
btn12 =Button(root , text="9" , padx=24, pady=21 ,font='bold' ,activebackground='#0059b3',command= lambda: click(9)).place(x=135,y=213)  
btn13 =Button(root , text="=" , padx=28, pady=58 ,font='bold' ,bg='#85adad',activebackground='#0059b3',command= lambda: equal()) .place(x=206,y=345)
btn14 =Button(root , text="-" , padx=30, pady=20 ,font='bold' ,activebackground='#0059b3',command= lambda: sub())   .place(x=206,y=277)  
btn15 =Button(root , text="+" , padx=29, pady=20 ,font='bold' ,activebackground='#0059b3',command= lambda: add())   .place(x=206,y=206)   
btn16 =Button(root , text="C" , padx=28, pady=26 ,font='bold' ,activebackground='#0059b3',command= lambda: clear()) .place(x=205,y=127)
btn17 =Button(root , text="x" , padx=21, pady=27 ,font='bold' ,activebackground='#0059b3',command= lambda: mlt())   .place(x=75 ,y=127)
btn18 =Button(root , text="%" , padx=22, pady=27 ,font='bold' ,activebackground='#0059b3',command= lambda: mod())   .place(x=5  ,y=127)
btn19 =Button(root , text="/" , padx=26, pady=27 ,font='bold' ,activebackground='#0059b3',command= lambda: dvd())   .place(x=136,y=127)

root.mainloop()




