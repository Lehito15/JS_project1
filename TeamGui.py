from PySide6 import QtCore, QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QListWidgetItem, QMessageBox
import re
import Team
import League
import Score_info

loader = QUiLoader()
import Table
import DataBase


class Team_gui(QtCore.QObject):
    def __init__(self):
        super().__init__()
        self.league = League.League([])
        self.ui1 = loader.load('team.ui', None)
        self.ui1.allPlayers.itemClicked.connect(self.move_player)
        self.ui1.starting11.itemClicked.connect(self.remove_player)
        self.ui1.table.clicked.connect(self.print_table)
        self.ui1.pushButton.clicked.connect(self.simulate_rounds)
        self.ui1.save.clicked.connect(self.save_game)

        # self.add_players()

    def show(self):
        self.ui1.show()
        # self.add_players()
        self.league.add_players()
        self.add_players()
        print(self.league.my_team.name)
        self.set_defoult()

    def add_players(self):
        print(f' ojo {self.league.my_team}')
        for player in self.league.my_team.players:
            item = QListWidgetItem()
            item.setText(f" {player.name},  {player.overall},  {player.position}")
            self.ui1.allPlayers.addItem(item)

    def move_player(self, player):
        selected_player = player.text()
        self.ui1.allPlayers.takeItem(self.ui1.allPlayers.row(player))
        item = QListWidgetItem(selected_player)
        self.ui1.starting11.addItem(item)
        name = re.search(r"^([\w\s'-]+),", selected_player)
        if name:
            self.league.my_team.add_starting(self.league.my_team.find_player(name.group(1).strip()))
        else:
          print(selected_player)

    def remove_player(self, player):
        selected_player = player.text()
        self.ui1.starting11.takeItem(self.ui1.starting11.row(player))
        item = QListWidgetItem(selected_player)
        self.ui1.allPlayers.addItem(item)
        name = re.search(r"^([\w\s'-]+),", selected_player)
        if name:
            self.league.my_team.remove_starting(self.league.my_team.find_player(name.group(1).strip()))
        else:
            print(selected_player)


    def simulate_rounds(self):
        if len(self.league.my_team.starting_team) != 11:
            QMessageBox.warning(None, "Błąd", "Twoja wyjściowa 11 nie jest kompletna")
        else:
            who_wins = self.league.simulate_round()
            self.ui1.round.setText(str(self.league.current_round))
            self.ui1.points.setText(str(self.league.my_team.points))
            self.league.teams = sorted(self.league.teams, key=lambda team: team.points, reverse=True)
            self.ui1.pozycja.setText(str(self.league.teams.index(self.league.my_team)+1))
            self.ui1.next_match.setText(self.league.next_match())
            print(who_wins[0])
            if who_wins[0] == 1:
                self.win = Score_info.ScoreDialog(who_wins[1].name, 'green', 'Wygrałeś')
                self.win.show()
            elif who_wins[0] == 0:
                self.draw = Score_info.ScoreDialog(who_wins[1].name, 'yellow', 'Zremisowałeś')
                self.draw.show()
            else:
                self.loss = Score_info.ScoreDialog(who_wins[1].name, 'red', 'Przegrałeś')
                self.loss.show()

    def print_table(self):
        self.table_window = Table.TeamTable(self.league.teams)
        self.table_window.show()

    def set_defoult(self):
        self.ui1.team.setText(self.league.my_team.name)
        self.ui1.round.setText('1')
        self.ui1.points.setText('0')
        self.ui1.pozycja.setText('...')
        self.ui1.next_match.setText(self.league.next_match())


    def save_game(self):
        db = DataBase.DataBase('baza.db')
        db.save_game(self.league.user, self.league.current_round, self.league.my_team.code, self.league.teams)
    def show_win_message(self):
        message_box = QMessageBox()
        message_box.setIcon(QMessageBox.Information)
        message_box.setWindowTitle("Wygrana!")
        message_box.setText("Gratulacje, wygrałeś!")
        message_box.setStandardButtons(QMessageBox.Ok)
        message_box.exec()
