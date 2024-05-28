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
                msg_box.setText("Right")
                msg_box.exec()
                MainPage.show()
                self.close()
                found = True
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
            break
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

class MainPage(QMainWindow, QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("Gui/Unit1.ui", self)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    msg_box = QMessageBox()
    LoginPage = LoginPage()
    RegisterPage = RegisterPage()
    LoginPage.show()
    MainPage = MainPage()
    sys.exit(app.exec())

