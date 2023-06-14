from PySide6 import QtWidgets
from PySide6.QtCore import Qt
import sys
from PySide6.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel, QPushButton, QLineEdit
from PySide6.QtGui import QFont, QColor, Qt


class ScoreDialog(QDialog):
    def __init__(self, team, colorr, score, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Wynik")
        self.resize(400, 200)

        layout = QVBoxLayout()

        label = QLabel(str(score))
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet(f"QLabel {{ color: {colorr}; font-size: 24px; }}")

        self.team_name_input = QLabel()
        self.team_name_input.setText(f'z zespołem {str(team)}')
        self.team_name_input.setAlignment(Qt.AlignCenter)

        button = QPushButton("OK")
        button.setMaximumWidth(100)
        button.setStyleSheet("QPushButton { background-color: #4CAF50; color: white; font-weight: bold; }")

        layout.addStretch(1)
        layout.addWidget(label)
        layout.addWidget(self.team_name_input)
        layout.addSpacing(20)  # Dodanie odstępu o wysokości 20 pikseli
        layout.addWidget(button)
        layout.addStretch(1)

        self.setLayout(layout)

        self.setStyleSheet("QDialog { background-color: #f2f2f2; }")

        button.clicked.connect(self.accept)

# app.exec()
