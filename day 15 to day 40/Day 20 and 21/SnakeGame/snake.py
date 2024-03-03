from turtle import Turtle
import time

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.change_to_snake_shape()
        self.line_moving = True
        self.last_move_time = time.time()
        self.move_count = 0
        self.delay = 0.1

    def create_snake(self):
        x = MOVE_DISTANCE
        for _ in range(3):
            x -= MOVE_DISTANCE
            self.add_segment(position=(x, 0))

    def reset(self):
        [segment.hideturtle() for segment in self.segments]
        self.segments.clear()
        self.__init__()

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.shapesize(stretch_wid=1, stretch_len=1, outline=1)
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def t_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
            self.move()
            self.line_moving = False

    def t_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
            self.move()
            self.line_moving = False

    def t_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
            self.move()
            self.line_moving = False

    def t_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
            self.move()
            self.line_moving = False

    def move(self):
        if self.move_count < 2:
            for i in range(len(self.segments) - 1, 0, -1):
                index = i
                other_turtle = self.segments[i]
                other_turtle.goto(self.segments[index - 1].position())
                other_turtle.setheading(self.segments[index - 1].heading())
            self.head.forward(MOVE_DISTANCE)
            self.line_moving = True
            self.move_count += 1

    def update_delay(self, loop_time):
        self.delay = 0.1
        self.delay -= loop_time  # Reduces the delay based on the time spent
        if self.delay < 0.05:  # Minimum limit for the delay
            self.delay = 0.05
        elif self.delay > 0.1:
            self.delay = 0.1

    def reset_delay_and_move_count(self):
        self.delay = 0.1
        self.move_count = 0

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def change_to_snake_shape(self):
        # Define the shape points for the snake's head
        self.head.shape("circle")
        self.head.penup()
        self.head.shapesize(1, 2, 1.5)  # Adjust the head size
        self.head.settiltangle(90)  # Rotate the shape if necessary
        self.head.setx(self.head.xcor() + 10)  # Adjust the position if necessary
        self.head.sety(self.head.ycor() + 10)  # Adjust the position if necessary
        self.head.settiltangle(0)  # Reset the tilt angle
