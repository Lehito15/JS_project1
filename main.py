import sys
from PySide6 import QtWidgets
#from select_club import Select_club
from UserGui import UserGui
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = UserGui()
    window.show()
    sys.exit(app.exec())