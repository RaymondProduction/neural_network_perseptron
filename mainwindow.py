# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(390, 306)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 0, 260, 260))
        self.widget.setMouseTracking(False)
        self.widget.setAutoFillBackground(False)
        self.widget.setStyleSheet("border: 2px solid black;\n"
"background-color: white;")
        self.widget.setObjectName("widget")
        self.clearButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.clearButton.setGeometry(QtCore.QRect(280, 10, 100, 30))
        self.clearButton.setObjectName("clearButton")
        self.checkButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.checkButton.setGeometry(QtCore.QRect(280, 50, 100, 30))
        self.checkButton.setObjectName("checkButton")
        self.alignButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.alignButton.setGeometry(QtCore.QRect(280, 90, 100, 30))
        self.alignButton.setObjectName("alignButton")
        self.forgetButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.forgetButton.setGeometry(QtCore.QRect(280, 130, 100, 30))
        self.forgetButton.setObjectName("forgetButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 390, 23))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(parent=self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(parent=self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionLoad_weights = QtGui.QAction(parent=MainWindow)
        self.actionLoad_weights.setObjectName("actionLoad_weights")
        self.actionSave_weights = QtGui.QAction(parent=MainWindow)
        self.actionSave_weights.setObjectName("actionSave_weights")
        self.actionAbout = QtGui.QAction(parent=MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuFile.addAction(self.actionLoad_weights)
        self.menuFile.addAction(self.actionSave_weights)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.clearButton.setText(_translate("MainWindow", "Clear"))
        self.checkButton.setText(_translate("MainWindow", "Check"))
        self.alignButton.setText(_translate("MainWindow", "Align"))
        self.forgetButton.setText(_translate("MainWindow", "Forget"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionLoad_weights.setText(_translate("MainWindow", "Load weights"))
        self.actionSave_weights.setText(_translate("MainWindow", "Save weights"))
        self.actionAbout.setText(_translate("MainWindow", "About"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
