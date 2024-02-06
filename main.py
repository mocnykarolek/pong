from turtle import Screen
from paddle import Paddle
import time
screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Pong game")
screen.tracer(0)
paddle = Paddle()
screen.listen()

screen.onkey(paddle.up, "Up")
screen.onkey(paddle.down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()


screen.exitonclick()