import datetime


class Post:
    number_of_Post_instances = 0

    def __init__(self, title="Reflective Post", text="", date=None):
        self._title = title
        self._text = text
        self.__date_created = date if date is not None else datetime.date.today()
        Post.number_of_Post_instances += 1

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, new_title):
        self._title = new_title

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, new_text):
        self._text = new_text

    @property
    def date(self):
        return self.__date_created

    def make_post(self):
        return f"""
               <h2>{self._title}</h2>
               <p>{self.date}</p>
               <p>{self._text} is an instance of a class Person.</p>
           """
