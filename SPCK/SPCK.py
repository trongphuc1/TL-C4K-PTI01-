import pyttsx3
import sys
from PyQt6.QtWidgets import *
from PyQt6 import uic
import json
import re


with open('./account.json', 'r') as file:
    data_account = json.load(file)


class LoginPage(QMainWindow, QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("Gui/Login.ui", self)
        self.btnLogin.clicked.connect(self.checkLogin)
        self.btn_register.clicked.connect(self.register)
    def checkLogin(self):
        email = self.txtEmail.text()
        password = self.txtPassword.text()
        found = False
        for  account in data_account:
            if account['email'] == email and account['password'] == password:
                found = True
                msg_box.setText("Right")
                msg_box.exec()
                MainPage.show()
                self.close()
                
                break

        if not found:
            msg_box.setText("Incorrect email or password")
            msg_box.exec()
    def register(self):
        RegisterPage.show()
        self.close()
        return
    
class RegisterPage(QMainWindow, QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("Gui/Sign_up.ui",self)
        self.btn_register.clicked.connect(self.checkRegister)
    def checkRegister(self):
        name = self.txtFullName.text()
        email = self.txtEmail.text()
        password = self.txtPassword.text()
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

        if name == '':
            msg_box.setText('Vui lòng nhập tên')
            msg_box.exec()
            return
        if email == '':
            msg_box.setText('Vui lòng nhập tài khoản')
            msg_box.exec()
            return
        
        if not re.match(email_regex, email):
            msg_box.setText('Tài khoản chưa nhạp đúng định dạng')
            msg_box.exec()
            return
        for account in data_account:
            if email == account['email']:
                msg_box.setText('tài khoản đã tồn tại')
                msg_box.exec()
                return
            
            if len(password) < 8:
                msg_box.setText("Password must be at least 8 characters long.")
                msg_box.exec()
                return
            
            if not re.search(r"\d", password):
                msg_box.setText("Password must include at least one digit.")
                msg_box.exec()
                return
            
            if not re.search(r"[A-Z]", password):
                msg_box.setText("Password must include at least one uppercase letter.")
                msg_box.exec()
                return
            
            if not re.search(r"[a-z]", password):
                msg_box.setText("Password must include at least one lowercase letter.")
                msg_box.exec()
                return
            if not re.search(r"[!@#\$%\^&\*]", password):
                msg_box.setText("Password must include at least one special character.")
                msg_box.exec()
                return
            
            new_account = {
            "email": email,
            "password": password   
            }
            data_account.append(new_account)
            with open('./account.json', "w") as json_file:
                json.dump(data_account, json_file, indent=4)
            LoginPage.show()
            self.close()
            return


    #     self.unit_item_list = self.load_data()
    #     self.load_data_Ui(self.unit_item_list)

    #     self.search.clicked.connect(self.search_item)
    #     self.edit.clicked.connect(self.edit_item)
    #     self.delete.clicked.connect(self.delete_item)
    #     self.add.clicked.connect(self.open_add_dialog)
    # def load_data(self):
    #     with open('note.json', 'r') as file:
    #         return json.load(file)
    # def load_data_UI(self,unit_item_list):
    #     for item in unit_item_list:
    #         title = item['title']
    #         self.Unitlist1.addItem(QListWidgetItem(title))
    #     if self.Unitlist1.count() > 0:
    #         self.Unitlist1.setCurrentRow(0)
    # def search_item(self):
    #     search_text = self.inputUnit.text().lower()
    #     self.Unitlist1.clear()
    #     for item in self.unit_item_list:
    #         if search_text in item['title'].lower():
    #             self.Unitlist1.addItem(QListWidgetItem(item['title']))

    # def open_add_dialog(self):
    #     dialog = AddDialog()
    #     if dialog.exec():
    #         self.load_data_UI
class MainPage(QMainWindow, QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("Gui/Unit1.ui", self)
        self.bt_les1.clicked.connect(self.button_les1)
    def button_les1(self):
        U1L1.show()
        self.close()

        
class Unit1les1(QMainWindow,QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("Gui/school1.ui",self)
        self.bt_next.clicked.connect(self.nextLesson)
        self.BacktoU1.clicked.connect(self.Back_to_U1)
    def nextLesson(self):
        U1L2.show()
        self.close()
    def Back_to_U1(self):
        MainPage.show()
        self.close()
class Unit1les2(QMainWindow,QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("Gui/school2.ui",self)
class SettingPage(QMainWindow, QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("Gui/Setting.ui",self)
    def search_item(self):
        search_text = self.inputUnit.text().lower()
        self.unitList1


if __name__ == '__main__':
    app = QApplication(sys.argv)
    msg_box = QMessageBox()
    LoginPage = LoginPage()
    RegisterPage = RegisterPage()
    U1L2 = Unit1les2()
    U1L1 = Unit1les1()
    LoginPage.show()
    Setting = SettingPage()
    MainPage = MainPage()
    sys.exit(app.exec())
