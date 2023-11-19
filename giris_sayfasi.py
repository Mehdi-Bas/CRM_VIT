
from PyQt6.QtWidgets import *
from girissayfasi import Ui_GirisSayfasi
from tercihler_sayfasi import tercih_sayfasi
class girissayfasi(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.giris=Ui_GirisSayfasi()
        self.giris.setupUi(self)
        self.tercihlersayfasiac=tercih_sayfasi()
        self.giris.girisButton.clicked.connect(self.GirisYap)
        
    def GirisYap(self):
        kadi=self.giris.lineEdit_1.text()
        sifre=self.giris.lineEdit_2.text()
        if kadi=='a' and sifre=='1234':
            self.close()
            self.tercihlersayfasiac.show()