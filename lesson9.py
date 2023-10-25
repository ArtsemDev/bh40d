from django.views.generic import ListView


class A:
    class_attr = "some class attr"

    def __str__(self):
        return self.class_attr


class B:
    class_attr = "another class attr"

    def __init__(self, obj_attr):
        self.obj_attr = obj_attr

    def foo(self):
        return "foo"


class C(A, B):

    def __init__(self, obj_attr, another_obj_attr):
        super().__init__(obj_attr=obj_attr)
        self.another_obj_attr = another_obj_attr
        self.__token = "asdfasdf"

    def foo(self):
        res = super().foo()
        return f"{res=}"

    def _request(self, raw_data):
        print(self.__token)

    def request(self, data):
        raw_response = self._request(data)


class DebtCard:

    def __init__(self, card_number):
        self.__card_number = card_number

    @property
    def card_number(self):
        return self.__card_number[:6] + "*****" + self.__card_number[-4:]

    @card_number.setter
    def card_number(self, value):
        if not isinstance(value, str):
            raise TypeError

        if not value.isdigit():
            raise ValueError

        if len(value) != 16:
            raise ValueError

        self.__card_number = value


from abc import ABC, abstractmethod


class AbstractMusic(ABC):

    @abstractmethod
    def get(self, name: str) -> dict:
        raise NotImplementedError


class YandexMusic(AbstractMusic):

    def get(self, name: str) -> dict:
        return {"name": name}


class AbstractPhone(ABC):

    @abstractmethod
    def call(self, phone):
        raise NotImplementedError


class SMSMixin:
    def sms(self, text, phone):
        raise NotImplementedError


class MobilePhone(SMSMixin, AbstractPhone):

    def sms(self, text, phone):
        pass

    def call(self, phone):
        pass


class SimplePhone(AbstractPhone):

    def call(self, phone):
        pass

# SOLID
# S - Single Responsibility
# O - Open/Close
# L - Liskov Substitution
# I - Interface Segregation
# D - Dependency Inversion


class AbstractVideo(ABC):

    @abstractmethod
    def play(self, offset: int = 0):
        pass


class Video(AbstractVideo):

    def play(self, offset: int = 0):
        print(f"play with {offset=}")


class VideoPlayer(AbstractVideo):

    def __init__(self, video: Video):
        self.video = video

    def play(self, offset: int = 0):
        self.video.play(offset)


class YoutubePlayer(VideoPlayer):
    def download(self):
        pass

    def upload(self):
        pass


# def __init__(self, title, price):
#     self.title = title
#     self.price = price
#
#
# def info(self):
#     return f"{self.title} {self.price}"
#
#
# Product = type("Product", (), {"title": None, "price": None, "__init__": __init__, "__str__": info})
#
# coffee = Product(title="Latte", price=5)
# print(coffee)


# def my_meta(name, bases, attributes):
#     attributes["b"] = 6
#     return type(name, bases, attributes)
#
#
# class A(metaclass=my_meta):
#
#     def __init__(self, a):
#         self.a = a
#
#
# a = A(a=5)
# print(a.b)


class MyMeta(type):
    def __new__(cls, name, bases, attributes):
        ...
        return type.__new__(cls, name, bases, attributes)


class B(metaclass=MyMeta):
    pass


class Singleton(type):
    _instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            instance = super().__call__(*args, **kwargs)
            cls._instance[cls] = instance
        return cls._instance[cls]


class MySingleton1(metaclass=Singleton):
    pass
