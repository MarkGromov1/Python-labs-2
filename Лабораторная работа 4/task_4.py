if __name__ == "__main__":
    class Auto:
        """ Базовый класс, описывающий группу автомобилей. """

        parking_places = 30

        def __init__(self, manufacturer: str, model: str, amount: int) -> None:
            """
            Создание и подготовка к работе объекта "Группа автомобилей"

            :param manufacturer: Производитель
            :param model: Модель
            :param amount: Количество автомобилей

            Пример:
            >>> my_autos = Auto("ВАЗ", "2121", 11)
            """
            self.manufacturer = manufacturer
            self.model = model
            if not isinstance(amount, int):
                raise TypeError
            if amount < 0:
                raise ValueError
            self.amount = amount
            self.parking()
            self.numbers()

        def __str__(self) -> str:
            """
            Функция, которая выводит информацию о группе автомобилей

            :return: Информация о группе автомобилей в формате строки
            """
            return f"Производитель: {self.manufacturer}. Модель: {self.model}."

        def __repr__(self) -> str:
            """
            Ещё одна функция, которая выводит информацию о группе автомобилей

            :return: Информация о группе автомобилей в формате repr
            """
            return f"{self.__class__.__name__}(manufacturer={self.manufacturer!r}, model={self.model!r})"

        def parking(self) -> None:
            """ Функция, которая определяет, хватит ли мест на парковке для автомобилей. """
            cls = self.__class__
            if cls.parking_places - self.amount >= 0:
                print("Все автомобили поместятся на парковке.")
            else:
                print("Автомобили не помещаются, парковку необходимо расширить!")

        def numbers(self) -> None:
            """ Функция, которая генерирует случайный трехзначный номер для каждого автомобиля. """
            from random import randint
            lst = [randint(100, 999) for _ in range(self.amount)]
            print(lst)

    class Truck(Auto):
        """ Дочерний класс группы грузовых автомобилей. """

        passenger_cars_in_truck = 3

        def __init__(self, manufacturer: str, model: str, amount: int, content: str) -> None:
            """
            Создание и подготовка к работе объекта "Группа грузовых автомобилей".

            Конструктор базового класса был унаследован и расширен дополнительным параметром.
            Поскольку конструктор был унаследован, то вызываемые в нём методы вызовутся и здесь.

            :param manufacturer: Производитель
            :param model: Модель
            :param amount: Количество автомобилей
            :param content: Содержимое кузова

            Пример:
            >>> my_trucks = Truck("ВАЗ", "2121", 11, "Пшено")
            """
            super().__init__(manufacturer, model, amount)
            self.content = content

        def __str__(self) -> str:
            """
            Функция, которая выводит информацию о группе автомобилей.
            Метод был перезагружен с вызовом конструктора базового класса.

            :return: Информация о группе автомобилей в формате строки
            """
            return f"{super().__str__()} Содержимое кузова: {self.content}"

        def __repr__(self) -> str:
            """
            Ещё одна функция, которая выводит информацию о группе автомобилей.
            Метод был перезагружен с вызовом конструктора базового класса.

            :return: Информация о группе автомобилей в формате repr
            """
            return f"{super().__repr__().replace(')', '')}, content={self.content!r})"

        def parking(self) -> None:
            """
            Функция, которая определяет, хватит ли мест на парковке для автомобилей.
            Этот метод был перезагружен, так как необходимо было показать, что грузовой автомобиль занимает
            несколько парковочных мест, в отличие от легкового.
            """
            cls = self.__class__
            if cls.parking_places - self.amount * cls.passenger_cars_in_truck >= 0:
                print("Все автомобили поместятся на парковке.")
            else:
                print("Автомобили не помещаются, парковку необходимо расширить!")

        # print(Auto("ВАЗ", "2121", 11))
        # print(Truck("ЗИЛ", "130", 11, "Пшено"))
        # Write your solution here


    pass
