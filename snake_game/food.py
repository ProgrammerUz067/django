from turtle import Turtle

import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=0.5,stretch_len=0.5)
        x_cor=random.randint(-250,250)
        y_cor=random.randint(-250,250)
        self.goto(x_cor,y_cor)

    def new_cor_food(self):
        x_cor=random.randint(-280,280)
        y_cor=random.randint(-280,280)
        self.goto(x_cor,y_cor)





