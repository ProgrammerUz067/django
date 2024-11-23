from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.update()



    def add_score(self):
        self.score+=1
        self.clear()
        self.update()

    def update(self):
        self.write(f"Score:{self.score}", move=False, align='center', font=('Arial', 20, 'normal'))




    def gameoff(self):
        self.goto(0,0)
        self.write(f"Game Over", move=False, align='center', font=('Arial', 20, 'normal'))









