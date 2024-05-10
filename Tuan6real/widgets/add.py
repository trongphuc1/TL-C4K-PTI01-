import sys
from PyQt6 import uic
from PyQt6.QtWidgets import *

class add(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/add.ui", self)
        self.button_add.clicked.connect(self.add_item)
    def add_item(self):
        text = self.add_input.text()
        if text:
            # add vo list widget
            item = QListWidgetItem(text)
            self.page_listwidget.listWidget.addItem(item)

    def set_page(self, page_listwidget):
        self.page_listwidget = page_listwidget