

from turtle import *
import turtle as tt
import random

global colourbg
colourbg = tt.bgcolour('black') #background color picking function


tt.pensize(2)
tt.speed(0)
tt.hideturtle()

colors = ["white", "yellow", "magenta", "cyan", "lime", "orange", "hotpink", "red", "blue"]

global is_drawing
is_drawing = False


colors = ["white", "yellow", "magenta", "cyan", "lime", "orange", "hotpink", "red", "blue"]
is_drawing = False

def star():
    for i in range(5):
        tt.forward(200)
        tt.left(144)
        
def small_star():
    for i in range(5):
        tt.forward(100)
        tt.left(144)

def make_circle():
    tt.circle(150, 360)
    tt.left(30)

def flower():
    small_star()
    make_circle()

def single_flower():
    setpos(0,0)
    flower()
        
         


def draw_flowers():
    global is_drawing
    if is_drawing:
        return
    
    is_drawing = True
    tt.clear()
    

    for i in range(25):
        tt.color(random.choice(colors))
        

        tt.penup()
        rpos = random.randrange(-400, 400, 10)
        dpos = random.randrange(-400, 400, 10)
        tt.setpos(rpos, dpos)
        tt.pendown()
        
     
        for n in range(12):
            star()
            make_circle()
            
    is_drawing = False

def draw_single_flowers():
    global is_drawing
    if is_drawing:
        return
    
    is_drawing = True
    tt.clear()
    

    tt.color(random.choice(colors))
        

    tt.penup()
    rpos = 0
    dpos = 0
    tt.setpos(rpos, dpos)
    tt.pendown()
        
     
    for n in range(12):
        small_star()
        make_circle()
            
    is_drawing = False


def draw_circles():
    global is_drawing
    if is_drawing:
        return
    
    is_drawing = True 
    tt.clear()
    for i in range(36):
        tt.color("purple")
        tt.circle(100)
        tt.left(10)
    is_drawing = False 

def draw_squares():
    global is_drawing
    if is_drawing:
        return
    
    is_drawing = True
    tt.clear()
    for i in range(18):
        tt.color("yellow")
        for n in range(4):
           tt.forward(100)
           tt.left(90)
        tt.left(20)
    is_drawing = False


tt.listen()
tt.onkey(draw_circles, "c") 
tt.onkey(draw_squares, "s")
tt.onkey(draw_flowers, "f")
tt.onkey(draw_single_flowers, "i") 

tt.mainloop()




