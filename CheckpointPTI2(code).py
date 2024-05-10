import sys
import json
from CheckpointPTI2() import load_json_data, write_json_data
from PyQt6 import uic
from PyQt6.QtWidgets import *



class Homework:
    def __init__(self, name, priority, completed=False):
        self.priority = priority
        self.name = name
        self.completed = completed


class HomeworkList:

        
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def all_completed(self):
        completed = True
        for item in self.items:
            if item.completed == False:
                completed = False
            print(item.name)
        if completed:
            print("All finished!")


lesson1 = Homework("Gamemaker", 1, True)
lesson2 = Homework("Văn", 2, True)
lesson3 = Homework("Lập trình app producer", 3, True)


homework_list = HomeworkList()
homework_list.add_item(lesson1)
homework_list.add_item(lesson2)
homework_list.add_item(lesson3)


homework_list.all_completed()

class Trongphuc(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("dialog.ui", self)
        self.pushButton.clicked.connect(self.showPhuc)
    def showPhuc(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Dialog = Trongphuc()
    Dialog.show()
    app.exec()





def load_json_data():
    anime_dict_data = list()
    with open("data.json","r") as json_in:
        json_data = json.load(json_in)
    anime_dict_data.extend(json_data)
    return anime_dict_data

def write_json_data(json_data):
    with open("data.json","W") as json_out:
        json.dump(json_data, json_out)


