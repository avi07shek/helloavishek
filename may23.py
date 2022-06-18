# data = ["sunil" ,"roshan", 29]
# print(data[0:2])


# data = ["sunil","roshan",29]
# print(data)
# data.append(9)
# data.append("programming")
# print(data)


# data=["sunil","roshan",29]
# print(data)
# del data[1]
# print(data)


# data=["sunil","roshan",29]
# print(data)
# data.remove(29)
# print(data)



# data=["sunil","roshan",29]
# print(data)
# data.pop()
# print(data)

# data=["sunil","roshan",29]
# data2=["a","b",12]
# print(data+data2)



# data=("sunil","roshan",29)
# print(data)


# data =["sunil","roshan",29]
# data2=[]
# data2=data.copy()
# print(data)
# print(data2)


# data=["sunil","roshan",29]   # clear function empty the set
# data.clear()
# print(data)

# data=("sunil","roshan",29)  #python create using slice and indexing
# print(data[1])


# data=tuple(range(0,10,1))
# print(data)

# data=("sunil","roshan",29)
# print(len(data))


# data=("sunil","roshan",29,["sunil","akash",29])
# print(data)
# print(len(data))
# data[3].pop()
# print(data)
# data[3].append("master")
# print(data)
# data[3].remove("akash")
# print(data)



# from tkinter import *
# hello=Tk()
# hello.mainloop()


# from tkinter import*
# window= Tk()
# window.maxsize(width=300,height=300)
# window.minsize(width=300,height=300)

# def func():
#     print("button is clicked")

# btn = Button(window,text="Login", command=func)



# from curses import BUTTON2_CLICKED
# from re import L
# from tkinter import*
# window=Tk()
# def myclick():
#     mylabel= Label(window, text="look i clicked a button", fg="red",bg="#000099",font=50)



# from tkinter import *
# screen=Tk()
# screen.maxsize(width=500, height=300)
# screen.minsize(width=500, height=300)

# mybutton = Button(screen, text="Button1")
# mybutton.pack()


# mybutton = Button(screen, text="Button2")
# mybutton.pack()

# mybutton = Button(screen, text="Button3")
# mybutton.pack()



# mybutton = Button(screen, text="Button4")
# mybutton.pack()

# screen.mainloop()




# from distutils.util import run_2to3
# from tkinter import*
# from turtle import title

# import PIL
# root=Tk()

# def click():
#     text1="Address: "+ mytext.get('1.0'END)
#     lbl.config(text=str(text1))

# mytext=text(root,font=20,width=20,height=10)
# mytext.place(x=0,y=50)


# btn = Button(root,text="click me",font=30,command=click)
# btn.place(x=400,y=300)

# lbl = Label(root,text="",font=30)
# lbl.place(x=200,y=300)

# root.mainloop()


# #Adding frames to program

# from tkinter import *
# window=Tk()
# frame = LabelFrame(window,text="This is my frame",padx=10,pady=10)

# #Radio button

# from tkinter import*

# window=Tk()
# def add():
#     print(var.get())
# var = IntVar



# #radio Button
# from tkinter import *
# window = Tk()
# def add():
#     selection = "you have selected the option" + str(var.get())
#     label.config(text=selection)
# var = IntVar()
# r1 = Radiobutton(window,text="option 1",variable=var,value=1,command=add)
# r1.pack(anchor=W)
# r2 = Radiobutton(window)   


# from tkinter import *
# # # import messagebox
# top=Tk()
# def add():
#     label config(text=checkVar1.get())
# CheckVar1 = IntVar()


# C1 = Checkbutton(top, 
# text = "Music", variable = CheckVar



# from tkinter import *
# from PIL import Image, ImageTk
# window = Tk()
# window.title("LOGIN")
# #define image
# my_image = ImageTk.PhotoImage(Image.open("police.png"))
# #create a label
# my_label = Label(image=my_image)
# my_label.pack()

# #button quit option
# button-quit = Button(window,text="Exit",command=window.quit,width=)
# button_quit.pack()
# window.mainloop()




# from tkinter import *
# from PIL import Image, ImageTk
# window = Tk()
# window.title("LOGIN")
# #define image
# my_image =Image.open("")
# resized_image = my_iamge.resize((300,250))
# converted_image=ImageTk.PhotoImage(resized_image)
# mylabel=Label(window,image=converted_image)
# mylabel.pack()

# window.mainloop()


# from tkinter import *
# from tkinter import messagebox
# root = Tk()

# def popup():
#     messagebox.showinfo("This is my popup","hello world")

# btn = button(root,text="popup", command=popup).pack()

# root.mainloop()


