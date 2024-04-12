class Homework:
    def  __init__(self, name,priority,completed = False):
        self.priority = priority
        self.name = name
        self.completed = completed

    def all_finished():
        for lesson in items:
            if lesson.completed == "Chưa hoàn thành":
             print(lesson.name)

lesson1 = Homework("Gamemaker",1,"Chưa hoàn thành")
lesson2 = Homework("Văn",2,"Chưa hoàn thành")
lesson3 = Homework("Lập trình app producer",3,"Chưa hoàn thành")
items = [lesson1,lesson2,lesson3]

Homework.all_finished()

class HomeworkList:
    def __init__(self):
        self.items = [lesson1,lesson2,lesson3]

    def add_item(self, item):
        self.items.append(item)


