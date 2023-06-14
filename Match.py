import math
import random
import Team
class Match:
    def __init__(self, team1: Team, team2: Team):
        self.team1 = team1
        self.team2 = team2
    def winner(self):
        diffrence = math.fabs(self.team1.avrage_overall()-self.team2.avrage_overall())
        if diffrence <= 7:
            prob1 = 45 - diffrence*5
            prob2 = 45 + diffrence*5
            prob_draw = 10

        else:
            prob2 = 90
            prob1 = 5
            prob_draw = 5
        rand_num = random.uniform(0, 100)
        if self.team1.avrage_overall() >= self.team2.avrage_overall():
            if rand_num < prob2:
                self.team1.add_points(3)
                self.team1.wins += 1
                self.team2.losses += 1
            elif rand_num < prob1 + prob2:
                self.team2.add_points(3)
                self.team2.wins += 1
                self.team1.losses += 1
            else:
                self.team1.draws += 1
                self.team2.draws +=1
                self.team1.add_points(1)
                self.team2.add_points(1)
        else:
            if rand_num < prob2:
                self.team2.add_points(3)
                self.team2.wins +=1
                self.team1.losses += 1
            elif rand_num < prob1 + prob2:
                self.team1.add_points(3)
                self.team1.wins += 1
                self.team2.losses += 1
            else:
                self.team1.draws += 1
                self.team2.draws +=1
                self.team1.add_points(1)
                self.team2.add_points(1)
