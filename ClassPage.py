class Page:
    """
    Класс Page

    Хранит в себе информацию о полях страницы
    notes - список нот
    notes_on_page - кол-во нот на странице
    page_number - номер страницы
    previous_element - предидущий элемент следующий элемент (если нет None)
    next_element - следующий элемент (если нет None)
    """

    def __init__(self, notes, notes_on_page, page_number, previous_element=None):
        """
        :param notes:
        :param notes_on_page:
        :param page_number:
        :param previous_element:
        """
        self.notes = notes
        self.note_count = notes_on_page
        self.page_number = page_number
        self.previous_element = previous_element
        self.next_element = None

    def add_next_element(self, next_element):
        """
        Добавляет последующий элемент
        :param next_element:
        """
        self.next_element = next_element
