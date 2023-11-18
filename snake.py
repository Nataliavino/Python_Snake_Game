from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        for i in STARTING_POSITIONS:
            new_snake = Turtle('square')
            new_snake.color('#774833')
            new_snake.penup()
            new_snake.goto(i)
            self.snake.append(new_snake)

    def add_snake(self):
        new_snake = Turtle('square')
        new_snake.color('#774833')
        new_snake.penup()
        last_snake_x = self.snake[-1].xcor()
        last_snake_y = self.snake[-1].ycor()
        new_snake.goto(last_snake_x, last_snake_y)
        self.snake.append(new_snake)

    def reset(self):
        for i in self.snake:
            i.goto(1000, 1000)
        self.snake.clear()
        self.create_snake()
        self.head = self.snake[0]

    def move(self):
        for j in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[j - 1].xcor()
            new_y = self.snake[j - 1].ycor()
            self.snake[j].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)