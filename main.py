from turtle import Screen, Turtle
from paddle import Paddle

# Create a screen
screen = Screen()
screen.setup(800, 600)
screen.bgcolor('black')
screen.title('My Pong Game')
screen.tracer(0)

# Create a paddle
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))


screen.listen()
screen.onkey(r_paddle.go_up, 'Up')
screen.onkey(r_paddle.go_down, 'Down')
screen.onkey(l_paddle.go_up, 'w')
screen.onkey(l_paddle.go_down, 's')

game_is_on = True
while game_is_on:
    screen.update()


screen.exitonclick()
