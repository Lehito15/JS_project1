import csv
import Match
import Player
import Team


class League:
    def __init__(self, teams, user=None, current_round=1, my_team=None):
        self.teams = teams
        self.schudle = self.make_schedule()
        self.current_round = current_round
        self.my_team = my_team
        self.user = user
        self.team_dict_objects = {}
        self.team_dict = {
            1: 'Arsenal',
            2: 'Aston Villa',
            3: 'Brentford',
            4: 'Brighton',
            5: 'Fulham',
            6: 'Chelsea',
            7: 'Crystal Palace',
            8: 'Everton',
            9: 'Leeds United',
            10: 'Leicester City',
            11: 'Liverpool',
            12: 'Manchester City',
            13: 'Manchester Utd',
            14: 'Newcastle Utd',
            15: 'Nott\'m Forest',
            16: 'Southampton',
            17: 'Spurs',
            18: 'AFC Bournemouth',
            19: 'West Ham',
            20: 'Wolves'
        }
        self.team_dict2 = {value: key for key, value in self.team_dict.items()}

    def make_dict(self):
        dict = {team.code: team for team in self.teams}
        self.team_dict_objects = dict

    def make_round(self, round):
        # generate list of teams
        lst = list(range(1, 20 + 1))
        # rotate
        round %= (20 - 1)  # clip to 0 .. num_teams - 2
        if round:  # if day == 0, no rotation is needed (and using -0 as list index will cause problems)
            lst = lst[:1] + lst[-round:] + lst[1:-round]
        # pair off - zip the first half against the second half reversed
        half = 20 // 2
        return list(zip(lst[:half], lst[half:][::-1]))

    def make_schedule(self):
        # number of teams must be even

        # build first round-robin
        schedule = [self.make_round(round) for round in range(20 - 1)]
        # generate second round-robin by swapping home,away teams
        swapped = [[(away, home) for home, away in day] for day in schedule]

        return schedule + swapped

    def print_schudle(self, team):
        t = Team.Team('elo', 2)
        for round in self.schudle:
            for tuple in round:
                if team in tuple:
                    index = tuple.index(team)
                    neighbor_index = (index + 1) % len(tuple)
                    neighbor = tuple[neighbor_index]
                    # print(f"Sąsiadująca cyfra dla {t.cluv_by_code(team)} to: {t.cluv_by_code(neighbor)}")
                    # print()
                    break

    def cluv_by_code(self, code):
        return self.team_dict[code]

    def code_of_team(self, name):
        return self.team_dict2.get(name)

    def find_team_by_code(self, code):
        for team in self.teams:
            if team.code == code:
                return team
        return None

    def add_players(self):
        with open('all_players.csv', 'r', encoding='utf-8') as file:
            players = csv.reader(file)
            next(players)
            for player in players:
                player_name = player[1]
                overall = int(player[2])
                position = player[3]
                team_name = player[4]
                if self.code_of_team(team_name) != None:
                    #print(f'ile {print(len(self.team_dict_objects))}')
                    team = self.team_dict_objects[self.code_of_team(team_name)]
                    team.add_player(Player.Player(player_name, int(overall), position, team))
                # else:
                #     #print(f'{team_name} {player_name}')
                #
                #     pass
                # # print(f'{team.code}  {player_name}')

    def simulate_round(self):
        opponent = None
        points = self.my_team.points
        for match in self.schudle[self.current_round]:
            team1, team2 = match
            # points = self.my_team.points
            if self.my_team.code in match:
                # print(len(self.team_dict_objects[team1].starting_team))
                print(f' moj ocer {self.my_team.avrage_overall()}')
                # print(type(self.my_team.starting_team[0]))
                print(f'punkty przed {points}')

                # print(type(self.team_dict_objects[team1]))
                if team1 == self.my_team.code:
                    self.team_dict_objects[team2].make_starting11()
                    m = Match.Match(self.team_dict_objects[team1], self.team_dict_objects[team2])
                    # print(f'{self.team_dict[team1]} vs {self.team_dict[team2]}')
                    # print(len(self.team_dict_objects[team2].starting_team))
                    print(f'{self.team_dict[team1]} vs {self.team_dict[team2]}')
                    m.winner()
                    opponent = self.team_dict_objects[team2]
                else:
                    self.team_dict_objects[team1].make_starting11()
                    m = Match.Match(self.team_dict_objects[team1], self.team_dict_objects[team2])
                    # print(len(self.team_dict_objects[team1].starting_team))
                    print(f'{self.team_dict[team1]} vs {self.team_dict[team2]}')
                    m.winner()
                    opponent = self.team_dict_objects[team1]
            else:
                self.team_dict_objects[team1].make_starting11()
                self.team_dict_objects[team2].make_starting11()
                m = Match.Match(self.team_dict_objects[team1], self.team_dict_objects[team2])
                m.winner()
            # print(f'{self.team_dict_objects[team1].avrage_overall()}  {self.team_dict_objects[team1].name}')
            # print(f'{self.team_dict_objects[team2].avrage_overall()}  {self.team_dict_objects[team2].name}')

        self.current_round += 1
        self.new_season()
        print(f'po {self.my_team.points}')
        if points + 1 == self.my_team.points:
            return (0, opponent)
        elif points + 3 == self.my_team.points:
            return (1, opponent)
        else:
            return (-1, opponent)

    def next_match(self):
        for match in self.schudle[self.current_round]:
            if self.my_team.code in match:
                team1, team2 = match
                if team1 == self.my_team.code:
                    return self.cluv_by_code(team2)
                else:
                    return self.cluv_by_code(team1)

    def new_season(self):
        if self.current_round >= 38:
            self.current_round = 0
            for team in self.teams:
                team.points = 0
                team.wins = 0
                team.draws = 0
                team.losses = 0
