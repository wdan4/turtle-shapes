from turtle import * ##
import tkinter as tk ##
from tkinter import ttk ##
from functools import partial


############### ## is not needed in main , #### is debug


global command_history
command_history =[]
global undo_step
undo_step = 0

def undo():
    print("attemping undo") ####
    global undo_step
    if undo_step < len(command_history):
        print("undo successful") ####
        undo_step+=1
        bob.reset()
        screen.tracer(0)
        bob.speed(0)
        for i in range(len(command_history)-undo_step):
            command_history[i]()
        screen.update()

def redo():
    print("attemping redo") ####
    global undo_step
    if undo_step != 0:
        print("redo successful") ####
        undo_step-=1
        bob.reset()
        screen.tracer(0)
        bob.speed(0)
        for i in range(len(command_history)-undo_step):
            command_history[i]()
        screen.update()



root = tk.Tk() ##
turtle_frame = ttk.Frame(root) ##
turtle_frame.grid(row=1, column=1) ##
canvas = tk.Canvas(turtle_frame, width=400, height=400) ##
canvas.pack() ##
screen = TurtleScreen(canvas) ##
bob = RawTurtle(screen) ##

def draw_star(colour,speed,thickness,scale): ##
    bob.color(colour) ##
    bob.speed(speed) ##
    bob.pensize(thickness) ##
    for _ in range(5): ##
        bob.forward(scale) ##
        bob.right(144) ##

######## example shapes v

colour,speed,thickness,scale = "#123456",6,3,40 

undo_step = 0
command_history.append(partial(draw_star, colour,speed,thickness,scale))
draw_star(colour,speed,thickness,scale)

colour,speed,thickness,scale = "#ffff56",2,1,78

undo_step = 0
command_history.append(partial(draw_star, colour,speed,thickness,scale))
draw_star(colour,speed,thickness,scale)

colour,speed,thickness,scale = "#12674a",9,5,159

undo_step = 0
command_history.append(partial(draw_star, colour,speed,thickness,scale))
draw_star(colour,speed,thickness,scale)

######## example shapes ^

print(command_history) ####


undo_button = ttk.Button(turtle_frame, text="↶", command=undo)
undo_button.place(x=10, y=10)

redo_button = ttk.Button(turtle_frame, text="↷", command=redo)
redo_button.place(x=60, y=10)

root.mainloop() ##

""" what you need to do for it to work

def star_helper():
    global command_history
    command_history.append(partial(draw_star, colour,speed,thickness,scale))
    draw_star(colour,speed,thickness,scale)


"""
