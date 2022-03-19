import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


player = Player()

screen.listen()
screen.onkey(player.move_up, "Up")
screen.onkey(player.move_down, "Down")
screen.onkey(player.move_left, "Left")
screen.onkey(player.move_right, "Right")


car = CarManager()

game_is_on = True
while game_is_on:
    time.sleep(0.1)

    #finish lane detector
    if player.ycor() >= 280:
        player.finish_line()
        car.level_up()
        print(car.level)

    #creating cars
    car.create_car()
    car.car_move()

    screen.update()

