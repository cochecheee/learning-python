from turtle import Turtle

ALIGNMENT = "center"
FONT = "Arial,24,normal"
GAME_OVER = "Game over!!!"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.pu()
        self.goto(0,270)
        self.hideturtle()
        self.refresh_score()
    
    def refresh_score(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT,font=FONT)
    
    def increase_score(self):
        self.score += 1
        self.clear()
        self.refresh_score()

    def game_over(self):
        self.goto(0,0)
        self.write(GAME_OVER, align=ALIGNMENT,font=FONT)