from ClassPage import Page
from ClassMelodyNote import MelodyNotebook


class Song:
    """
    Класс Song

    Хранит ноты и тетрадь
    notes - ноты
    notebook - тетрадь

    Имеет методы:
    add_note(note)
    play()
    change_moods(mood, start, end):
    into_pages(notes_on_page):
    """

    def __init__(self, notes = [], notebook=None):
        """
        :param notes:
        :param notebook:
        """
        self.values = notes
        self.notebook = notebook

    def __lshift__(self, right):
        """
        Добавляет новую ноту
        :param right:
        """
        self.values.append(right)

    def __getitem__(self, item):
        return self.values[item]

    def add_notebook(self, note):
        """
        Добавляет ноту в песнь
        :param note:
        """
        self.notebook = note

    def __add__(self, other):
        if self.notebook == None or other.notebook == None:
            return MelodyNotebook([self, other])
        else:
            if self.notebook != None:
                self.notebook << other
            else:
                other.note << self

    def play(self):
        """
        Пригрывает песню
        """
        for i in self.values:
            if i.note_mood == "Major":
                print(i.note_sign.upper())
            else:
                print(i.note_sign.lower())

    def change_moods(self, mood, start=0, end=-1):
        """
        Изменяет mood у нот с start до end
        :param mood:
        :param start:
        :param end:
        """
        if start == None:
            start = 0
        if end == -1 or end == None:
            end = len(self.values)

        for i in range(start, end):
            self.values[i].change_mood(mood)

    def __enter__(self):
        print("Start playing song!")
        self.play()

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Song end!")

    def __lt__(self, other):
        if len(self.values) < len(other.values):
            return True
        elif len(self.values) == len(other.values):
            mood_self = 0
            mood_other = 0
            for i in self.values:
                if i.note_mood == "Major":
                    mood_self += 1
            for i in other.values:
                if i.note_mood == "Major":
                    mood_other += 1
            if mood_self < mood_other:
                return True
            else:
                return False
        else:
            return False

    def __le__(self, other):
        if len(self.values) <= len(other.values):
            return True
        elif len(self.values) == len(other.values):
            mood_self = 0
            mood_other = 0
            for i in self.values:
                if i.note_mood == "Major":
                    mood_self += 1
            for i in other.values:
                if i.note_mood == "Major":
                    mood_other += 1
            if mood_self <= mood_other:
                return True
            else:
                return False
        else:
            return False

    def __eq__(self, other):
        if len(self.values) == len(other.values):
            mood_self = 0
            mood_other = 0
            for i in self.values:
                if i.note_mood == "Major":
                    mood_self += 1
            for i in other.values:
                if i.note_mood == "Major":
                    mood_other += 1
            if mood_self == mood_other:
                return True
            else:
                return False
        else:
            return False

    def __gt__(self, other):
        return not (self.__lt__(other))

    def __ge__(self, other):
        if len(self.values) >= len(other.values):
            return True
        elif len(self.values) == len(other.values):
            mood_self = 0
            mood_other = 0
            for i in self.values:
                if i.note_mood == "Major":
                    mood_self += 1
            for i in other.values:
                if i.note_mood == "Major":
                    mood_other += 1
            if mood_self >= mood_other:
                return True
            else:
                return False
        else:
            return False

    def __ne__(self, other):
        return not (self.__eq__(other))

    def into_pages(self, notes_on_page):
        """
        Возвращяет итератор
        :param notes_on_page:
        """
        pages = self._num_round(len(self.values) / notes_on_page)
        massive_pages = []
        for i in range(pages):
            if i == 0:
                massive_pages.append(Page(self.values[:notes_on_page], notes_on_page, i))
            elif i == pages:
                massive_pages.append(Page(self.values[notes_on_page * i:], notes_on_page, i, massive_pages[-1]))
                massive_pages[i - 1].add_next_element(massive_pages[i])
            else:
                massive_pages.append(
                    Page(self.values[notes_on_page * (i - 1):notes_on_page * i], notes_on_page, i, massive_pages[-1]))
                massive_pages[i - 1].add_next_element(massive_pages[i])
        return iter(massive_pages)

    def _num_round(self, number):
        if int(number) != number:
            return int(number) + 1
        else:
            return int(number)
