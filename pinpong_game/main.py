from turtle import Turtle,Screen
import time

import score
from score import Scoreboard
from paddle import Paddle
from ball import Ball
import time


screen=Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Ping Pong game")
screen.tracer(0)




r_paddel=Paddle((380,0))
l_paddel=Paddle((-380,0))
ball=Ball()




screen.listen()
screen.onkey(r_paddel.up,"Up")
screen.onkey(r_paddel.down,"Down")
screen.onkey(l_paddel.up,"w")
screen.onkey(l_paddel.down,"s")





game_is_on=True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounse_y()

    if (ball.distance(r_paddel)<50 and ball.xcor()>300) or (ball.distance(l_paddel)<50 and ball.xcor()<-300):
        ball.bounse_x()

    if ball.xcor()>380:
        ball.reset_position()
        score.l_point()


    if ball.xcor()<-380:
        ball.reset_position()
        score.r_point()




screen.exitonclick()



