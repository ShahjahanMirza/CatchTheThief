from turtle import Turtle


STARTING_POSITION = (0, -580)
# MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
MOVE_DISTANCE = 12
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Catcher(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("blue")
        self.setheading(90)
        self.go_to_start()

    def move(self):
        self.forward(MOVE_DISTANCE)

    def up(self):
        if self.heading() != DOWN:
            self.setheading(UP)

    def down(self):
        if self.heading() != UP:
            self.setheading(DOWN)

    def left(self):
        if self.heading() != RIGHT:
            self.setheading(LEFT)

    def right(self):
        if self.heading() != LEFT:
            self.setheading(RIGHT)

    def go_to_start(self):
        self.goto(STARTING_POSITION)
