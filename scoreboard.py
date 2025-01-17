from turtle import Turtle


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        with open ("data.txt") as data:
            self.highscore= int(data.read())
   
        self.penup()
        self.color("white")
        self.goto(0,270)
        self.hideturtle()
        self.update_scoreboard()
      
    
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} | High Score: {self.highscore} ", align="center", font=("Arial", 24, "normal"))
        
    def reset (self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open ("data.txt",mode="w") as data:
                data.write(f"{self.highscore}")
        self.score = 0
        self.update_scoreboard()
        
    def addscore(self):
        
        self.score += 1
        self.update_scoreboard()
        
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", align="center", font=("Arial", 24, "normal"))