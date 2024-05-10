import json

class AnimeItem:
    def __init__(self, anime_id,title,release_data, \
                 image = None,rating= None, link = None):
        self.id = anime_id
        self.title = title
        self.release_data = release_data
        self.image = image
        self.rating = float(rating) if rating else 0
        self.link = link
anime = AnimeItem(1, "One Piece" , "01/01/2001")
with open("data.json","w") as file:
    json.dump(anime.__dict__,file)