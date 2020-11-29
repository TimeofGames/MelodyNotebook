from Enums import MusicalMood
from Enums import NoteSign


class Note:
    """
    Класс Note

    Хранит в себе знак и лад.

    note_sing - нотный знак
    note_mood - нотный лад(По умалчанию Major)

    Имеет метод Change_mood(new_mood)
    """

    def __init__(self, note_sign, note_mood="Major"):
        """
        :param note_sign:
        :param note_mood: (По умалчанию Major)
        """
        self.note_signs = {
            "c": NoteSign.c,
            "d": NoteSign.d,
            "e": NoteSign.e,
            "f": NoteSign.f,
            "g": NoteSign.g,
            "a": NoteSign.a,
            "h": NoteSign.h
        }
        self.note_moods = {
            "Major": MusicalMood.Major,
            "Minor": MusicalMood.Minor
        }
        self._note_sign = self.note_signs[note_sign]
        self._note_mood = self.note_moods[note_mood]

    def __lt__(self, other):
        if self._note_sign.value < other._note_sign.value:
            return True
        elif self._note_sign.value < other._note_sign.value and self._note_mood.value < other._note_mood.value:
            return True
        else:
            return False

    def __le__(self, other):
        if self._note_sign.value <= other._note_sign.value:
            return True
        elif self._note_sign.value <= other._note_sign.value and self._note_mood.value <= other._note_mood.value:
            return True
        else:
            return False

    def __eq__(self, other):
        if self._note_sign.value == other._note_sign.value and self._note_mood.value == other._note_mood.value:
            return True
        else:
            return False

    def __gt__(self, other):
        return not (self.__lt__(other))

    def __ge__(self, other):
        if self._note_sign.value >= other._note_sign.value:
            return True
        elif self._note_sign.value >= other._note_sign.value and self._note_mood.value >= other._note_mood.value:
            return True
        else:
            return False

    def __ne__(self, other):
        return not (self.__eq__(other))

    def change_mood(self, new_mood):
        """
        Меняет Mood данной ноты
        :param new_mood:
        """
        self._note_mood = self.note_moods[new_mood]

    @property
    def note_sign(self):
        return self._note_sign.name

    @property
    def note_mood(self):
        return self._note_mood.name
