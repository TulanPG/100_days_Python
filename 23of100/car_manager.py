from turtle import Turtle
from random import Random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
LEVEL = 0
random = Random()


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.level = 0


    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:

            new_car = Turtle("square")
            new_car.color(COLORS[random.randrange(0, 5)])
            new_car.penup()
            new_car.goto(280, random.randrange(-250, 250))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.right(180)
            self.all_cars.append(new_car)


    def car_move(self):

        for car in self.all_cars:
            new_x = car.xcor() - STARTING_MOVE_DISTANCE - MOVE_INCREMENT * self.level
            car.goto(new_x, car.ycor())


    def back_car(self):

        for car in self.all_cars:
            if car.xcor() < - 300:
                car.goto(280, random.randrange(-250, 250))



    def level_up(self):
        self.level += 1