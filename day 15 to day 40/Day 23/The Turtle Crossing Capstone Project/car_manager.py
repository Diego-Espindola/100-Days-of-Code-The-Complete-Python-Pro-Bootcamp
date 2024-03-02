from turtle import Turtle
import random as r

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
X_RANGE = 280
X_INITIAL_RANGE = (8, 15)
Y_RANGE = (-10, 13)


class CarCreator(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color(r.choice(COLORS))
        self.penup()
        self.setheading(180)
        self.shapesize(stretch_len=2)
        self.goto(position)


class CarManager:
    def __init__(self):
        self.cars = []
        self.created_car = False
        self.x_range = X_RANGE

    def create_car(self, quantity=1, x_range=X_RANGE):
        for _ in range(quantity):
            self.created_car = True
            position = self.get_new_position(x_range=x_range)
            while not self.free_position(position):
                position = self.get_new_position(x_range=x_range)
            self.cars.append(CarCreator(position))

    def start_game(self):
        for i in range(7):
            self.create_car(x_range=X_INITIAL_RANGE)
        self.created_car = True

    def move(self):
        for car in self.cars[:]:
            car.forward(MOVE_DISTANCE)
            if car.xcor() < -280:
                car.hideturtle()
                self.cars.remove(car)
                del car

    def car_crash(self, turtle):
        for car in self.cars:
            if abs(car.xcor() - turtle.xcor()) < 20 and abs(car.ycor() - turtle.ycor()) < 20:
                return True
        return False

    def free_position(self, position):
        """Return True if the position is free to place a car"""
        for car in self.cars:
            if abs(car.ycor() - position[1]) <= 40 and abs(car.xcor() - position[0]) <= 40:
                return False
        return True

    @staticmethod
    def get_new_position(x_range):
        if isinstance(x_range, tuple):
            x_cord = r.randint(x_range[0], x_range[1]) * 20
        else:
            x_cord = X_RANGE
        y_cord = r.randint(Y_RANGE[0], Y_RANGE[1]) * 20
        return x_cord, y_cord

    @staticmethod
    def increase_move_distance():
        global MOVE_DISTANCE
        MOVE_DISTANCE += MOVE_INCREMENT

    def clean_cars(self):
        for car in self.cars:
            car.hideturtle()
            del car
        self.cars.clear()

    def next_game(self):
        self.clean_cars()
        self.increase_move_distance()
