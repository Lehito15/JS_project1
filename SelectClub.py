from PySide6 import QtCore, QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtUiTools import  QUiLoader
from PySide6.QtWidgets import QListWidgetItem, QMessageBox
import re
import Team
import TeamGui
import League
loader = QUiLoader()
import Table
import DataBase


class Select_club(QtCore.QObject):
    def __init__(self):
        super().__init__()
        self.ui = loader.load('select_club1.ui', None)
        self.ui.listWidget.itemClicked.connect(self.handle_item_click)
        self.ui.Klub_dalej.clicked.connect(self.newUi)
        self.user = None
        self.team_gui = TeamGui.Team_gui()

    def show(self):
        self.ui.show()
        self.add_clubs()

    def add_clubs(self):
        teams = ['Arsenal', 'Aston Villa', 'Brentford', 'Brighton', 'Fulham', 'Chelsea',
                 'Crystal Palace', 'Everton', 'Leeds United', 'Leicester City', 'Liverpool', 'Manchester City',
                 'Manchester Utd', 'Newcastle United', 'Nott\'m Forest', 'Southampton', 'Spurs', 'AFC Bournemouth',
                 'West Ham', 'Wolves']
        teams.sort()
        self.ui.listWidget.addItems(teams)

    def newUi(self):
       # print(self.team_gui.league.my_team.name)
        #self.team_gui = TeamGui.Team_gui()
        self.team_gui.league.user = self.user

        if self.team_gui.league.my_team != None:
            self.ui.hide()
            #self.ui1.show()
            self.team_gui.show()
            self.team_gui.league.add_players()
        else:
            QMessageBox.warning(None, "Błąd", 'Wybierz zespół')

    def handle_item_click(self,item):
        selected_team = item.text()
        t = Team.Team('d',0)
        #print(selected_team)
        teams = ['Arsenal', 'Aston Villa', 'Brentford', 'Brighton', 'Fulham', 'Chelsea',
                 'Crystal Palace', 'Everton', 'Leeds United', 'Leicester City', 'Liverpool', 'Manchester City',
                 'Manchester Utd', 'Newcastle United', 'Nott\'m Forest', 'Southampton', 'Spurs', 'AFC Bournemouth',
                 'West Ham', 'Wolves']
        #self.league.my_team = Team.Team(selected_team, t.code_of_team(selected_team))
        #teams.remove(selected_team)
        premier_league_teams = []
        team_dict = {
            1: Team.Team('Arsenal', 1),
            2: Team.Team('Aston Villa', 2),
            3: Team.Team('Brentford', 3),
            4: Team.Team('Brighton', 4),
            5: Team.Team('Fulham', 5),
            6: Team.Team('Chelsea', 6),
            7: Team.Team('Crystal Palace', 7),
            8: Team.Team('Everton', 8),
            9: Team.Team('Leeds United', 9),
            10: Team.Team('Leicester City', 10),
            11: Team.Team('Liverpool', 11),
            12: Team.Team('Manchester City', 12),
            13: Team.Team('Manchester Utd', 13),
            14: Team.Team('Newcastle Utd', 14),
            15: Team.Team('Nott\'m Forest', 15),
            16: Team.Team('Southampton', 16),
            17: Team.Team('Spurs', 17),
            18: Team.Team('AFC Bournemouth', 18),
            19: Team.Team('West Ham', 19),
            20: Team.Team('Wolves', 20)
        }
        self.team_gui.league.team_dict_objects = team_dict

        for team in team_dict:
            premier_league_teams.append(team_dict[team])
            if team_dict[team].name == selected_team:
                self.team_gui.league.my_team = team_dict[team]
            #premier_league_teams.append(Team.Team(team,t.code_of_team(team)))
        self.team_gui.league.teams = premier_league_teams
        #premier_league_teams.append(self.league.my_team)

        #self.league.make_dict()
        #print(len(self.league.teams))
        #self.league.add_players()
       # print(self.league.team_dict_objects)
        return premier_league_teams