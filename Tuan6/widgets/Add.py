import sys
from PyQt6 import uic
from PyQt6.QtWidgets import *

class Add(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/Create.ui", self)
        self.Add.clicked.connect(self.add_item)
    def add_item(self):
        text = self.add_input.text()
        if text:
            # Add vo list widget
            Item = QListWidgetItem(text)
            self.page_listwidget.listWidget.addItem(Item)
    def set_page(self, page_listwidget):
        self.page_listwidget = page_listwidget