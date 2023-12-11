import sys
from PyQt5.QtWidgets import QApplication

from src.gui.home import FolderSelectApp
from src.gui.sorting import SortingPage

def run_app():
    app = QApplication(sys.argv)
    window = FolderSelectApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    run_app()
