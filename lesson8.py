from typing import Any


# class User:
#
#     def __init__(self, name, email=None):
#         if not name.isalpha():
#             raise ValueError
#
#         if email is not None and "@" not in email:
#             raise ValueError
#
#         self.name = name
#         self.email = email
#
#     @classmethod
#     def bar(cls):
#         print("bar")
#
#     def foo(self):
#         print("foo")
#
#     @staticmethod
#     def baz():
#         print("baz")


# vasya = User(name="Vasya", email="vasya@gmail.com")
# petya = User(name="Petya")
# print(vasya.email)
# print(petya.email)
# User.foo(vasya)
# vasya.foo()
# petya.foo()
# vasya.email = "vasya@gmail.com"
# User.name = "Admin"
# print(vasya.name is petya.name is User.name)
# print(petya.name)


#  Написать класс Product
#  1. конструктор должен принимать атрибуты name: str, descr: str, price: positive float
#  аргументы конструктора должны проверяться на тип, цена должна проверяться на положительность
#  если все аргументы валидные, объявить атрибуты объекта на их основании
#  2. объявить метод dump который будет возвращать словарь, с ключами name, descr, price
#  а значения - значения соответствующих атрибутов объекта
from functools import total_ordering


@total_ordering
class Product:
    """Класс представления товара"""

    def __init__(self, name: str, descr: str, price: float) -> None:
        """Инициализация атрибутов объекта

        :param name: Название товара
        :param descr: Описание товара
        :param price: Цена товара
        """

        if not isinstance(name, str):
            raise TypeError("argument name must be string")

        if not isinstance(descr, str):
            raise TypeError("argument descr must be string")

        if not isinstance(price, (float, int)):
            raise TypeError("argument price must be float")

        if price < 0:
            raise ValueError("argument price must be great then 0")

        self.name = name
        self.descr = descr
        self.price = price

    def dump(self) -> dict[str, Any]:
        """Сериализация объекта

        :return: Словарь с данными объекта
        """
        return {"name": self.name, "descr": self.descr, "price": self.price}

    def __str__(self) -> str:
        return f"{self.name}, {self.descr}, {self.price}"

    # def __bool__(self) -> bool:
    #     return bool(self.price)

    def __len__(self) -> int:
        return round(self.price)

    def __getitem__(self, item):
        return self.name[item]

    # def __iter__(self):
    #     return self
    #
    # def __next__(self):
    #     self.i += 1
    #     if self.i < len(self.name):
    #         return self.name[self.i]
    #     else:
    #         self.i = -1
    #         raise StopIteration

    def __gt__(self, other):
        if isinstance(other, Product):
            return self.price > other.price
        elif isinstance(other, (int, float)):
            return self.price > other
        raise TypeError

    # def __le__(self, other):
    #     return not self.__gt__(other)
    #
    # def __lt__(self, other):
    #     if isinstance(other, Product):
    #         return self.price < other.price
    #     elif isinstance(other, (int, float)):
    #         return self.price < other
    #     raise TypeError
    #
    # def __ge__(self, other):
    #     return not self.__lt__(other)

    def __eq__(self, other):
        if isinstance(other, Product):
            return self.price == other.price
        elif isinstance(other, (int, float)):
            return self.price == other
        raise TypeError

    # def __ne__(self, other):
    #     return not self.__eq__(other)

    def __add__(self, other):
        if isinstance(other, Product):
            return self.price + other.price
        elif isinstance(other, (int, float)):
            return self.price + other
        raise TypeError

    def __radd__(self, other):
        return self.__add__(other)

    def __iadd__(self, other):
        if isinstance(other, Product):
            self.price += other.price
        elif isinstance(other, (int, float)):
            self.price += other
        else:
            raise TypeError

        return self


# prod1 = Product(name="Cappuccino", descr="Hot, with milk", price=4)
# print(prod1.__class__)
# print(prod1.dump.__doc__)
# prod2 = Product(name="Latte", descr="Hot, with milk", price=5)
# prod1 += prod2
# print(prod1.price)
# print(Product.__doc__)
# print(Product.__name__)
