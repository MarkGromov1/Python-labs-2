class Book:
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"

    @property
    def name(self) -> str:
        return self._name

    @property
    def author(self) -> str:
        return self._author


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    def __str__(self):
        return f"{super().__str__()} Количество страниц {self.pages}"

    def __repr__(self):
        return f"{super().__repr__().replace(')', '')}, pages={self.pages!r})"

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, pages: int) -> None:
        if not isinstance(pages, int):
            raise TypeError
        if pages < 0:
            raise ValueError
        self._pages = pages


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    def __str__(self):
        return f"{super().__str__()} Продолжительность {self.duration} секунд"

    def __repr__(self):
        return f"{super().__repr__().replace(')', '')}, duration={self.duration!r})"

    @property
    def duration(self) -> float:
        return self._duration

    @duration.setter
    def duration(self, duration: float) -> None:
        if not isinstance(duration, float):
            raise TypeError
        if duration < 0:
            raise ValueError
        self._duration = duration


# print(Book("Букварь", "Громов М.В."))
# print(PaperBook("Азбука", "Бакулин П.Ю.", 165))
# print(AudioBook("Словарь", "Васютин П.Е.", 165.25))
