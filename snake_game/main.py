from turtle import Turtle,Screen
import time

from food import Food
from score import Score
from snake import Snake, STARTING_POSITIONS

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("brown")
screen.title("Ilon o'yini")
screen.tracer(0)
snake=Snake()
food=Food()
screen.listen()
score=Score()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")





game_is_on=True

while game_is_on:
    screen.update()
    score.update()
    time.sleep(0.2)
    snake.move()
    if snake.head.distance(food)<15:
        food.new_cor_food()
        score.add_score()



    if snake.head.xcor()>290 or snake.head.xcor()<-290 or snake.head.ycor()>290 or snake.head.ycor()<-290:
        game_is_on=False
        score.gameoff()





screen.exitonclick()

