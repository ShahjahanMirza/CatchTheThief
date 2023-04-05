from turtle import Turtle, Screen
import time
from thief import Thief
from catcher import Catcher
from scoreboard import Scoreboard
from obstacles import Obstacles
import turtle

# background road
image = "big_road.gif"
# -------------------------------

# screen settings
screen = turtle.Screen()
screen.setup(width=1200, height=1000)
screen.title("Thief Catching on Road")
screen.bgcolor("white")
screen.tracer(0)
screen.addshape(image)
turtle.shape(image)
# --------------------------------

# thief and Catcher defined with their movements
thief = Thief()
catcher = Catcher()
scoreboard = Scoreboard()
obstacles = Obstacles()

screen.listen()
screen.onkey(thief.up, "Up")
screen.onkey(thief.down, "Down")
screen.onkey(thief.left, "Left")
screen.onkey(thief.right, "Right")
screen.onkey(catcher.up, "w")
screen.onkey(catcher.down, "s")
screen.onkey(catcher.left, "a")
screen.onkey(catcher.right, "d")
# ------------------------------------------


# game running
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    # -----------------------

    # creating obstacles and moving them
    obstacles.create_obstacles()
    obstacles.move_obstacles()
    # -------------------

    # moving thief and catcher on screen
    thief.move()
    catcher.move()
    # -------------------

    # detecting collision with obstacles
    for obstacle in obstacles.all_obstacles:
        if obstacle.distance(thief) < 19:
            game_is_on = False
            scoreboard.game_over()
    # --------------------

    # detecting if catcher has caught the thief
    if catcher.distance(thief) < 19:
        game_is_on = False
        scoreboard.game_over()
    # -------------------

    # detecting if thief has crossed the road
    # if thief.ycor() > 490:
    if thief.is_at_finish_line():
        scoreboard.increase_score()
        catcher.go_to_start()
        thief.go_to_start()
        obstacles.level_up()
        time.sleep(1)
    # -------------------

# exits screen when clicked
screen.exitonclick()
# ----------------------
