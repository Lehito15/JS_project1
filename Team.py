import Player

class Team:
    def __init__(self, name, code, points=0, wins=0, losses=0, draws=0):
        self.name = name
        self.points = points
        self.wins = wins
        self.losses = losses
        self.draws = draws
        self.players = []
        self.code = code
        self.starting_team = []

        self.team_dict = team_dict = {
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
            14: 'Newcastle United',
            15: 'Nott\'m Forest',
            16: 'Southampton',
            17: 'Spurs',
            18: 'AFC Bournemouth',
            19: 'West Ham',
            20: 'Wolves'
        }

    def add_player(self, player):
        self.players.append(player)

    def cluv_by_code(self, code):
        return self.team_dict[code]

    def code_of_team(self, name):
        return self.team_dict.get(name)

    def add_starting_team(self, player):
        self.starting_team.append(player)

    def avrage_overall(self):
        total_overall = sum(player.overall for player in self.starting_team if player is not None)
        return total_overall / 11

    def add_starting(self, player: Player):
        print(type(player))
        self.starting_team.append(player)

    def remove_starting(self, player):
        self.starting_team.remove(player)

    def add_points(self, points):
        self.points += points

    def find_player(self, name):
        for player in self.players:
            if player.name == name:
                return player
        return None

    def make_starting11(self):
        if len(self.starting_team) != 11:
            self.starting_team = []
            self.players.sort(key=lambda x: x.overall, reverse=True)
            self.starting_team = self.players[:11]
