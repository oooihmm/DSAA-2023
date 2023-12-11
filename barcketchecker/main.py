import sys
from PyQt5.QtWidgets import QApplication
from src.gui import BracketCheckerApp

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BracketCheckerApp()
    window.show()
    sys.exit(app.exec_())
