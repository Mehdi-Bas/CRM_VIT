# Form implementation generated from reading ui file 'girissayfasi.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_GirisSayfasi(object):
    def setupUi(self, GirisSayfasi):
        GirisSayfasi.setObjectName("GirisSayfasi")
        GirisSayfasi.resize(850, 504)
        self.centralwidget = QtWidgets.QWidget(parent=GirisSayfasi)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setStyleSheet("background-color: rgb(255, 246, 201);")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.labelKullanci = QtWidgets.QLabel(parent=self.frame)
        self.labelKullanci.setGeometry(QtCore.QRect(428, 160, 111, 20))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(12)
        self.labelKullanci.setFont(font)
        self.labelKullanci.setStyleSheet("color: rgb(69, 79, 83);")
        self.labelKullanci.setObjectName("labelKullanci")
        self.lineEdit_1 = QtWidgets.QLineEdit(parent=self.frame)
        self.lineEdit_1.setGeometry(QtCore.QRect(550, 151, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Sitka Display")
        font.setPointSize(11)
        font.setBold(False)
        self.lineEdit_1.setFont(font)
        self.lineEdit_1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.labelSifre = QtWidgets.QLabel(parent=self.frame)
        self.labelSifre.setGeometry(QtCore.QRect(490, 200, 49, 16))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(12)
        self.labelSifre.setFont(font)
        self.labelSifre.setStyleSheet("color: rgb(69, 79, 83);")
        self.labelSifre.setObjectName("labelSifre")
        self.girisButton = QtWidgets.QPushButton(parent=self.frame)
        self.girisButton.setGeometry(QtCore.QRect(600, 260, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(11)
        self.girisButton.setFont(font)
        self.girisButton.setStyleSheet("background-color: rgb(69, 79, 83);\n"
"\n"
"color: rgb(255, 255, 255);\n"
"")
        self.girisButton.setObjectName("girisButton")
        self.labelBilgi = QtWidgets.QLabel(parent=self.frame)
        self.labelBilgi.setGeometry(QtCore.QRect(550, 230, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.labelBilgi.setFont(font)
        self.labelBilgi.setStyleSheet("color: rgb(69, 79, 83);")
        self.labelBilgi.setObjectName("labelBilgi")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(550, 190, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Sitka Display")
        font.setPointSize(9)
        font.setBold(False)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.frame_2 = QtWidgets.QFrame(parent=self.frame)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 421, 461))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.labelResim = QtWidgets.QLabel(parent=self.frame_2)
        self.labelResim.setGeometry(QtCore.QRect(10, 0, 411, 461))
        self.labelResim.setText("")
        self.labelResim.setPixmap(QtGui.QPixmap("resimler/werherer logo.png"))
        self.labelResim.setObjectName("labelResim")
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        GirisSayfasi.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=GirisSayfasi)
        self.statusbar.setObjectName("statusbar")
        GirisSayfasi.setStatusBar(self.statusbar)

        self.retranslateUi(GirisSayfasi)
        QtCore.QMetaObject.connectSlotsByName(GirisSayfasi)

    def retranslateUi(self, GirisSayfasi):
        _translate = QtCore.QCoreApplication.translate
        GirisSayfasi.setWindowTitle(_translate("GirisSayfasi", "GirisSayfasi"))
        self.labelKullanci.setText(_translate("GirisSayfasi", "Kullanci Adi"))
        self.labelSifre.setText(_translate("GirisSayfasi", "Sifre"))
        self.girisButton.setText(_translate("GirisSayfasi", "Giris"))
        self.labelBilgi.setText(_translate("GirisSayfasi", "Kullanici adinizi ve sifresinizi giriniz"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    GirisSayfasi = QtWidgets.QMainWindow()
    ui = Ui_GirisSayfasi()
    ui.setupUi(GirisSayfasi)
    GirisSayfasi.show()
    sys.exit(app.exec())