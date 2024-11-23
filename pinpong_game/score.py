from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score=0
        self.r_score=0
        self.move_speed=0.2
        self.update_scoreboard()





    def update_scoreboard(self):
        self.clear()
        self.goto(-100,200)
        self.write(self.l_score,align="center",font=("Courier",50,"normal"))
        self.goto(100,200)
        self.write(self.r_score,align="center",font=("Courier",50,"normal"))
        self.draw_center_line()




    def draw_center_line(self):
        # Maydonning o'rtasidan yuqoriga chiziq chizish
        self.goto(0, 300)
        self.setheading(270)  # Yuqoriga qarab bo'lish
        self.color("white")
        self.pendown()
        self.pensize(4)
        self.forward(600)  # Maydon uzunligi
        self.penup()

        # Maydonning o'rtasidan pastga chiziq chizish
        self.goto(0, -300)
        self.setheading(270)  # Pastga qarab bo'lish
        self.pendown()
        self.forward(600)  # Maydon uzunligi
        self.penup()



    def l_point(self):
        self.l_score+=1
        self.update_scoreboard()

    def r_point(self):
        self.r_score+=1
        self.update_scoreboard()




