STARTING_POSITIONS=[(0,0),(-20,0),(-40,0)]



from turtle import Turtle
class Snake:
    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head=self.segments[0]

    def create_snake(self):
        for positions in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.penup()
            new_segment.color("white")
            new_segment.goto(positions)
            self.segments.append(new_segment)


    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            x_cor = self.segments[seg - 1].xcor()
            y_cor = self.segments[seg - 1].ycor()
            self.segments[seg].goto(x_cor, y_cor)
        self.head.forward(20)


    def up(self):
        self.head.setheading(90)

    def down(self):
        self.head.setheading(-90)

    def left(self):
        self.head.setheading(-180)

    def right(self):
        self.head.setheading(0)





    def Up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)

    def Down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)

    def Left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)

    def Right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)


