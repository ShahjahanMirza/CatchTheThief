from turtle import Turtle

STARTING_POSITION = (0, -500)
MOVE_DISTANCE = 11
FINISH_LINE_Y = 490
# MOVE_DISTANCE = 16
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Thief(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.color('red')
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

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
    
    def go_to_start(self):
        self.goto(STARTING_POSITION)
        
        
