###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import turtle

import colorgram

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r=color.rgb.r
#     g=color.rgb.g
#     b=color.rgb.b
#     rgb_colors.append((r,g,b))
#
# print(rgb_colors)
import turtle
import random
from turtle import Turtle,Screen
turtle.colormode(255)
color_list=[ (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
titi=Turtle()
titi.speed(0)
titi.hideturtle()
titi.penup()
titi.setheading(220)
titi.forward(250)

for no_of_dots in range(1,101):
    titi.setheading(0)
    titi.dot(20,random.choice(color_list))
    titi.forward(50)

    if no_of_dots%10==0:
        titi.setheading(90)
        titi.forward(50)
        titi.setheading(180)
        titi.forward(500)

screen=Screen()
screen.exitonclick()
