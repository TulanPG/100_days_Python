from turtle import Screen
import time
from paddle import Paddle
from ball import Ball

basic_pos_left = (-350, 0)
basic_pos_right = (350, 0)
ball_speed = 3

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My Snake Game - Tulan vol.2 Turtle")
screen.tracer(0)

r_paddle = Paddle(basic_pos_right)
l_paddle = Paddle(basic_pos_left)
ball = Ball(ball_speed)

screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.01)
    ball.ball_move()

    # detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect goal
    if ball.xcor() > 380 or ball.xcor() < -380:
        print("goal")
        ball.goto(0, 0)
        ball.bounce_x()

    # detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330 or ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_x()

screen.exitonclick()
