from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem
import League
import Team


from PySide6.QtWidgets import QMainWindow, QTableWidget, QTableWidgetItem, QHeaderView
from PySide6.QtCore import Qt

class TeamTable(QMainWindow):
    def __init__(self, teams):
        super().__init__()
        self.setWindowTitle("Tabela zespołów")

        sorted_teams = sorted(teams, key=lambda team: team.points, reverse=True)  # Sortowanie drużyn według punktów

        table_widget = QTableWidget()
        table_widget.setColumnCount(3)  # Liczba kolumn w tabeli
        table_widget.setHorizontalHeaderLabels(["Pozycja", "Nazwa", "Punkty"])  # Nagłówki kolumn

        table_widget.setRowCount(len(sorted_teams))  # Liczba wierszy w tabeli


        for row, team in enumerate(sorted_teams):
            name_item = QTableWidgetItem(team.name)
            points_item = QTableWidgetItem(str(team.points))
            position = QTableWidgetItem(str(row+1))
            position.setTextAlignment(Qt.AlignCenter)
            points_item.setTextAlignment(Qt.AlignCenter)
            name_item.setTextAlignment(Qt.AlignCenter)
            table_widget.setItem(row, 1, name_item)
            table_widget.setItem(row, 2, points_item)
            table_widget.setItem(row, 0, position)



        table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # Rozciąganie kolumn
        table_widget.verticalHeader().setVisible(False)  # Ukrywanie nagłówka wierszy

        # Dodawanie ikon do pierwszej kolumny


        self.setCentralWidget(table_widget)

        self.resize(800, 600)  # Domyślny rozmiar okna

        self.setMinimumSize(400, 300)  # Minimalny rozmiar okna
