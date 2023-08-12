import datetime


class Post:
    number_of_Post_instances = 0

    def __init__(self, title="Reflective Post", date=None, text="", links=None, *pictures):
        if links is None:
            links = {}
        self._title = title
        self.__date_created = date if date is not None else datetime.date.today()
        self._text = text
        self._links = links
        self._pictures = pictures
        Post.number_of_Post_instances += 1

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, new_title):
        self._title = new_title

    @property
    def date(self):
        return self.__date_created

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, new_text):
        self._text = new_text

    @property
    def links(self):
        return self._links

    @property
    def pictures(self):
        return self._pictures

    @pictures.setter
    def pictures(self, new_pictures):
        self._pictures = new_pictures
