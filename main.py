import turtle
from turtle import Turtle , Screen
import random
titi = Turtle()
titi.shape("turtle")
titi.color("green")
turtle.colormode(255)
def random_color():
    r=random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    my_tuple= (r,g,b)
    return my_tuple
def rotate(size):
    titi.speed(0)
    for i in range(360//size):
        titi.color(random_color())
        titi.circle(100)
        titi.setheading(titi.heading()+size)
rotate(10)
# choice=[0,90,180,270]
#
# for i in range(50):
#     titi.color(random_color())
#     titi.pensize(10)
#     titi.speed(10)
#
#     titi.right(random.choice(choice))
#     titi.forward(100)
#
#







#
# for j in range(3,10):
#     titi.color(random.choice(turtle_colors))
#     for i in range(j):
#         n=360//j
#         titi.right(n)
#         titi.forward(100)
#     titi.color()
#

screen=Screen()
screen.exitonclick()
