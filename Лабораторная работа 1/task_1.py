class MyBudget:
    def __init__(self, savings: (int, float), salary: (int, float),
                 expenses: (int, float)):
        """
        Создание и подготовка к работе объекта "Бюджет семьи"

        :param savings: Накопления
        :param salary: Зарплата
        :param expenses: Расходы

        Примеры:
        >>> my_budget = MyBudget(100, 200, 300)
        """
        if not isinstance(savings, (int, float)):
            raise TypeError("Накопления должны быть типа int или float")
        if savings < 0:
            raise ValueError("Накопления должны быть положительным числом")
        if not isinstance(salary, (int, float)):
            raise TypeError("Зарплата должна быть типа int или float")
        if salary < 0:
            raise ValueError("Зарплата должна быть положительным числом")
        if not isinstance(expenses, (int, float)):
            raise TypeError("Расходы должны быть типа int или float")
        if expenses < 0:
            raise ValueError("Расходы должны быть положительным числом")

    def how_much(self) -> int | float:
        """
        Функция которая проверяет, равны ли доходы расходам, или больше/меньше их

        :return: Разность между зарплатой и расходами

        Примеры:
        >>> my_budget = MyBudget(100, 200, 300)
        >>> my_budget.how_much()
        -100
        """

    def possible_debts(self) -> int | float:
        """
        Функция которая определяет, останутся ли деньги на следующий месяц, или придется брать в долг

        :return: Сумма сбережений и разности между зарплатой и расходами

        Примеры:
        >>> my_budget = MyBudget(100, 200, 300)
        >>> my_budget.possible_debts()
        0
        """
        ...


class BusesForChildren:
    def __init__(self, all_children: int, children_in_bus: int,
                 available_buses: int):
        """
        Создание и подготовка к работе объекта "Автопарк"

        :param all_children: Дети, которых нужно отвезти на автобусах
        :param children_in_bus: Количество мест в автобусе для детей
        :param available_buses: Количество уже имеющихся автобусов в автопарке

        Примеры:
        >>> buses_for_children = BusesForChildren(100, 20, 4)
        """
        if not isinstance(all_children, int):
            raise TypeError("Количество детей должно быть целым числом")
        if all_children < 0:
            raise ValueError(
                "Количество детей должно быть положительным числом")
        if not isinstance(children_in_bus, int):
            raise TypeError("Количество мест должно быть целым числом")
        if children_in_bus < 0:
            raise ValueError(
                "Количество мест должно быть положительным числом")
        if not isinstance(available_buses, int):
            raise TypeError(
                "Количество имеющихся автобусов должно быть целым числом")
        if available_buses < 0:
            raise ValueError(
                "Количество имеющихся автобусов должно быть положительным числом")

    def bus_number(self) -> int:
        """
        Функция, которая определяет количество автобусов, которого хватит, чтобы уместить всех детей.

        :return: Необходимое количество автобусов, равное частному количества детей и количества мест в одном автобусе, округленному в большую сторону

        Примеры:
        >>> buses_for_children = BusesForChildren(100, 20, 4)
        >>> buses_for_children.bus_number()
        5
        """
        ...

    def new_buses(self) -> int:
        """
        Функция которая определяет, нужно ли закупать автобусы дополнительно

        :return: Разность между необходимым количеством автобусов и уже имеющимся

        Примеры:
        >>> buses_for_children = BusesForChildren(100, 20, 4)
        >>> buses_for_children.new_buses()
        1
        """
        ...


class PairOfNumbers:
    def __init__(self, first_number: int, second_number: int, divider: int):
        """
        Создание и подготовка к работе объекта "Пара чисел"

        :param first_number: Первое число
        :param second_number: Второе число
        :param divider: Делитель

        Примеры:
        >>> pair_of_numbers = PairOfNumbers(15, 20, 3)

        """
        if not isinstance(first_number, int):
            raise TypeError("Первое число должно быть целым")
        if not isinstance(second_number, int):
            raise TypeError("Второе число должно быть целым")
        if not isinstance(divider, int):
            raise TypeError("Делитель должен быть целым числом")

    def numbers_quotient(self) -> bool:
        """
        Функция, которая определяет, есть ли остаток при делении первого числа на второе, а также при делении второго числа на первое

        :return: Делится ли одно из чисел на другое без остатка

        Примеры:
        >>> pair_of_numbers = PairOfNumbers(15, 20, 3)
        >>> pair_of_numbers.numbers_quotient()
        False
        """
        ...

    def divider_quotient(self) -> bool:
        """
        Функция которая определяет, есть ли остаток при делении первого и второго чисел на делитель

        :return: Делятся ли первое и второе числа на делитель без остатка

        Примеры:
        >>> pair_of_numbers = PairOfNumbers(15, 20, 3)
        >>> pair_of_numbers.divider_quotient()
        True
        False
        """
        ...


# TODO Написать 3 класса с документацией и аннотацией типов

if __name__ == "__main__":
    import doctest
    doctest.testmod()  # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
