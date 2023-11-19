from PyQt6.QtWidgets import *
from mentor import Ui_mentorSayfasi
class mentor_sayfasi(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.mentor=Ui_mentorSayfasi()
        self.mentor.setupUi(self)
        self.mentor.TercihlerEkraniButtonMen.clicked.connect(self.TercihlerSayfasinaGit)
    def TercihlerSayfasinaGit(self):
        from tercihler_sayfasi import tercih_sayfasi
        self.close()
        self.tercih=tercih_sayfasi()
        self.tercih.show()