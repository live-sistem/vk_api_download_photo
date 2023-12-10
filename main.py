import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

from main_untitled import Ui_Dialog
from vk_save import url_api, download
from dotenv import load_dotenv

load_dotenv()
VK_USER_ID = os.getenv('VK_USER_ID')
VK_TOKEN = os.getenv('VK_TOKEN')

dow = 0
count = 10

class ExampleApp(QtWidgets.QDialog):
    def __init__(self):
        super(ExampleApp, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self) 
        button = self.ui.buttonBox.clicked.connect(self.response)
        
    def response(self):
        # input_id = self.ui.lineEdit.text()
        # input_token = self.ui.lineEdit_2.text()
        self.response_jsons = url_api(dow, 10, VK_USER_ID, VK_TOKEN)
        self.down = download(self.response_jsons)
        print(self.down)


        # except:
        #     msg = QMessageBox() 
        #     msg.setIcon(QMessageBox.Information)  
        #     msg.setWindowTitle("Warning")
        #     msg.setText("Проблемы с соединением")
        #     msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel) 
        #     retval = msg.exec_()
            

        # print("no")
        # self.downloads = download(self.response_json, 0 )



def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    # window.response()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
