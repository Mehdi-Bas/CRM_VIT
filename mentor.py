# Form implementation generated from reading ui file 'mentor.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_mentorSayfasi(object):
    def setupUi(self, mentorSayfasi):
        mentorSayfasi.setObjectName("mentorSayfasi")
        mentorSayfasi.resize(776, 524)
        self.centralwidget = QtWidgets.QWidget(parent=mentorSayfasi)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
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
        self.tableWidgetMen = QtWidgets.QTableWidget(parent=self.frame)
        self.tableWidgetMen.setGeometry(QtCore.QRect(10, 10, 511, 461))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.tableWidgetMen.setFont(font)
        self.tableWidgetMen.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidgetMen.setObjectName("tableWidgetMen")
        self.tableWidgetMen.setColumnCount(3)
        self.tableWidgetMen.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetMen.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetMen.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetMen.setHorizontalHeaderItem(2, item)
        self.frame_2 = QtWidgets.QFrame(parent=self.frame_4)
        self.frame_2.setGeometry(QtCore.QRect(10, 0, 215, 481))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.tumGorusmelerButton = QtWidgets.QPushButton(parent=self.frame_2)
        self.tumGorusmelerButton.setGeometry(QtCore.QRect(0, 90, 211, 61))
        self.tumGorusmelerButton.setStyleSheet("background-color: rgb(186, 0, 0);\n"
"border-radius:30px;\n"
"color: rgb(255, 255, 255);")
        self.tumGorusmelerButton.setObjectName("tumGorusmelerButton")
        self.lineEditMen = QtWidgets.QLineEdit(parent=self.frame_2)
        self.lineEditMen.setGeometry(QtCore.QRect(10, 10, 191, 22))
        self.lineEditMen.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEditMen.setObjectName("lineEditMen")
        self.araButtonMen = QtWidgets.QPushButton(parent=self.frame_2)
        self.araButtonMen.setGeometry(QtCore.QRect(150, 40, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(10)
        self.araButtonMen.setFont(font)
        self.araButtonMen.setFocusPolicy(QtCore.Qt.FocusPolicy.TabFocus)
        self.araButtonMen.setStyleSheet("background-color: rgb(186, 0, 0);\n"
"border-radius:30px;\n"
"color: rgb(255, 255, 255);")
        self.araButtonMen.setObjectName("araButtonMen")
        self.TercihlerEkraniButtonMen = QtWidgets.QPushButton(parent=self.frame_2)
        self.TercihlerEkraniButtonMen.setGeometry(QtCore.QRect(0, 190, 211, 61))
        self.TercihlerEkraniButtonMen.setStyleSheet("background-color: rgb(186, 0, 0);\n"
"border-radius:30px;\n"
"color: rgb(255, 255, 255);")
        self.TercihlerEkraniButtonMen.setObjectName("TercihlerEkraniButtonMen")
        self.comboBox = QtWidgets.QComboBox(parent=self.frame_2)
        self.comboBox.setGeometry(QtCore.QRect(-2, 310, 221, 22))
        self.comboBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.frame_4, 0, 0, 1, 1)
        mentorSayfasi.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=mentorSayfasi)
        self.statusbar.setObjectName("statusbar")
        mentorSayfasi.setStatusBar(self.statusbar)

        self.retranslateUi(mentorSayfasi)
        QtCore.QMetaObject.connectSlotsByName(mentorSayfasi)

    def retranslateUi(self, mentorSayfasi):
        _translate = QtCore.QCoreApplication.translate
        mentorSayfasi.setWindowTitle(_translate("mentorSayfasi", "MentorSayfasi"))
        item = self.tableWidgetMen.horizontalHeaderItem(0)
        item.setText(_translate("mentorSayfasi", "Ad Soyad"))
        item = self.tableWidgetMen.horizontalHeaderItem(1)
        item.setText(_translate("mentorSayfasi", "Proje Gonderim Tarihi"))
        item = self.tableWidgetMen.horizontalHeaderItem(2)
        item.setText(_translate("mentorSayfasi", "Proje Gelis Tarihi"))
        self.tumGorusmelerButton.setText(_translate("mentorSayfasi", "Tum Gorusmeler"))
        self.araButtonMen.setText(_translate("mentorSayfasi", "ARA"))
        self.TercihlerEkraniButtonMen.setText(_translate("mentorSayfasi", "Tercihler Ekranina Geri Don"))
        self.comboBox.setItemText(0, _translate("mentorSayfasi", "VIT projesinin tamamına katılması uygun olur"))
        self.comboBox.setItemText(1, _translate("mentorSayfasi", "VIT projesi ilk IT eğitimi alıp ITPH a yönlendirilmesi uygun olur"))
        self.comboBox.setItemText(2, _translate("mentorSayfasi", "VIT projesi ingilizce eğitimi alıp ITPH a yönlendirilmesi uygun olur"))
        self.comboBox.setItemText(3, _translate("mentorSayfasi", "VIT projesi kapsamında direkt ITPH a yönlendirilmesi uygun olur."))
        self.comboBox.setItemText(4, _translate("mentorSayfasi", "Direkt bireysel koçluk ile işe yönlendirilmesi uygun olur"))
        self.comboBox.setItemText(5, _translate("mentorSayfasi", "Bir sonraki VIT projesine katilmasi daha uygun olur"))
        self.comboBox.setItemText(6, _translate("mentorSayfasi", "Başka bir sektöre yönlendirilmeli"))
        self.comboBox.setItemText(7, _translate("mentorSayfasi", "Diger"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mentorSayfasi = QtWidgets.QMainWindow()
    ui = Ui_mentorSayfasi()
    ui.setupUi(mentorSayfasi)
    mentorSayfasi.show()
    sys.exit(app.exec())
