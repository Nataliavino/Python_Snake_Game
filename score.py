from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Arial', 20, 'bold')


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('black')
        self.goto(0, 270)
        self.score = 0
        with open('score.txt') as file:
            self.high_score = int(file.read())
        self.show_score()

    def add_score(self):
        self.score += 1
        self.show_score()

    def reset(self):
        if self.score > self.high_score:
            with open('score.txt', mode='w') as file:
                file.write(str(self.score))
        self.score = 0
        self.show_score()

    def show_score(self):
        self.clear()
        self.write(f'Score: {self.score} High Score: {self.high_score}', False, ALIGNMENT, FONT)