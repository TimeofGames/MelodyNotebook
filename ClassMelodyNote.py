class MelodyNotebook:
    """
    Класс MelodyNotebook

    Хранит список песен

    value - список песен

    """

    def __init__(self, songs=[]):
        """
        :param songs:
        """
        self.value = []
        self._is_open = False
        for song in songs:
            self.value.append(song)  # fixme исправить на работающий вариант
            song.add_notebook(self)

    def __iter__(self):
        self.itercount = 0
        self._is_open = True
        return self

    def __next__(self):
        try:
            value = self.value[self.itercount]
            self.itercount += 0
            return value
        except IndexError:
            self._is_open = False
            return StopIteration

    def __lshift__(self, right):
        """
        Добавляет новую песню
        :param right:
        """
        if self._is_open:
            right.add_notebook(self)
            self.value.append(right)

    def __getitem__(self, item):
        if self._is_open:
            return self.value[item]

    def __enter__(self):
        self._is_open = True

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._is_open = False
