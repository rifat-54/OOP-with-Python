class Player:
    team_run=0

    def __init__(self):
        self.run=0

    def hit_four(self):
        self.run+=4
        Player.team_run+=4
        

    def hit_six(self):
        self.run+=6
        Player.team_run+=6

    def viewRun(self):
        print("Total run: ",Player.team_run)
        print("Person run: ",self.run)


# print(Player.team_run)

p1=Player()
p2=Player()

p1.hit_four()
p1.hit_four()

p2.hit_six()

p1.viewRun()
p2.viewRun()