import sys
from PyQt6 import uic
from PyQt6.QtWidgets import *

class ListWidget(QMainWindow):
    def __init__(self, page_add, page_update):
        self.page_add = page_add
        self.page_update = page_update
        super().__init__()
        uic.loadUi("ui/listwidget.ui", self)
        self.Add.clicked.connect(self.page_add.show)
        self.Update.clicked.connect(self.page_update.show)