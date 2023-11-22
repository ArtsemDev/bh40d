# import pytest
from typing import Callable


def multiply(*args: int | float) -> int | float:
    """Функция нахождения произведения чисел

    :param args: Числа, произведение которых необходимо найти
    :return: Результат произведения
    """
    result = 1
    for arg in args:
        result *= arg
    return result


# @pytest.mark.parametrize(
#     argnames=("result", "args"),
#     argvalues=(
#             (24, (1, 2, 3, 4)),
#             (-40, (4, 5, 2, -1))
#     )
# )
# def test_multiply(result, args):
#     assert multiply(*args) == result

class A(object):

    def __init__(self, name):
        self.name = name
        self.__token = "rtdfg8uihj"

    @property
    def token(self):
        return self.__token

    @token.setter
    def token(self, value):
        self.__token = value

    def __str__(self):
        return self.name

    def dump(self):
        return {
            "name": self.name
        }


class B(A):

    def __init__(self, name, surname):
        super().__init__(name)
        self.surname = surname

    def __str__(self):
        r = super().__str__()
        return f"{r} {self.surname}"

    def dump(self):
        data = super().dump()
        data["surname"] = self.surname
        return data


class MyClass:

    def get_request(self, **kwargs):
        pass


class MyClass2:

    def request(self, method, url, json):
        pass


class MyClassAdapter(MyClass):

    def request(self, method, url, json):
        return self.get_request(method=method, url=url, json=json)


class Router:

    def __init__(self, name, routers: list["Router"] = None):
        self.routers = routers or []
        self.handlers = {}
        self.name = name

    def include_router(self, router: "Router"):
        self.routers.append(router)

    def feed_update(self, update):
        # for k, v in self.handlers:
        #     if k(update):
        #         return v()
        print(self.name)
        for router in self.routers:
            router.feed_update(update=update)


class Handler:

    def __init__(self, observer: "Observer"):
        self.observer = observer

    def __call__(self):
        print("process")
        self.observer.log()


class Observer:

    def __init__(self):
        self.handler = Handler(observer=self)

    def log(self):
        print("FEED")


class View:

    def __init__(self):
        self.func = None
        self.filter = None


class ViewBuilder:

    def __init__(self):
        self.view = View()

    def reset(self):
        view = self.view
        self.view = View()
        return view

    def add_func(self, func: Callable):
        self.view.func = func
        return self

    def add_filter(self, obj):
        self.view.filter = obj
        return self


def foo():
    pass


def bar():
    pass


class User:
    __slots__ = ("name", "email")

    def __init_subclass__(cls, **kwargs):
        if not kwargs.get("prefix"):
            raise AttributeError
        cls.prefix = kwargs.get("prefix")

    def __init__(self, name, email):
        self.name = name
        self.email = email


class Person(User, prefix="Person", sss=234):
    __slots__ = ("age", )
    # prefix = "Person"
