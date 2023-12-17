import os
import sys
import requests, json, time, os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from main_untitled import Ui_Dialog
from vk_save import url_api, download, info_max_count, test_api
# from async_one import main_asyncio
from dotenv import load_dotenv

load_dotenv()
VK_USER_ID = os.getenv('VK_USER_ID')
VK_TOKEN = os.getenv('VK_TOKEN')


class ExampleApp(QtWidgets.QDialog):
    def __init__(self):
        super(ExampleApp, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self) 
        button = self.ui.buttonBox.clicked.connect(self.response)
        
    def response(self):  
            # input_id = self.ui.lineEdit.text()
            # input_token = self.ui.lineEdit_2.text()
            input_count = self.ui.lineEdit_3.text()

            self.count_offset = 0
            self.response_jsons = url_api(0, 1, VK_USER_ID, VK_TOKEN)
            self.max_count = info_max_count(self.response_jsons)
            self.count_in = test_api(self.response_jsons)

            if self.count_in != False:
                # в принципе все логично но у PYQT, есть встроенные функции преобразования "строки состояния" в проценты от шагов минимального и максимального шага 
                # тут инфа по ней https://doc.qt.io/qt-5/qprogressbar.html#details
                print(self.max_count)
                # self.main_asyncio = main_asyncio(self.count_in, self.max_count, self.response_jsons, self.count_offset)
                # print(self.main_asyncio)

                for self.count_in in range(0, self.max_count):
                    self.count_in+=1
                    self.response_jsons_one = url_api(self.count_offset, self.count_in, VK_USER_ID, VK_TOKEN)
                    self.downloads = download(self.response_jsons_one)

                    if self.count_in == 200:
                        self.count_offset == self.count_in
                    print("count_in", self.count_in, "count_offset", self.count_offset)

                    self.result_max_count = self.max_count / self.count_in
                    self.percentages = 100 / self.result_max_count
                    self.ui.progressBar.setValue(int(self.percentages))
                    print(self.count_in)
                    



                # while self.count_in != self.max_count:
                #     self.response_jsons_one = url_api(self.count_offset, self.count_in, VK_USER_ID, VK_TOKEN)
                #     self.downloads = download(self.response_jsons_one)
                        
                #     if self.count_in == self.count_offset + self.count_in:
                #         self.count_offset == self.count_in
                #     print("count_in", self.count_in, "count_offset", self.count_offset)

                    
                
            else:
                msg = QMessageBox() 
                msg.setIcon(QMessageBox.Information)  
                msg.setWindowTitle("Warning")
                msg.setText("что-то пошло не так")
                msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel) 
                retval = msg.exec_()
        # except:
        #     msg = QMessageBox() 
        #     msg.setIcon(QMessageBox.Information)  
        #     msg.setWindowTitle("Warning")
        #     msg.setText("Проблемы с соединением")
        #     msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel) 
        #     retval = msg.exec_()
        # print("no")
        # self.downloads = download(self.response_json, 0 )

        # async def main_asyncio(self, self.count_in, self.max_count, self.response_jsons, self.count_offset):
        #     print("ffff")
        #     self.response_jsons_one = url_api(self.count_offset, self.count_in, VK_USER_ID, VK_TOKEN)
        #     self.downloads = download(self.response_jsons_one)
                
        #     if self.count_in == self.count_offset + self.count_in:
        #         self.count_offset == self.count_in
        #     print("count_in", self.count_in, "count_offset", self.count_offset)
        # return   

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    # window.response()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
