from PyQt6.QtWidgets import *
from basvurular import Ui_MainWindow

class basvurular_sayfasi(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.basvuru=Ui_MainWindow()
        self.basvuru.setupUi(self)
        self.basvuru.TercihlerEkraniButtonBas.clicked.connect(self.TercihlerSayfasinaGit)
    def TercihlerSayfasinaGit(self):
        from tercihler_sayfasi import tercih_sayfasi
        self.close()
        self.tercih=tercih_sayfasi()
        self.tercih.show()