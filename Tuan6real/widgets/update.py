import sys
from PyQt6 import uic
from PyQt6.QtWidgets import *

class update(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/edit.ui", self)
        self.buttonBox.clicked.connect(self.update_item)
    def update_item(self):
        selected_items = self.page_listwidget.listWidget.selectedItems()
        if selected_items:
            text = self.lineEdit.text()
            if text:
                selected_items[0].setText(text)
    def set_page(self, page_listwidget):
        self.page_listwidget = page_listwidget