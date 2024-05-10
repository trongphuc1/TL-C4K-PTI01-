import sys
from PyQt6 import uic
from PyQt6.QtWidgets import *

class Update(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/Update.ui", self)
        self.Update.clicked.connect(self.update_item)
def update_item(self):
        selected_items = self.page_listwidget.listWidget.selectedItems()
        if selected_items:
            text = self.lineEdit.text()
            if text:
                selected_items[0].setText(text)