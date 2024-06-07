import json
from data_io import load_json_data, write_json_data

class AnimeItem:
    def __init__(self, anime_id, title, release_date, image = None, rating = None, link = None):
        self.id = anime_id
        self.title = title
        self.release_date = release_date
        self.image = image
        self.rating = float(rating) if rating else 0
        self.link = link
anime = AnimeItem(1, "One Piece", "01/01/2001")

class AnimeDatabase:
    def __init__(self):
        self.anime_item_list = list()
        self.anime_dict_data = load_json_data()
        self.anime_title_list = self.get_title_list()
    def items_to_data(self):
        pass
    def load_data(self):
        for anime_dict in self.anime_dict_data:
            anime = AnimeItem(anime_id = anime_dict["id"],
                              title = anime_dict["title"],
                              release_date = anime_dict ["release_date"],
                              image = anime_dict ["image"],
                              rating = anime_dict ["rating"],
                              link = anime_dict ["link"])
            self.anime_item_list.append(anime)
    def get_first_item_by_title(self, anime_title):
        pass
    def add_item(self, anime_dict):
        pass
    def edit_item(self, edit_title, new_dict):
        pass
    def delete_item(self, delete_title):
        pass
    # def search_by_title(self, search_title) -> list[AnimeItem]:
    #     pass
    def sort_item_by_rating(self, top = None):
        pass
    def sort_item_by_title(self, top = None):
        pass
    def sort_item_by_date(self, top = None):
        pass
    def get_title_list(self):
        titles = [anime["Title"]  for anime in self.anime_dict_data]
        return titles   
# with open("data.json", "w") as file:
#     json.dump(anime.__dict__, file)