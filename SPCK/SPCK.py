import pyttsx3
import sys
from PyQt6.QtWidgets import *
from PyQt6 import uic
import json
import re

engine = pyttsx3.init()
with open('./account.json', 'r') as file:
    data_account = json.load(file)


class LoginPage(QMainWindow, QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("Gui/Login.ui", self)
        self.btnLogin.clicked.connect(self.checkLogin)
        self.btn_register.clicked.connect(self.register)
        self.btn_guest.clicked.connect(self.guest_account)
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
    def guest_account(self):
        MainPage.show()
        self.close()
    
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
#Unit 1 place
class ComputerPage(QMainWindow,QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("Gui/windowplace.ui",self)
        self.bt_app.clicked.connect(self.button_goto_app)
        self.bt_Visual.clicked.connect(self.bt_error)
        self.bt_google.clicked.connect(self.bt_error)
        self.bt_word.clicked.connect(self.bt_error)
        self.shutdown.clicked.connect(self.off_window)
    def off_window(self):
        self.close()
    def button_goto_app(self):
        LoginPage.show()
        self.close()
    def bt_error(self):
        ErrorPage.show()
        self.close()
class ErrorPage(QMainWindow,QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("Gui/errorplace.ui",self)
        self.bt_backtowindow.clicked.connect(self.backwindow)
    def backwindow(self):
        ComputerPage.show()
        self.close()
class MainPage(QMainWindow, QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("Gui/Unit1.ui", self)
        # self.bt_les1.clicked.connect(self.button_les1)
        # self.bt_les2.clicked.connect(self.button_les2)
        self.bt_les3.clicked.connect(self.button_les3)
        self.bt_les4.clicked.connect(self.button_les4)
        self.bt_les5.clicked.connect(self.button_les5)
        self.bt_quit.clicked.connect(self.button_quit)
        self.btn_logout.clicked.connect(self.button_logout)
        self.bt_U2.clicked.connect(self.button_U2)
        self.bt_midtest.clicked.connect(self.button_midterm)
        self.bt_U3.clicked.connect(self.button_U3)
        self.bt_U4.clicked.connect(self.button_U4)
        self.bt_finaltest.clicked.connect(self.button_finaltest)
    def button_midterm(self):
        MidTest.show()
        self.close()
    def button_U2(self):
        U2.show()
        self.close()
    def button_U3(self):
        U3.show()
        self.close()
    def button_U4(self):
        U4.show()
        self.close()
    def button_finaltest(self):
        FinalTest.show()
        self.close()
    def button_logout(self):
        LoginPage.show()
        self.close()
    def button_quit(self):
        ComputerPage.show()
        self.close()
    # def button_les1(self):
    #     U1L1.show()
    #     self.close()
    # def button_les2(self):
    #     U1L2.show()
    #     self.close()
    def button_les3(self):
        U1L3.show()
        self.close()
    def button_les4(self):
        U1L4.show()
        self.close()
    def button_les5(self):
        U1L5.show()
        self.close()
class Right(QMainWindow, QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("Gui/correct.ui",self)
class Wrong(QMainWindow,QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("Gui/wrong.ui",self)
# class Unit1les1(QMainWindow,QWidget):
#     def __init__(self):
#         super().__init__()
#         uic.loadUi("Gui/school1.ui",self)
#         self.bt_next.clicked.connect(self.nextLesson)
#         self.BacktoU1.clicked.connect(self.Back_to_U1)
#         self.states = {
#             'pencil': True,
#             'book': True,
#             'bag': True,
#             'chair': True,
#             'table': True
#         }
#     def nextLesson(self):
#         U1L2.show()
#         self.close()
#         # Check if all buttons have been clicked
#         if all(self.states.values()):
#             # All buttons have been clicked, proceed to the next lesson
            
#             msg_box.setText("Proceeding to the next lesson.")
#             msg_box.exec()
#             # Logic for loading the next lesson here
#         else:
#             msg_box.setText("Please interact with all items before proceeding.")
#             msg_box.exec()
#             # Optionally, inform the user to interact with all items

#     def Back_to_U1(self):
#         MainPage.show()
#         self.close()
        
#         self.btn_pencil.clicked.connect(lambda: self.buttonClicked("Pencil"))
        
#         self.btn_book.clicked.connect(lambda: self.buttonClicked("Book"))
#         self.btn_bag.clicked.connect(lambda: self.buttonClicked("Bag"))
#         self.btn_chair.clicked.connect(lambda: self.buttonClicked("Chair"))
#         self.btn_table.clicked.connect(lambda: self.buttonClicked("Table"))
    
#     def buttonClicked(self, item):
#         self.states[item.lower()] = True  # Update state
#         self.speak(item)

#     def speak(self, text):
#         engine = pyttsx3.init()
#         engine.say(text)
#         engine.runAndWait()

# class Unit1les2(QMainWindow,QWidget):
#     def __init__(self):
#         super().__init__()
#         uic.loadUi("Gui/school2.ui",self)
#         self.bt_next2.clicked.connect(self.nextLesson)
#         self.BacktoU1_2.clicked.connect(self.Back_to_U1)
#     def nextLesson(self):
#         U1L3.show()
#         self.close()
#     def Back_to_U1(self):
#         MainPage.show()
#         self.close()
class Unit1les3(QMainWindow,QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("Gui/school3.ui",self)
        self.bt_next3.clicked.connect(self.nextLesson)
        self.BacktoU1_3.clicked.connect(self.Back_to_U1)
        self.right.clicked.connect(self.right_click)
        self.right2.clicked.connect(self.right_click)
        self.right3.clicked.connect(self.right_click)
        self.right4.clicked.connect(self.right_click)
        self.wrong1.clicked.connect(self.wrong_click)
        self.wrong2.clicked.connect(self.wrong_click)
        self.wrong3.clicked.connect(self.wrong_click)
        self.wrong4.clicked.connect(self.wrong_click)
        self.wrong5.clicked.connect(self.wrong_click)
        self.wrong6.clicked.connect(self.wrong_click)
        self.wrong7.clicked.connect(self.wrong_click)
        self.wrong8.clicked.connect(self.wrong_click)
    def wrong_click(self):
        Wrong.show()
    def right_click(self):
        Right.show()
    def nextLesson(self):
        U1L4.show()
        self.close()
    def Back_to_U1(self):
        MainPage.show()
        self.close()
    

class Unit1les4(QMainWindow,QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("Gui/school4.ui",self)
        self.bt_next4.clicked.connect(self.nextLesson)
        self.BacktoU1_4.clicked.connect(self.Back_to_U1)
        self.check1.clicked.connect(self.correct_place)
        self.check1_2.clicked.connect(self.wrong_place)
        self.check2_2.clicked.connect(self.correct_place)
        self.check2.clicked.connect(self.wrong_place)
        self.check3_2.clicked.connect(self.correct_place)
        self.check3.clicked.connect(self.wrong_place)
    def correct_place(self):
        Right.show()
    def wrong_place(self):
        Wrong.show()
    def nextLesson(self):
        U1L5.show()
        self.close()
    def Back_to_U1(self):
        MainPage.show()
        self.close()


        
class Unit1les5(QMainWindow,QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("Gui/school5.ui",self)
        self.bt_next5.clicked.connect(self.nextLesson)
        self.BacktoU1_5.clicked.connect(self.Back_to_U1)
        self.right.clicked.connect(self.right_click)
        self.right2.clicked.connect(self.right_click)
        self.right3.clicked.connect(self.right_click)
        self.right4.clicked.connect(self.right_click)
        self.wrong.clicked.connect(self.wrong_click)
        self.wrong2.clicked.connect(self.wrong_click)
        self.wrong3.clicked.connect(self.wrong_click)
        self.wrong4.clicked.connect(self.wrong_click)
        self.wrong5.clicked.connect(self.wrong_click)
        self.wrong6.clicked.connect(self.wrong_click)
        self.wrong7.clicked.connect(self.wrong_click)
        self.wrong8.clicked.connect(self.wrong_click)
    def wrong_click(self):
        Wrong.show()
    def right_click(self):
        Right.show()
    def nextLesson(self):
        Congraplace.show()
        self.close()
    def Back_to_U1(self):
        MainPage.show()
        self.close()
class Congraplace(QMainWindow,QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("Gui/congra.ui",self)
        self.bt_gotoU2.clicked.connect(self.nextUnit2)
        self.BacktoU1_6.clicked.connect(self.Back_to_U1)
    def nextUnit2(self):
        U2.show()
        self.close()
    def Back_to_U1(self):
        MainPage.show()
        self.close()
class Congraplace2(QMainWindow,QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("Gui/congra2.ui",self)
        self.bt_gotoU3.clicked.connect(self.nextUnit3)
        self.bt_backU2.clicked.connect(self.Back_to_U2)
    def nextUnit3(self):
        U3.show()
        self.close()
    def Back_to_U2(self):
        U2.show()
        self.close()
class Congraplace3(QMainWindow,QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("Gui/congra4.ui",self)
        self.bt_gotoU4.clicked.connect(self.nextUnit4)
        self.BacktoU3.clicked.connect(self.Back_to_U3)
    def Back_to_U3(self):
        U2.show()
        self.close()
    def nextUnit4(self):
        U3.show()
        self.close()
class Congraplace4(QMainWindow,QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("Gui/congra3.ui",self)
        self.go_back.clicked.connect(self.Finalcongra)
    def Finalcongra(self):
        MainPage.show()
        self.close()
class Finishtest(QMainWindow,QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("Gui/Midtermfinishpage.ui",self)
        self.back.clicked.connect(self.Back)
    def Back(self):
        MainPage.show()
        self.close
class MidTest(QMainWindow,QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("Gui/midtermtestui.ui",self)
        self.submit.clicked.connect(self.finish_page)
        self.back.clicked.connect(self.Back)
    def Back(self):
        MainPage.show()
        self.close()
    def finish_page(self):
        Finishtest.show()
        self.close()    
class FinalTest(QMainWindow,QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("Gui/FinalTest.ui",self)
        self.submit.clicked.connect(self.finish_page)
        self.back.clicked.connect(self.Back)
    def finish_page(self):
        Finishtest.show()
        self.close()  
    def Back(self):
        MainPage.show()
        self.close()
#Unit 2 place
class U2(QMainWindow,QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("Gui/Unit2.ui",self)
        # self.les1.clicked.connect(self.button_U2les1)
        self.les2.clicked.connect(self.button_les2)
        # self.les3.clicked.connect(self.button_les3)
        self.les4.clicked.connect(self.button_les4)
        self.les5.clicked.connect(self.button_les5)
        self.quit.clicked.connect(self.button_quit)
        self.logout.clicked.connect(self.button_logout)
        self.U1.clicked.connect(self.button_U1)
        self.midtest.clicked.connect(self.button_midterm)
        self.U3.clicked.connect(self.button_U3)
        self.U4.clicked.connect(self.button_U4)
        self.FinalTest.clicked.connect(self.button_finaltest)
    # def button_U2les1(self):
    #     U2L1.show()
    #     self.close()
    def button_les2(self):
        U2L2.show()
        self.close()
    # def button_les3(self):
    #     U2L3.show()
    #     self.close()
    def button_les4(self):
        U2L4.show()
        self.close()
    def button_les5(self):
        U2L5.show()
        self.close()
    def button_midterm(self):
        MidTest.show()
        self.close()
    def button_U1(self):
        MainPage.show()
        self.close()
    def button_U3(self):
        U3.show()
        self.close()
    def button_U4(self):
        U4.show()
        self.close()
    def button_finaltest(self):
        FinalTest.show()
        self.close()
    def button_logout(self):
        LoginPage.show()
        self.close()
    def button_quit(self):
        ComputerPage.show()
        self.close()
# class U2L1(QMainWindow,QWidget):
#     def __init__(self):
#         super().__init__()
#         uic.loadUi("Gui/music1.ui",self)
class U2L2(QMainWindow,QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("Gui/music2.ui",self)
        self.wrong.clicked.connect(self.Wrong_place)
        self.right.clicked.connect(self.Correct_place)
        self.wrong2.clicked.connect(self.Wrong_place)
        self.right2.clicked.connect(self.Correct_place)
        self.wrong3.clicked.connect(self.Wrong_place)
        self.wrong4.clicked.connect(self.Wrong_place)
        self.wrong5.clicked.connect(self.Wrong_place)
        self.wrong6.clicked.connect(self.Wrong_place)
        self.right3.clicked.connect(self.Correct_place)
        self.bt_next.clicked.connect(self.Next_place)
        self.bt_backU2.clicked.connect(self.back_U2_place)
    def Next_place(self):
        U2L4.show()
        self.close()
    def back_U2_place(self):
        U2.show()
        self.close()
    def Wrong_place(self):
        Wrong.show()
    def Correct_place(self):
        Right.show()
        
# class U2L3(QMainWindow,QWidget):
#     def __init__(self):
#         super().__init__()
#         uic.loadUi("Gui/music3.ui",self)
class U2L4(QMainWindow,QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("Gui/music4.ui",self)
        self.bt_NL.clicked.connect(self.Next_place)
        self.bt_backU2.clicked.connect(self.back_U2_place)
        self.classical.clicked.connect(self.Correct_place)
        self.pop.clicked.connect(self.Wrong_place)
        self.rock.clicked.connect(self.Wrong_place)
        self.eletronic.clicked.connect(self.Wrong_place)
        self.rock2.clicked.connect(self.Correct_place)
        self.pop2.clicked.connect(self.Wrong_place)
        self.eletronic2.clicked.connect(self.Wrong_place)
        self.classical2.clicked.connect(self.Wrong_place)
        self.pop3.clicked.connect(self.Correct_place)
        self.eletronic3.clicked.connect(self.Correct_place)
        self.classical.clicked.connect(self.Wrong_place)
        self.rock3.clicked.connect(self.Wrong_place)
    def Wrong_place(self):
        Wrong.show()
    def Correct_place(self):
        Right.show()
    def Next_place(self):
        U2L5.show()
        self.close()
    def back_U2_place(self):
        U2.show()
        self.close()
    

class U2L5(QMainWindow,QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("Gui/music5.ui",self)
        self.bt_NL.clicked.connect(self.Next_place)
        self.Back_U2.clicked.connect(self.back_U2_place)
        self.classical1.clicked.connect(self.Correct_place)
        self.pop1.clicked.connect(self.Wrong_place)
        self.rock1.clicked.connect(self.Wrong_place)
        self.classical2.clicked.connect(self.Wrong_place)
        self.pop2.clicked.connect(self.Wrong_place)
        self.rock2.clicked.connect(self.Correct_place)
        self.classical3.clicked.connect(self.Wrong_place)
        self.pop3.clicked.connect(self.Correct_place)
        self.rock3.clicked.connect(self.Wrong_place)
    def Wrong_place(self):
        Wrong.show()
    def Correct_place(self):
        Right.show()
    def Next_place(self):
        Congraplace2.show()
        self.close()
    def back_U2_place(self):
        U2.show()
        self.close()

#Unit 3 place
class U3(QMainWindow,QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("Gui/Unit3.ui",self)
        self.Quit.clicked.connect(self.Quit_place)
        self.Logout.clicked.connect(self.Logout_place)
        self.U1.clicked.connect(self.Goto_U1)
        self.U2.clicked.connect(self.Goto_U2)
        self.U4.clicked.connect(self.Goto_U4)
        self.midtest.clicked.connect(self.Midterm_test)
        self.finaltest.clicked.connect(self.Final_test)
        self.les1.clicked.connect(self.U3les1)
        self.les2.clicked.connect(self.U3les2)
        self.les3.clicked.connect(self.U3les3)
        self.les4.clicked.connect(self.U3les4)
    def U3les4(self):
        U3L4.show()
        self.close()
    def U3les3(self):
        U3L3.show()
        self.close()
    def U3les2(self):
        U3L2.show()
        self.close()
    def U3les1(self):
        U3L1.show()
        self.close()
    def Final_test(self):
        FinalTest.show()
        self.close()
    def Midterm_test(self):
        MidTest.show()
        self.close()
    def Goto_U4(self):
        U4.show()
        self.close()
    def Goto_U2(self):
        U2.show()
        self.close()
    def Goto_U1(self):
        MainPage.show()
        self.close()
    def Logout_place(self):
        LoginPage.show()
        self.close()
    def Quit_place(self):
        ComputerPage.show()
        self.close()
class U3L1(QMainWindow,QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("Gui/house2.ui",self)
        self.bt_next.clicked.connect(self.next_place)
        self.bt_backU3.clicked.connect(self.backtoU3)
    def backtoU3(self):
        U3.show()
        self.close()
    def next_place(self):
        U3L2.show()
        self.close()
class U3L2(QMainWindow,QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("Gui/house3.ui",self)
        self.bt_next.clicked.connect(self.next_place)
        self.bt_backU3.clicked.connect(self.backtoU3)
        self.bt_correct.clicked.connect(self.Correct_place)
        self.bt_wrong.clicked.connect(self.Wrong_place)
        self.bt_wrong2.clicked.connect(self.Wrong_place)
        self.bt_next.clicked.connect(self.next_place)
        self.bt_backU3.clicked.connect(self.backtoU3)
    def backtoU3(self):
        U3.show()
        self.close()
    def next_place(self):
        U3L3.show()
        self.close()
    def Correct_place(self):
        Right.show()
    def Wrong_place(self):
        Wrong.show()
    def backtoU3(self):
        U3.show()
        self.close()
    def next_place(self):
        U3L3.show()
        self.close()
class U3L3(QMainWindow,QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("Gui/house4.ui",self)
        self.school.clicked.connect(self.Wrong_place)
        self.table.clicked.connect(self.Wrong_place)
        self.house.clicked.connect(self.Correct_place)
        self.bt_next.clicked.connect(self.next_place)
        self.bt_backU3.clicked.connect(self.backtoU3)
    def backtoU3(self):
        U3.show()
        self.close()
    def next_place(self):
        U3L4.show()
        self.close()
    def Correct_place(self):
        Right.show()
    def Wrong_place(self):
        Wrong.show()
class U3L4(QMainWindow,QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("Gui/house5.ui",self)
        self.bt_nextlesson.clicked.connect(self.Next_place)
        self.bt_backtoU3.clicked.connect(self.backtoU3)
        self.correct.clicked.connect(self.Correct_place)
        self.correct2.clicked.connect(self.Correct_place)
        self.correct3.clicked.connect(self.Correct_place)
        self.wrong.clicked.connect(self.Wrong_place)
        self.wrong2.clicked.connect(self.Wrong_place)
        self.wrong3.clicked.connect(self.Wrong_place)
        self.wrong4.clicked.connect(self.Wrong_place)
        self.wrong5.clicked.connect(self.Wrong_place)
        self.wrong6.clicked.connect(self.Wrong_place)
    def backtoU3(self):
        U3.show()
        self.close()
    def Next_place(self):
        Congraplace3.show()
        self.close()
    def Correct_place(self):
        Right.show()
    def Wrong_place(self):
        Wrong.show()
#Unit 4 place
class U4(QMainWindow,QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("Gui/Unit4.ui",self)
        self.Quit.clicked.connect(self.Quit_place)
        self.Logout.clicked.connect(self.Logout_place)
        self.U1.clicked.connect(self.Goto_U1)
        self.U2.clicked.connect(self.Goto_U2)
        self.U3.clicked.connect(self.Goto_U3)
        self.midtest.clicked.connect(self.Midterm_test)
        self.finaltest.clicked.connect(self.Final_test)
        self.les1.clicked.connect(self.U4les1)
        self.les2.clicked.connect(self.U4les2)
        self.les3.clicked.connect(self.U4les3)
    def U4les1(self):
        U4L1.show()
        self.close()
    def U4les2(self):
        U4L2.show()
        self.close()
    def U4les3(self):
        U4L3.show()
        self.close()
    def Final_test(self):
        FinalTest.show()
        self.close()
    def Midterm_test(self):
        MidTest.show()
        self.close()
    def Goto_U3(self):
        U3.show()
        self.close()
    def Goto_U2(self):
        U2.show()
        self.close()
    def Goto_U1(self):
        MainPage.show()
        self.close()
    def Logout_place(self):
        LoginPage.show()
        self.close()
    def Quit_place(self):
        ComputerPage.show()
        self.close()
class U4L1(QMainWindow,QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("Gui/food2.ui",self)
        self.bt_NL.clicked.connect(self.Next_place)
        self.backtoU4.clicked.connect(self.backtoU4_place)
    def backtoU4_place(self):
        U4.show()
        self.close()
    def Next_place(self):
        U4L2.show()
        self.close()
class U4L2(QMainWindow,QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("Gui/food4.ui",self)
        self.bt_NL.clicked.connect(self.Next_place)
        self.backtoU4.clicked.connect(self.backtoU4_place)
    def backtoU4_place(self):
        U4.show()
        self.close()
    def Next_place(self):
        U4L3.show()
        self.close()
class U4L3(QMainWindow,QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("Gui/food5.ui",self)
        self.bt_NL.clicked.connect(self.Next_place)
        self.backtoU4.clicked.connect(self.backtoU4_place)
        self.correct.clicked.connect(self.Correct_place)
        self.wrong2.clicked.connect(self.Wrong_place)
        self.wrong1.clicked.connect(self.Wrong_place)
    def Correct_place(self):
        Right.show()
    def Wrong_place(self):
        Wrong.show()
    def backtoU4_place(self):
        U4.show()
        self.close()
    def Next_place(self):
        Congraplace4.show()
        self.close()
        
# class SettingPage(QMainWindow, QWidget):
#     def __init__(self):
#         super().__init__()
#         uic.loadUi("Gui/Setting.ui",self)
#     def search_item(self):
#         search_text = self.inputUnit.text().lower()
#         self.unitList1


if __name__ == '__main__':
    app = QApplication(sys.argv)
    msg_box = QMessageBox()
    LoginPage = LoginPage()
    RegisterPage = RegisterPage()
    ErrorPage = ErrorPage()
    # U1L2 = Unit1les2()
    # U1L1 = Unit1les1()
    U1L3 = Unit1les3()
    U1L4 = Unit1les4()
    U1L5 = Unit1les5()
    Finishtest = Finishtest()
    MidTest = MidTest()
    FinalTest = FinalTest()
    Right = Right()
    Wrong = Wrong()
    U2 = U2()
    # U2L1 = U2L1()
    U2L2 = U2L2()
    # U2L3 = U2L3()
    U2L4 = U2L4()
    U2L5 = U2L5()
    U3 = U3()
    U3L1 = U3L1()
    U3L2 = U3L2()
    U3L3 = U3L3()
    U3L4 = U3L4()
    U4 = U4()
    U4L1 = U4L1()
    U4L2 = U4L2()
    U4L3 = U4L3()
    Congraplace = Congraplace()
    Congraplace2 = Congraplace2()
    Congraplace3 = Congraplace3()
    Congraplace4 = Congraplace4()
    ComputerPage = ComputerPage()
    ComputerPage.show()
    # Setting = SettingPage()
    MainPage = MainPage()
    sys.exit(app.exec())
