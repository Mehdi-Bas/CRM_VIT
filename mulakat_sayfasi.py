from PyQt6.QtWidgets import *
from mulakatlar import Ui_MulakatlarSayfasi

class mulakatlar_sayfasi(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.mulakat=Ui_MulakatlarSayfasi()
        self.mulakat.setupUi(self)
        self.mulakat.TercihlerEkraniButtonMul.clicked.connect(self.TercihlerSayfasinaGit)
    def TercihlerSayfasinaGit(self):
        from tercihler_sayfasi import tercih_sayfasi
        self.close()
        self.tercih=tercih_sayfasi()
        self.tercih.show()