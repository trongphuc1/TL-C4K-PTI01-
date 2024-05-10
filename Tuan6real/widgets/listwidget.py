import sys
from PyQt6 import uic
from PyQt6.QtWidgets import *

class listwidgets(QMainWindow):
    def __init__(self, page_add, page_update):
        self.page_add = page_add
        self.page_update = page_update
        super().__init__()
        uic.loadUi("ui/listwidget.ui", self)
        self.add_item.clicked.connect(self.page_add.show)
        self.update_item.clicked.connect(self.page_update.show)
        self.delete_item.clicked.connect(self.remove_item)
    def remove_item(self):
        selected_items = self.listWidget.selectedItems()
        self.listWidget.takeItem(self.listWidget.row(selected_items[0]))