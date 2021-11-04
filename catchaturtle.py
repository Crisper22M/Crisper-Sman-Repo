# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand
#-----game configuration---

trtl.bgcolor("turquoise")

fill_color = "green"
size = 3
shape = "turtle"
score = 0

#-----initialize turtle-----
shen = trtl.Turtle()
shen.penup()
shen.fillcolor(fill_color)
shen.shapesize(size)
shen.shape(shape)

#-----game functions--------

def shen_clicked(x, y):
    change_position()
def change_position():
    new_xpos = rand.randint(-200,200)
    new_ypos = rand.randint(-150,150)
    shen.goto(new_xpos,new_ypos)
def update_score():
    

#make background pieces 
shen.goto(-200,50)
shen.pendown()
shen.pencolor("black")
shen.fillcolor("green")
shen.begin_fill()
shen.circle(150,360,5)
shen.end_fill()
shen.penup()

#-----events----------------

wn = trtl.Screen()
shen.onclick(shen_clicked)
wn.mainloop()



























































































































