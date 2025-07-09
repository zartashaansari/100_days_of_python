from turtle import Turtle,Screen
tim=Turtle()
screen=Screen()
screen.listen()

def mov_forward():
    tim.forward(100)
def mov_back():
    tim.backward(100)
def clockwise():
    tim.setheading(tim.heading()-10)
def anti_clockwise():
    tim.setheading(tim.heading()+10)
screen.onkey(key="w",fun=mov_back)
screen.onkey(key="d",fun=clockwise)
screen.onkey(key="s",fun=mov_forward)
screen.onkey(key="a",fun=anti_clockwise)
screen.onkey(key="c",fun=tim.reset)
screen.exitonclick()