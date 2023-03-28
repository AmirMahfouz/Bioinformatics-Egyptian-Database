from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys
import os
from os import path

from PyQt5.uic import loadUiType       #مكتبة عشان اقدر افتح ملف ال Designer بتاعي ةاتعامل معاه بالكود واعدل فيه

Form_CLASS,_ = loadUiType(path.join(path.dirname(__file__), "main.ui"))

class Main(QMainWindow, Form_CLASS):
    def __init__(self, parent=None):
        super(Main,self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.initUI()
        self.Handel_DB_connection()
     #   self.control_buttons()                  ##   ERRORR Here !!!!!!!!!!!!!######################################################################


##Changes in the RUN time
    def initUI(self):
        self.setWindowTitle("Simple Tool")

       # self.tabWidget.tabBar().setVisible(False)        if you want to don't shoe tab widget
########### Database Conncetion
    def Handel_DB_connection(self):
        pass
# all Bnttons in the app

    def control_buttons(self):
############# login button
        self.pushButton.clicked.connect(self.user_login)

        ##### Gene Info

        self.pushButton_5.clicked.connect(self.Edit_gene_info)
        self.pushButton_7.clicked.connect(self.Save_gene_info)
        self.pushButton_6.clicked.connect(self.Delete_gene_info)

        ########3 Protein Info
        self.pushButton_2.connect(self.Edit_protein_info)
        self.pushButton_7.clicked.connect(self.Save_gene_info)
        self.pushButton_6.clicked.connect(self.Delete_gene_info)








##################################################
################# Uers
    def user_login(self):
        pass

######################### Gene
    def Save_gene_info(self):
        pass


    def Delete_gene_info(self):
        pass


    def Edit_gene_info(self):
        pass

##################################Protein
    def Save_protein_info(self):
        pass

    def Delete_protein_info(self):
        pass

    def Edit_protein_info(self):

        pass
## Seach using ID
    def Search(self):
        pass


def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    app.exec_()


if __name__ == '__main__':
        main()