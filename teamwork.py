import tkinter as tk
from turtle import *
from tkinter import colorchooser
from tkinter.ttk import *


colour = "#000000"

screen = Screen()

root = screen._root

root.state('zoomed')
bob=Turtle()
screen.bgcolor("#FFFFFF")

bob.fd(100)
bob.shape('turtle')

def pickbgcolour():
    colourbg = colorchooser.askcolor()
    colourbg = colourbg[1]
    screen.bgcolor(colourbg)

def pickColour():
    colour = colorchooser.askcolor()
    colour = colour[1]
    butCol2.config(bg=colour)
    bob.color(colour)
    # colour = colour.split('#')[-1].strip()
    # print(colour)

def drawImg():
    bob.fd(40)
   


def clearImg():
    bob.clear()
    bob.penup()
    bob.setpos(0,0)
    bob.pendown()


def ccw():
    bob.left(90)

def cw():
    bob.right(90)

canvas = screen.getcanvas()

# SIDE

# BUTTONS

butDraw = Button(canvas.master, text="Draw Line", command=lambda: drawImg())
butDraw.place(x=20, y=20)

butClear = Button(canvas.master, text="Clear Image", command=lambda: clearImg())
butClear.place(x=20, y=50)

butCol = Button(canvas.master, text="Colour:", command=lambda: pickColour(), width=6)
butCol.place(x=20, y=80)

butCol2 = tk.Button(canvas.master, background=colour, command=lambda: pickColour(), width=2, height=1)
butCol2.place(x=70, y=80)

butCol3 = Button(canvas.master, text="BG Colour", command=lambda: pickbgcolour(), width=8)
butCol3.place(x=20, y=110)




ccwb = Button(canvas.master, text="90 acw", command=lambda: ccw(), width=8)
ccwb.place(x=100, y=20)

cwb = Button(canvas.master, text="90 cw", command=lambda: cw(), width=8)
cwb.place(x=160, y=20)








# SLIDERS

slidersc = tk.Scale(canvas.master, label="Scale", from_ =0, to =10, bg="#1192E9", orient='horizontal')
slidersc.place(x=20, y=140)

slidertn = tk.Scale(canvas.master, label="Thickness", from_ =0, to =10, bg="#1192E9", orient='horizontal', variable=bob.pensize())
slidertn.place(x=20, y=210)


#TOP

#BUTTONS



star = Button(canvas.master, text="Star", command=lambda: pickColour(), width=6)
star.place(x=760, y=20)

polygon = Button(canvas.master, text="Polygon", command=lambda: pickColour(), width=8)
polygon.place(x=860, y=20)

chat = Button(canvas.master, text="Chat", command=lambda: pickColour(), width=6)
chat.place(x=960, y=20)

circles = Button(canvas.master, text="Circles", command=lambda: pickColour(), width=6)
circles.place(x=1060, y=20)

# RIGHT

fram1 = Frame(canvas.master, width=200, height=450, relief="raised")
fram1.place(x=1600, y=100)




fram2 = Frame(canvas.master)

fram3 = Frame(canvas.master)

fram4 = Frame(canvas.master)




screen.mainloop()