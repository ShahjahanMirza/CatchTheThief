from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class Obstacles(Turtle):
    def __init__(self):
        super().__init__()
        self.all_obstacles = []
        self.obstacle_speed = STARTING_MOVE_DISTANCE

    def create_obstacles(self):
        random_chance = random.randint(1, 5)
        if random_chance == 1:
            new_obs = Turtle("square")
            new_obs.shapesize(stretch_wid=1, stretch_len=2)
            new_obs.penup()
            new_obs.color(random.choice(COLORS))
            random_y = random.randint(-440, 440)
            new_obs.goto(550, random_y)
            self.all_obstacles.append(new_obs)

    def move_obstacles(self):
        for obs in self.all_obstacles:
            obs.backward(self.obstacle_speed)

    def level_up(self):
        self.obstacle_speed += STARTING_MOVE_DISTANCE
