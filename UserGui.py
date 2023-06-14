from PySide6 import QtCore, QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtUiTools import  QUiLoader
from PySide6.QtWidgets import QListWidgetItem, QMessageBox
import re
import Team
import League
loader = QUiLoader()
import Table
import SelectClub
import DataBase
import TeamGui
class UserGui(QtCore.QObject):
    def __init__(self):
        super().__init__()
        self.start = loader.load('start.ui', None)
        self.start.saves.setVisible(False)
        self.start.poczatek.clicked.connect(self.start_user)
        self.start.wczytaj.clicked.connect(self.load_game)
        self.team_guii = TeamGui.Team_gui()
    def show(self):
        self.start.show()
    def start_user(self):
        if  len(self.start.user.text()) != 0:
            #print(f'{self.start.user.text()} i co')
            #self.league.user = self.start.user.text()
            user = self.start.user.text()
            self.Select_team = SelectClub.Select_club()
            self.Select_team.user = user
            self.start.hide()
            self.Select_team.show()
        else:
            QMessageBox.warning(None, "Błąd", "Podaj swój nick")
    def load_game(self):
        db = DataBase.DataBase('baza.db')
        count = db.count_saved_leagues(self.start.user.text())
        t= Team.Team('d',0)
        print(count)
        if count == 0:
            QMessageBox.warning(None, "Błąd", "Nie masz żadnych zapisanych gier")
        elif count == 1 :
            info = db.read_database(self.start.user.text())
            self.load_db(info,self.start.user.text())
        else:
            leagues = db.user_leagues(self.start.user.text())
            for league in leagues:
                item = QListWidgetItem()
                item.setText(f'Twój zespół {t.cluv_by_code(league[0])} ostatnia kolejka {league[1]}. {league[2]}')
                item.setData(Qt.UserRole,league[2])
                item.setData(Qt.UserRole+1,self.start.user.text())
                self.start.saves.addItem(item)
            self.start.saves.setVisible(True)
            self.start.saves.itemClicked.connect(self.get_idL)


    def get_idL(self, item):
        db = DataBase.DataBase('baza.db')
        info = db.read_database(item.data(Qt.UserRole+1), item.data(Qt.UserRole))

        #print(item.data(Qt.UserRole+1))
        self.load_db(info, item.data(Qt.UserRole+1))
    def load_db(self, info,user):
        nr_round = info[0][0]
        my_team = info[0][1]
        print(type(my_team))
        del info[0]
        self.team_dict = {team[1]: Team.Team(team[0], team[1], team[2], team[3], team[4], team[5]) for team in info}
        self.list_team = list(self.team_dict.values())
        #print(list(team_dict.values()))
        #self.league = League.League(list(team_dict.values()),user,nr_round,team_dict[my_team])
        #self.league.my_team = team_dict[my_team]
        #self.league.team_dict_objects = team_dict
        #self.start.hide()
        #self.team_guii.league.team_dict_objects = team_dict
        #self.team_guii = TeamGui.Team_gui()
        #self.team_guii.league.team_dict_objects = self.team_dict
        #self.team_guii.show()
        self.team_guii.league = League.League(self.list_team,user,nr_round,self.team_dict[my_team])
        self.team_guii.league.team_dict_objects = self.team_dict
        self.team_guii.league.my_team = self.team_dict[my_team]
        print(f'mojj {self.team_guii.league.my_team.name}')
        #self.team_guii.league.team_dict_objects = team_dict
        #self.team_guii.league.add_players()
        self.start.hide()
        self.team_guii.show()
        self.team_guii.ui1.round.setText(str(self.team_guii.league.current_round))
        self.team_guii.ui1.points.setText(str(self.team_guii.league.my_team.points))
        self.team_guii.league.teams = sorted(self.team_guii.league.teams, key=lambda team: team.points, reverse=True)
        self.team_guii.ui1.pozycja.setText(str(self.team_guii.league.teams.index(self.team_guii.league.my_team) + 1))



        #self.ui1.show()
        #self.league.add_players()
        #self.add_players()
        #self.set_defoult()