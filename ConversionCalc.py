# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 09:24:59 2022

@author: suman
"""

import tkinter
from tkinter import *

window1 = Tk()

window1.title("My GUI App")


# InstructionLabel1 = tkinter.Label(window1, text = "Click the number buttons for the length in inches, then multiply for the cm value.", font= ('helvetica',12, "bold"))
# InstructionLabel1.grid(row=0, column=0)


def buttons_click(num):
    previous_num = User_input.get()
    User_input.delete(0,END) 
    User_input.insert(0, str(previous_num) + str(num))

User_input=Entry(window1,width=60,bg="white",fg="blue",borderwidth=10)
User_input.grid(row=1,column=0,columnspan=8)




# def button_multiply():
#     first_num = User_input.get()
#     global f_num
#     global math
#     math= "multi"
#     f_num = int(first_num)
#     User_input.delete(0,END)


def button_equal(): 
    first_num = User_input.get()
    global f_num
    global math
    math= "multi"
    f_num = int(first_num)
    User_input.delete(0,END)
    
    if math=="add":
        second_num = User_input.get()
        User_input.delete(0,END)
        User_input.insert(0, f_num + int(second_num)) 
    elif math=="multi":
        User_input.delete(0,END)
        User_input.insert(0, f_num * 2.54)


def button_clear():
    User_input.delete(0,END)
    
myButton = Button(window1,text ="1",padx=20, pady=20,fg="black",bg="white", command=lambda: buttons_click(1))
myButton.grid(row=2, column=0)

myButton1 = Button(window1,text ="2",padx=20, pady=20,fg="black",bg="white", command=lambda: buttons_click(2))
myButton1.grid(row=2, column=1)

myButton2 = Button(window1,text ="3",padx=20, pady=20,fg="black",bg="white", command=lambda: buttons_click(3))
myButton2.grid(row=2, column=2)

myButton3 = Button(window1,text ="4",padx=20, pady=20,fg="black",bg="white",command=lambda: buttons_click(4))
myButton3.grid(row=3, column=0)

myButton4 = Button(window1,text ="5",padx=20, pady=20,fg="black",bg="white",command=lambda: buttons_click(5))
myButton4.grid(row=3, column=1)

myButton5 = Button(window1,text ="6",padx=20, pady=20,fg="black",bg="white",command=lambda: buttons_click(6))
myButton5.grid(row=3, column=2)

myButton6 = Button(window1,text ="7",padx=20, pady=20,fg="black",bg="white",command=lambda: buttons_click(7))
myButton6.grid(row=4, column=0)

myButton7 = Button(window1,text ="8",padx=20, pady=20,fg="black",bg="white",command=lambda: buttons_click(8))
myButton7.grid(row=4, column=1)

myButton8 = Button(window1,text ="9",padx=20, pady=20,fg="black",bg="white",command=lambda: buttons_click(9))
myButton8.grid(row=4, column=2)

myButton9 = Button(window1,text ="0",padx=20, pady=20,fg="black",bg="white",command=lambda: buttons_click(0))
myButton9.grid(row=5, column=1)

myButton10 = Button(window1,text ="C",padx=27, pady=20,fg="black",bg="white", command=button_clear)
myButton10.grid(row=2, column=3)

myButton11 = Button(window1,text ="Convert",padx=26, pady=20,fg="black",bg="white", command=button_equal)
myButton11.grid(row=4, column=3)

# myButton12 = Button(window1,text ="*2.54",padx=21, pady=20,fg="black",bg="white", command=button_multiply)
# myButton12.grid(row=3, column=3)

window1.mainloop()