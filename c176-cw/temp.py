class score():
    def __init__ (self):
        self.score=5
    def showscore(self):
        print(self.score)
    def update_score(self):
        self.score=self.score+5
        print(self.score)
player=score()
player.update_score()
player.update_score()
player.update_score()
player.update_score()
player.update_score()