import sys
from PyQt6.QtWidgets import *
from PyQt6 import uic
from widgets.listwidget import ListWidget
from widgets.Add import Add
from widgets.Update import Update


if __name__ == '__main__':
    app = QApplication(sys.argv)
    page_add = Add()
    page_update = Update()
    page_listwidget = ListWidget(page_add, page_update)
    page_add.set_page(page_listwidget)
    page_update.set_page(page_listwidget)
    page_listwidget.show()
    app.exec()
