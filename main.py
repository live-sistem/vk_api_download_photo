import sys
import os
from PyQt5 import QtWidgets
from design import Ui_Dialog
from vk_save import url_api
from dotenv import load_dotenv

load_dotenv()
VK_USER_ID = os.getenv('VK_USER_ID')
VK_TOKEN = os.getenv('VK_TOKEN')

dow = 0
count = 10

class ExampleApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(ExampleApp, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self) 
        self.response_json = url_api(dow, "10", VK_USER_ID, VK_TOKEN)
        print(self.response_json)

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()