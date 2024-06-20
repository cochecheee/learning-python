from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.pu()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("yellow")
        # dont need to wait create foot and move to specific position
        self.speed("fastest")
        self.refresh_food()

    def refresh_food(self):
        self.goto(random.randint(-280,280),random.randint(-280,280))
