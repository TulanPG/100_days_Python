from turtle import Turtle
from random import Random

random = Random()


class Ball(Turtle):

    def __init__(self, ball_speed):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape("circle")
        self.x_move = ball_speed
        self.y_move = ball_speed

    def ball_move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
