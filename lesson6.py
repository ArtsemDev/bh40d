# # def multiply(a, b=2):
# #     c = a * b
# #     return c
# #
# #
# # def bar(*args, **kwargs):
# #     print(args)
# #     print(kwargs)
# #
# #
# # def baz(a, b=None):
# #     if b is None:
# #         b = []
# #     b.append(a)
# #     print(b)
# #
# #
# # def func(a):
# #     a()
# #
# #
# # def callback():
# #     print("callback")
# #
# #
# # # numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# # # result = list(map(lambda x: x**2, numbers))
# # # print(result)
# # # result = list(filter(lambda x: x % 2, numbers))
# # # print(result)
# #
# #
# # # cities = ["Minsk", "Mogilev", "Gomel", "Brest"]
# # # population_density = [23.4, 15.8, 31.6, 7.7]
# # # result = list(zip(cities, population_density, strict=True))
# # # print(result)
# #
# # # objs = [4, 3, "78", "4", 45, "98"]
# # # objs.sort(key=int)
# # # print(objs)
# #
# # # numbers = [7, 65, 3, 8, -56, -234, 456, -1384, 654]
# # # print(max(numbers, key=abs))
# #
# #
# # #  Дан список словарей, каждый словарь содержит имя и возраст пользователя
# # #  1. необходимо отсортировать список по убыванию возрастов
# # #  2. найти самого молодого пользователя
# #
# # # users = [
# # #     {"name": "Alex", "age": 34},
# # #     {"name": "Pavel", "age": 46},
# # #     {"name": "Maria", "age": 18},
# # #     {"name": "Max", "age": 24},
# # # ]
# # # users.sort(key=lambda x: x.get("age"))
# # # print(users)
# #
# #
# # # def foo(a, b):
# # #     for i in range(a, b):
# # #         yield i**2
# # #
# # #
# # # a = foo(4, 10)
# # # for i in a:
# # #     print(i)
# #
# #
# # # def infinity_range(start, step):
# # #     while True:
# # #         yield start
# # #         start += step
# #
# #
# # # for i in infinity_range(2, 2):
# # #     print(i)
# #
# #
# # a = 5
#
#
# # def foo():
# #     a = 4
# #
# #     def bar():
# #         nonlocal a
# #         print(a)
# #
# #     return bar
#
#
# # globals()["foo"]()
#
#
# # def decorator(func):
# #     def wrapper(a, b):
# #         a += 2
# #         b += 2
# #         res = func(a, b)
# #         return f"{res=}"
# #
# #     return wrapper
# #
# #
# # def baz(a, b):
# #     return a * b
#
#
# # decorated_baz = decorator(baz)
# # print(baz(5, 6))
# # print(decorated_baz(5, 6))
#
#
# def decorator(a):
#     def wrapper(func):
#         def wrapped(b, d):
#             b += a
#             d += a
#             res = func(b, d)
#             return f"{res=}"
#
#         return wrapped
#
#     return wrapper
#
#
# @decorator(3)
# def foo(b, d):
#     return b * d
#
#
# # print(foo(1, 2))
#
#
register = {}


def dispatcher(text):
    def wrapper(func):
        register[text] = func

        def wrapped():
            return func()

        return wrapped

    return wrapper


@dispatcher(text="Hello")
def func1():
    return "Hey"


#
#
# @dispatcher(text="Bye")
# def func2():
#     return "Good Bye"
#
#
# def error():
#     return "Error"
#
#
# def func3(a, b, c):
#     return a * b * c
#
#
# # objs = {"a": 3, "b": 4, "c": 5}
# # print(func3(**objs))
#
#
# # numbers = [*range(1, 10)]
# # print(numbers)
# # numbers = "1234567"
# # a, b, *c = numbers
# # print(a)
# # print(b)
# # print(c)
#
#
# data = {"b": 3, "a": 5, "c": 4}
#
#
# def foo2(a, b, c):
#     return a * b * c
#
#
# print(foo2(a=data.get("a"), b=data.get("b"), c=data.get("c")))

a = [
    4,
    5,
    2,
    3,
    4,
    3,
    [
        5,
        4,
        5,
        4,
        3,
        4,
        3,
        [
            6,
            5,
            6,
            4,
            5,
            3,
            4,
        ],
        [
            6,
            5,
            6,
            45,
            4,
            [
                5,
                2,
                2,
                3,
                2,
                7,
                [
                    8,
                    6,
                    7,
                    4,
                    5,
                ],
            ],
        ],
    ],
]


def recursive_multiply(numbers):
    result = 1
    for number in numbers:
        if isinstance(number, int):
            result *= number
        else:
            result *= recursive_multiply(number)
    return result


# print(recursive_multiply(a))