# from tkinter import *
# from tkinter import messagebox
# root = Tk()

# def popup():
#     response = messagebox.askyesno("This is popup", "hello world")
#     Label(root,text=response).pack()

#     if response ==1:
#         Label(root,text="Clicked Yes").pack()
#     else:
#         Label(root,text="Clicked No").pack()


# btn = Button(root,tex="popup", command=popup).pack()
# root.mainloop()



# from tkinter import * 
# from PIL import Image,ImageTk
# root = Tk()
# def open():
#     global my_img
#     top = Toplevel()
#     my_img = ImageTk.PhotoImage(Image.open("eaglee.png"))
#     my_label = Label(top,image=my_img)
#     mylabel_.pack(pady=10)
#     btn = Button( top,text="Close window", command= top.destroy)
#     btn.pack()

# btnn = Button(root,text="open",command=open)
# btnn.pack()
# root.mainloop()


# from tkinter import * 
# root=Tk()
# root.geometry("200*200")
# def show():
#     label.config(text=clicked.get())
#     option={"monday","tuesday","wednesday","thursday","friday","saturday"}

# clicked = StringVar()
# clicked.set("Monday")

# drop = OptionMenu ( root, clicked, "options")
# drop.pack()



# button= Button (root , text = ")


# from tkinter import * 

# root=Tk()

# #defning title of the project
# root.title("Simple Calculator")

# e= Entry(root, width=35, borderwidth=5)
# e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# def button_click(number):
#     current = e.get()
#     e.delete(0,END)
#     e.insert(0,str(current)+str(number))

# def button_clear():
#     e.delete(0,END)

# def button_add():
#     first_number = e.get()
#     global f_num
#     f_num = int(first_number)
#     e.delete(0,END)

# def button_equal():
#     second_number = e.get()
#     e.delete(0,END)
#     e.insert(0, f_num + int(second_number))

# #definng the button

# button_1 = Button(root, text="1", padx=40, pady=20, command=lambda:button_click(1))

# button_2 = Button(root, text="2", padx=40, pady=20, command=lambda:button_click(2))


# button_3 = Button(root, text="3", padx=40, pady=20, command=lambda:button_click(3))


# button_4 = Button(root, text="4", padx=40, pady=20, command=lambda:button_click(4))


# button_5 = Button(root, text="5", padx=40, pady=20, command=lambda:button_click(5))


# button_6 = Button(root, text="6", padx=40, pady=20, command=lambda:button_click(6))


# button_7 = Button(root, text="7", padx=40, pady=20, command=lambda:button_click(7))


# button_8 = Button(root, text="8", padx=40, pady=20, command=lambda:button_click(8))


# button_9 = Button(root, text="9", padx=40, pady=20, command=lambda:button_click(9))


# button_0 = Button(root, text="0", padx=40, pady=20, command=lambda:button_click(0))


# button_add = Button(root, text="+", padx=39, pady=20, command=button_add)


# button_equal = Button(root, text="=", padx=91, pady=20, command=button_equal)


# button_clear = Button(root, text="clear", padx=79, pady=20, command=button_clear)





# #putting button on the screen

# button_1.grid(row= 3, column = 0)
# button_2.grid(row= 3, column = 1)
# button_3.grid(row= 3, column = 2)

# # button_4.grid(row= 2, column = 0)
# button_5.grid(row= 2, column = 1)
# button_6.grid(row= 2, column = 2)

# button_7.grid(row= 1, column = 0)
# button_8.grid(row= 1, column = 1)
# button_9.grid(row= 1, column = 2)


# button_0.grid(row = 4, column = 0)
# button_clear.grid(row = 4, column = 1, columnspan = 2)
# button_add.grid(row = 5, column = 0)
# button_equal.grid(row = 5 , column = 1, columnspan= 2)

# root.mainloop()






from tkinter import *

root=Tk()
root.title("Simple Calculator")
e= Entry(root,width=35, borderwidth=5)
e.grid(row=0,column=0, columnspan=3, padx=10,pady=10)
def button_click(number):
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))

def button_clear():
    e.delete(0,END)

def button_add():
    first_number=e.get()
    
    compute="addition"
    f_num=int(first_number)
    e.delete(0,END)


def button_subtract():
    first_number=e.get()
    compute="subtraction"
    f_num=int(first_number)
    e.delete(0,END)


def button_multiply():
    first_number=e.get()
    compute="multipilcation"
    f_num=int(first_number)
    e.delete(0,END)


    
def button_division():
    first_number=e.get()
    compute="division"
    f_num=int(first_number)
    e.delete(0,END)

    

root.mainloop()
   




































                 


