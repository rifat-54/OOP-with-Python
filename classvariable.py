class Player:
    team_run=0
    player_count=0

    def __init__(self):
        self.run=0    #instant variable
        Player.player_count+=1

    def hit_four(self):
        self.run+=4    #instant varible
        Player.team_run+=4     #class variable
        # self.team_run+=4
        

    def hit_six(self):
        self.run+=6
        Player.team_run+=6

    def viewRun(self):
        print("Total run: ",Player.team_run)
        print("Person run: ",self.run)
        print("Total Player: ",Player.player_count)


# print(Player.team_run)

p1=Player()
p2=Player()
p3=Player()

p1.hit_four()
p1.hit_four()

p2.hit_six()

p1.viewRun()
p2.viewRun()

print(p1.__dict__)