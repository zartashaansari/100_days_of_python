import random
from turtle import Turtle,Screen
screen=Screen()
screen.setup(width=500, height=400)
user_bet=screen.textinput("Make your bet","Please enter the color of the color you want tto put a bet on")
color_list=["red","green","purple","yellow","orange","blue"]
players=[]
x = -230
y = 160
game_on=False
for i in range(6):
    tim=Turtle()
    tim.penup()
    tim.shape("turtle")
    tim.color(color_list[i])
    tim.goto(x,y)
    players.append(tim)
    y-=50
if user_bet:
    game_on=True
while game_on:

    for a_turtle in  players:
        if a_turtle.xcor()>230:
            winning_color=a_turtle.pencolor()
            game_on = False
            if winning_color==user_bet:

                print(f"You won!.The {winning_color} turtle is the winner.")
            else:

                print(f"You Lose!.The {winning_color} turtle is the winner.")
        a_turtle.forward(random.randint(0,10))

screen.exitonclick()