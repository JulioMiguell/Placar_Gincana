import sys
from PyQt5.QtWidgets import QApplication
from placarGincana import Placar
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Placar()
    sys.exit(app.exec_())