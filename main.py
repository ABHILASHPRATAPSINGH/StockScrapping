
import sys

from PyQt5.QtWidgets import QApplication

from Document_Response import Document_Response
from Extrat_Data import ExtractData
from URL import Ui_scrappingDetails

if __name__=='__main__':
    try:
        app=QApplication(sys.argv)
        window=Ui_scrappingDetails()
        window.show()
        app.exec()
    except BaseException as e:
        print(e)
