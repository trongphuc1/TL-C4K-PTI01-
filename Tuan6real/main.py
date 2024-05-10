import sys
from PyQt6.QtWidgets import *
from PyQt6 import uic
from widgets.listwidget import listwidgets
from widgets.add import add
from widgets.update import update

if __name__ == '__main__':
    app = QApplication(sys.argv)
    page_add = add()
    page_update = update()
    page_listwidget = listwidgets(page_add, page_update)
    page_add.set_page(page_listwidget)
    page_update.set_page(page_listwidget)
    page_listwidget.show()
    app.exec()