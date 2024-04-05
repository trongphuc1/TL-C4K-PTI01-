class Englishlesson:
    def  __init__(self,Lesson_id,Unit,release_date,rating,hardlv,title):
        self.lesson_id = Lesson_id
        self.title = title
        self.unit = Unit
        self.release_date = release_date
        self.rating = rating if rating else 0
        self.hardlv = hardlv
    def update(self, new_data:dict):
        # Thuộc tính nào trống sẽ ko cập nhật
        for attribute, value in new_data.items():
            if value:
                setattr(self,attribute,value)

    def Duyet_phan_tu():
        for lesson in Lessons:
            print(lesson.title)
    def xoa_tieu_de():
        remove_title = input( "Nhập tiêu đề bạn muốn xóa:")
        for lesson in Lessons:
            if lesson.title == remove_title:
                Lessons.remove(lesson)
    def update_lesson():
        lesson = Englishlesson(1,"School","27/04/2024",8.5,0,"Hello student")
        new_data = {"title": "Hello student"}
        lesson.update(new_data)
        print(lesson.title)
        print(lesson.release_date)

lesson1 = Englishlesson(1,"School","27/04/2024",8.5,0,"Hello student")
lesson2 = Englishlesson(2,"Music","28/04/2024",9,1,"I like music")
lesson3 = Englishlesson(3,"Home","28/04/2024",8,1,"I have big home")
lesson4 = Englishlesson(4,"Food","29/04/2024",10,2,"I like eating food")
Lessons = [lesson1,lesson2,lesson3,lesson4]
lesson5 = Englishlesson(5,"Napoleon","15/8/1769",10,2,"Napoleon:there's nothing we can do...")
Lessons.append(lesson5)
Englishlesson.Duyet_phan_tu()
Englishlesson.xoa_tieu_de()
Englishlesson.Duyet_phan_tu()
Englishlesson.update_lesson()


class Englishlessonlist:
    def __init__(self):
        self.lesson_item_list = list()
    def get_item_by_title(self, lesson_title) -> Englishlesson:
        pass
    def addPnew_item(self, Englishlessonlist):
        pass
    def edit_item(self, edit_title, lesson: Englishlesson):
        pass
    def delete_item(self, delete_title):
        pass
