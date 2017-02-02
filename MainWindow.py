# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Mainwindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_FinanzControl(object):
    def setupUi(self, FinanzControl):
        FinanzControl.setObjectName(_fromUtf8("FinanzControl"))
        FinanzControl.setEnabled(True)
        FinanzControl.resize(1040, 700)
        self.centralwidget = QtGui.QWidget(FinanzControl)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.layoutWidget = QtGui.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 10, 1001, 631))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.btnEinkuenfte = QtGui.QPushButton(self.layoutWidget)
        self.btnEinkuenfte.setObjectName(_fromUtf8("btnEinkuenfte"))
        self.horizontalLayout.addWidget(self.btnEinkuenfte)
        self.btnAusgaben = QtGui.QPushButton(self.layoutWidget)
        self.btnAusgaben.setObjectName(_fromUtf8("btnAusgaben"))
        self.horizontalLayout.addWidget(self.btnAusgaben)
        self.btnUebersicht = QtGui.QPushButton(self.layoutWidget)
        self.btnUebersicht.setObjectName(_fromUtf8("btnUebersicht"))
        self.horizontalLayout.addWidget(self.btnUebersicht)
        self.btnGrafik = QtGui.QPushButton(self.layoutWidget)
        self.btnGrafik.setObjectName(_fromUtf8("btnGrafik"))
        self.horizontalLayout.addWidget(self.btnGrafik)
        self.btnLoginDaten = QtGui.QPushButton(self.layoutWidget)
        self.btnLoginDaten.setObjectName(_fromUtf8("btnLoginDaten"))
        self.horizontalLayout.addWidget(self.btnLoginDaten)
        self.btnPasswortAendern = QtGui.QPushButton(self.layoutWidget)
        self.btnPasswortAendern.setObjectName(_fromUtf8("btnPasswortAendern"))
        self.horizontalLayout.addWidget(self.btnPasswortAendern)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        spacerItem = QtGui.QSpacerItem(20, 34, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.MinimumExpanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.calendarWidget = QtGui.QCalendarWidget(self.layoutWidget)
        self.calendarWidget.setObjectName(_fromUtf8("calendarWidget"))
        self.horizontalLayout_2.addWidget(self.calendarWidget)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_3.addWidget(self.label_2)
        self.listView_2 = QtGui.QListView(self.layoutWidget)
        self.listView_2.setObjectName(_fromUtf8("listView_2"))
        self.verticalLayout_3.addWidget(self.listView_2)
        self.btnAktualisieren = QtGui.QPushButton(self.layoutWidget)
        self.btnAktualisieren.setObjectName(_fromUtf8("btnAktualisieren"))
        self.verticalLayout_3.addWidget(self.btnAktualisieren)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.listView = QtGui.QListView(self.layoutWidget)
        self.listView.setObjectName(_fromUtf8("listView"))
        self.verticalLayout.addWidget(self.listView)
        self.btnNeuerTermin = QtGui.QPushButton(self.layoutWidget)
        self.btnNeuerTermin.setObjectName(_fromUtf8("btnNeuerTermin"))
        self.verticalLayout.addWidget(self.btnNeuerTermin)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        FinanzControl.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(FinanzControl)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1040, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        FinanzControl.setMenuBar(self.menubar)

        self.retranslateUi(FinanzControl)
        QtCore.QMetaObject.connectSlotsByName(FinanzControl)

    def retranslateUi(self, FinanzControl):
        FinanzControl.setWindowTitle(_translate("FinanzControl", "MainWindow", None))
        self.btnEinkuenfte.setText(_translate("FinanzControl", "Einkünfte", None))
        self.btnAusgaben.setText(_translate("FinanzControl", "Ausgaben", None))
        self.btnUebersicht.setText(_translate("FinanzControl", "Übersicht", None))
        self.btnGrafik.setText(_translate("FinanzControl", "Grafik", None))
        self.btnLoginDaten.setText(_translate("FinanzControl", "Login Daten", None))
        self.btnPasswortAendern.setText(_translate("FinanzControl", "Passwort ändern", None))
        self.label_2.setText(_translate("FinanzControl", "Übersicht", None))
        self.btnAktualisieren.setText(_translate("FinanzControl", "Aktualisieren", None))
        self.label.setText(_translate("FinanzControl", "Termine", None))
        self.btnNeuerTermin.setText(_translate("FinanzControl", "Neuer Termin", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    FinanzControl = QtGui.QMainWindow()
    ui = Ui_FinanzControl()
    ui.setupUi(FinanzControl)
    FinanzControl.show()
    sys.exit(app.exec_())

