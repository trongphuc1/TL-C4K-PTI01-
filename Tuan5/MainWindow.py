import sys
from PyQt6.QtWidgets import *
from models import AnimeDatabase, AnimeItem
class MainWindow(QMainWindow):
    def __init__(self, parent:QApplication):
        global widgets
        widgets = self.ui

        global database
        self.dtb = AnimeDatabase()
        database = self.dtb

        self.setup_CRUD_page()
        ...
    def setup_CRUD_page(self):
        database.load_data()
        widgets.animeList.addItems(database.anime_title_list)
        widgets.animeList.setCurrentRow(0)
        widgets.addButton.clicked.connect(lambda:AnimeCRUD.add(self))
        widgets.editButton.clicked.connect(lambda:AnimeCRUD.edit(self))
        widgets.removeButton.clicked.connect(lambda:AnimeCRUD.remove(self))
        widgets.searchAnime.clicked.connect(lambda:AnimeCRUD.search(self))

class AnimeCRUD():
    def add(self):
        currIndex = widgets.animeList.currentRow()
        add_dialog = AddDialog()
        if add_dialog.exec():
            inputs = add_dialog.return_input_fields()
            widgets.animeList.insertItem(currIndex, inputs["title"])
            database.add_item(inputs)
    def edit(self):
        curr_index = widgets.animeList.currentRow()
        item = widgets.animeList.item(curr_index)
        item_title = item.text()
        edit_item = database.get_first_item_by_title(item_title)
        if item is not None:
            edit_dialog = EditDialog(edit_item)
            if edit_dialog.exec():
                inputs= edit_dialog
                item.setText(inputs["title"])
                database.edit_item(item_title, inputs)
    def delete(self):
        curr_index = widgets.animeList.currentRow()
        item = widgets.animeList.item(curr_index)
        item_title = item.text()
        if item is None:
            return
        question = QMessageBox.question(self, "Remove Anime?", "Do you want to remove this anime?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if question == QMessageBox.StandardButton.Yes:
            item = widgets.animeList.takeItem(curr_index)
            database.delete_item(item_title)
    def search(self):
        search_anime_field = widgets.inputAnime.text().strip().lower()
        if search_anime_field:
            matched_items = widgets.animeList.findItems(search_anime_field, Qt.MatchFlag.MatchContains)
            for i in range(widgets.animeList.count()):
                it = widgets.animeList.item(i)
                it.setHidden(it not in matched_items)
            else:
                for i in range(widgets.animeList.count()):
                    it = widgets.animeList.item(i)
                    it.setHidden(False)
