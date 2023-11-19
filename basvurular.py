# Form implementation generated from reading ui file 'basvurular.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(775, 534)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_4 = QtWidgets.QFrame(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(14)
        self.frame_4.setFont(font)
        self.frame_4.setStyleSheet("background-color: rgb(255, 246, 201);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.frame = QtWidgets.QFrame(parent=self.frame_4)
        self.frame.setGeometry(QtCore.QRect(230, 0, 531, 491))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.tableWidgetB = QtWidgets.QTableWidget(parent=self.frame)
        self.tableWidgetB.setGeometry(QtCore.QRect(10, 10, 511, 461))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.tableWidgetB.setFont(font)
        self.tableWidgetB.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidgetB.setObjectName("tableWidgetB")
        self.tableWidgetB.setColumnCount(8)
        self.tableWidgetB.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetB.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetB.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetB.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetB.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetB.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetB.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetB.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetB.setHorizontalHeaderItem(7, item)
        self.frame_2 = QtWidgets.QFrame(parent=self.frame_4)
        self.frame_2.setGeometry(QtCore.QRect(10, 0, 215, 481))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.tumBasvurularButton = QtWidgets.QPushButton(parent=self.frame_2)
        self.tumBasvurularButton.setGeometry(QtCore.QRect(0, 90, 211, 61))
        self.tumBasvurularButton.setStyleSheet("background-color: rgb(186, 0, 0);\n"
"border-radius:30px;\n"
"color: rgb(255, 255, 255);")
        self.tumBasvurularButton.setObjectName("tumBasvurularButton")
        self.MentorTanimliButton = QtWidgets.QPushButton(parent=self.frame_2)
        self.MentorTanimliButton.setGeometry(QtCore.QRect(0, 180, 211, 61))
        self.MentorTanimliButton.setStyleSheet("background-color: rgb(186, 0, 0);\n"
"border-radius:30px;\n"
"color: rgb(255, 255, 255);")
        self.MentorTanimliButton.setObjectName("MentorTanimliButton")
        self.MentorTanimsizButton = QtWidgets.QPushButton(parent=self.frame_2)
        self.MentorTanimsizButton.setGeometry(QtCore.QRect(0, 270, 211, 61))
        self.MentorTanimsizButton.setStyleSheet("background-color: rgb(186, 0, 0);\n"
"border-radius:30px;\n"
"color: rgb(255, 255, 255);")
        self.MentorTanimsizButton.setObjectName("MentorTanimsizButton")
        self.TercihlerEkraniButtonBas = QtWidgets.QPushButton(parent=self.frame_2)
        self.TercihlerEkraniButtonBas.setGeometry(QtCore.QRect(0, 360, 211, 61))
        self.TercihlerEkraniButtonBas.setStyleSheet("background-color: rgb(186, 0, 0);\n"
"border-radius:30px;\n"
"color: rgb(255, 255, 255);")
        self.TercihlerEkraniButtonBas.setObjectName("TercihlerEkraniButtonBas")
        self.lineEditBas = QtWidgets.QLineEdit(parent=self.frame_2)
        self.lineEditBas.setGeometry(QtCore.QRect(10, 10, 191, 22))
        self.lineEditBas.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEditBas.setObjectName("lineEditBas")
        self.araButtonbas = QtWidgets.QPushButton(parent=self.frame_2)
        self.araButtonbas.setGeometry(QtCore.QRect(150, 40, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(10)
        self.araButtonbas.setFont(font)
        self.araButtonbas.setFocusPolicy(QtCore.Qt.FocusPolicy.TabFocus)
        self.araButtonbas.setStyleSheet("background-color: rgb(186, 0, 0);\n"
"border-radius:30px;\n"
"color: rgb(255, 255, 255);")
        self.araButtonbas.setObjectName("araButtonbas")
        self.horizontalLayout.addWidget(self.frame_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tableWidgetB.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Tarih"))
        item = self.tableWidgetB.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "New Column"))
        item = self.tableWidgetB.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Mail"))
        item = self.tableWidgetB.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Telefon"))
        item = self.tableWidgetB.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Posta kodu"))
        item = self.tableWidgetB.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "New Column"))
        item = self.tableWidgetB.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "eyalet"))
        item = self.tableWidgetB.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "ekonomik durum"))
        self.tumBasvurularButton.setText(_translate("MainWindow", "Tum Basvurular"))
        self.MentorTanimliButton.setText(_translate("MainWindow", "Mentor GorusmesiTanimlananlar"))
        self.MentorTanimsizButton.setText(_translate("MainWindow", "Mentor GorusmesiTanimlanmayanlar"))
        self.TercihlerEkraniButtonBas.setText(_translate("MainWindow", "Tercihler Ekranina Geri Don"))
        self.araButtonbas.setText(_translate("MainWindow", "ARA"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())