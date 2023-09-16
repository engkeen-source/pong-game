from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from time import sleep

WIDTH = 800
HEIGHT = 600

# Create a screen
screen = Screen()
screen.setup(WIDTH, HEIGHT)
screen.bgcolor('black')
screen.title('My Pong Game')
screen.tracer(0)

# Create a paddle
r_paddle = Paddle((380, 0))
l_paddle = Paddle((-380, 0))

# Create a ball
ball = Ball()
x_limit = screen.window_width() / 2 - 20
y_limit = screen.window_height() / 2 - 20

# Create a scoreboard
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, 'Up')
screen.onkey(r_paddle.go_down, 'Down')
screen.onkey(l_paddle.go_up, 'w')
screen.onkey(l_paddle.go_down, 's')

game_is_on = True
sleep_in_sec = 0.1
while game_is_on:
    screen.update()
    ball.move()
    sleep(ball.move_speed)

    # Detect collision with wall
    if ball.ycor() > y_limit or ball.ycor() < -y_limit:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > x_limit-20 or ball.distance(l_paddle) < 50 and ball.xcor() < -(x_limit-20):
        ball.bounce_x()

    # Detect R paddle misses
    if ball.xcor() > x_limit:
        ball.reset_position()
        scoreboard.l_point()

    # Detect L paddle misses
    if ball.xcor() < -x_limit:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
