import sys
from PyQt5.QtWidgets import QApplication
from src.gui import ImageSlideshow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = ImageSlideshow()
    mainWin.show()
    sys.exit(app.exec_())
