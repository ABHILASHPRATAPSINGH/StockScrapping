import os
import sys

import pandas
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFrame, QApplication, QMessageBox

from Document_Response import Document_Response
from Extrat_Data import ExtractData
from Import_Export_Data import ImportExportData
from utility import PathUtility


class Ui_scrappingDetails(QFrame):

    def __init__(self):
        super().__init__()
        self.setupUi()


    def setupUi(self):
        scrappingDetails=self
        self.df = ImportExportData().importStock_URL()
        # abhilashTxt=PathUtility.getPackagedFilePathStrict("resource",'abhilash.txt')  # ye resource se phele ka path khud uthayega dynamicly,, pr ek jruri baat ki resource folder ka apke project m hona jruri hai, ya jo folder ho uska name yha parameter me pass karaye, or next parameter me file ka naame.
        # print(abhilashTxt)
        scrappingDetails.setObjectName("scrappingDetails")

        scrappingDetails.resize(344, 117)
        self.cmb_URL = QtWidgets.QComboBox(scrappingDetails)
        self.cmb_URL.setGeometry(QtCore.QRect(70, 50, 171, 22))
        self.cmb_URL.setObjectName("cmb_URL")
        self.cmb_URL.addItems(list(self.df.index))
        self.stock = self.cmb_URL.currentText()

        self.URL=self.df.loc[self.stock,'URL']

        self.cmb_URL.currentTextChanged.connect(self.changed_sto)

        self.lbl_URL = QtWidgets.QLabel(scrappingDetails)
        self.lbl_URL.setGeometry(QtCore.QRect(40, 53, 41, 20))
        self.lbl_URL.setObjectName("lbl_URL")

        self.btn_OK = QtWidgets.QPushButton(scrappingDetails)
        self.btn_OK.setGeometry(QtCore.QRect(260, 50, 51, 21))
        self.btn_OK.setObjectName("btn_OK")
        # self.btn_OK.clicked.connect(self.cn_ok_btn)

        self.line = QtWidgets.QFrame(scrappingDetails)
        self.line.setGeometry(QtCore.QRect(20, 80, 311, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")



        QtCore.QMetaObject.connectSlotsByName(scrappingDetails)
        scrappingDetails.setWindowTitle("Scraping URL")
        self.btn_OK.setText("OK")
        self.lbl_URL.setText("URL:")
        self.btn_OK.clicked.connect(self.cn_ok_btn)

    def changed_sto(self):
        self.stock = self.cmb_URL.currentText()
        self.URL = self.df.loc[self.stock, 'URL']
        return self.URL

    def cn_ok_btn(self):
        # print(self.URL)
        # print(self.stock)
        outputFile=os.environ["USERPROFILE"]+"/Desktop/{}.xlsx".format(self.stock)
        resp = Document_Response(self.URL).req_htmlDocument()
        df = ExtractData(resp).ex_shareholding_details()
        df1 = pandas.DataFrame(df)
        # df1.to_excel("C:\\Users\\DELL\\Desktop\\" +self.stock + ".xlsx")
        df1.to_excel(outputFile)
        QMessageBox.information(self, "Status", "Done")


