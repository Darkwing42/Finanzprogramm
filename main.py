from PyQt4 import QtGui
import sys
import MainWindow

class FinanzApp(QtGui.QMainWindow, MainWindow.Ui_FinanzControl):
    def __init__(self):
        super(FinanzApp, self).__init__()
        self.setupUi(self)



def main():
    app = QtGui.QApplication(sys.argv)
    ui = FinanzApp()
    ui.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
