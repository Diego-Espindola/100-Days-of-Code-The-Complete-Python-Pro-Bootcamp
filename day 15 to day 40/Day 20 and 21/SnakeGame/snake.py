from turtle import Turtle

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

    def create_snake(self):
        x = MOVE_DISTANCE
        for _ in range(3):
            x -= MOVE_DISTANCE
            self.add_segment(position=(x, 0))

    def add_segment(self, position):
        print(position)
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.shapesize(stretch_wid=1, stretch_len=1, outline=5)
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def t_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def t_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def t_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def t_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def move(self):
        print(self.segments)
        for i in range(len(self.segments) - 1, 0, -1):
            index = i
            other_turtle = self.segments[i]
            other_turtle.goto(self.segments[index - 1].position())
            other_turtle.setheading(self.segments[index - 1].heading())
        self.head.forward(MOVE_DISTANCE)
    def extend(self):
        self.add_segment(self.segments[-1].position())
