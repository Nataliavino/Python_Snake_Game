import time
from turtle import Screen
from food import Food
from score import Score
from snake import Snake

screen = Screen()
screen.setup(600, 600)
screen.bgpic('bg.png')
screen.title('My Snake Game')
screen.tracer(0)

score = Score()
snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up,'Up')
screen.onkey(snake.down,'Down')
screen.onkey(snake.left,'Left')
screen.onkey(snake.right,'Right')

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        score.add_score()
        snake.add_snake()

    # Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.ycor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() < -290:
        score.reset()
        snake.reset()

    # Detect collision with tail
    for i in snake.snake[1:]:
        if snake.head.distance(i) < 10:
            score.reset()
            snake.reset()

screen.exitonclick()