from turtle import Turtle


class Paddle(Turtle):
    def __init__(self,go_start):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.goto(go_start)



    def up(self):
       y_cor=self.ycor()+20
       self.goto(self.xcor(),y_cor)


    def down(self):
       y_cor=self.ycor()-20
       self.goto(self.xcor(),y_cor)
