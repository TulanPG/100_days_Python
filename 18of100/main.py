import turtle
from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
screen = Screen()


def move_forwards():
    tim.forward(10)


def move_back():
    tim.backward(10)


def right():
    tim.right(10)


def left():
    tim.left(10)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_back)
screen.onkey(key="d", fun=right)
screen.onkey(key="a", fun=left)
screen.onkey(key="c", fun=clear)

screen.exitonclick()
