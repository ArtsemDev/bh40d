# def main(a, b, c=5, *args, **kwargs):
#     d = a * b * c
#     return d


def foo(*, a, b, c, **kwargs):
    pass


def bar(func):
    func()


def baz():
    print("baz")


def decorator(decorator_argument1, decorator_argument2):
    def wrapped(func):

        def wrapper(*args, **kwargs):
            print("Pre process")
            res = func(*args, **kwargs)
            print("Post process")
            return res

        return wrapper

    return wrapped


@decorator(3, 4)
def func1(a, b, c=None):
    print("Process")
    return


@decorator(7, 3)
def func2(e, k=5):
    return


decorated_func1 = decorator(4, 5)(func1)


def geom_range(start, multiply, count):
    for _ in range(count):
        yield start
        start *= multiply


# for i in geom_range(2, 2, 5):
#     print(i)


#  Написать генератор, принимающий 3 аргумента:
#  number: int
#  start: int
#  end: int
#  генератор должен возвращать number в степени от start до end
#  example: number=2, start=2, end=4
#  result: 4, 8, 16

def func(number, start, end, step=1):
    for i in range(start, end+1, step):
        yield pow(number, i)


# for i in func(2, 2, 5):
#     print(i)

# a = func(2, 2, 5)


def global_func():
    a = 5
    b = 6

    def local_func():
        print(a * b)

    return local_func

# from sys import getrecursionlimit, setrecursionlimit
# print(getrecursionlimit())
# setrecursionlimit(1500)


def recursive_func(a):
    print(a)
    if a > 0:
        recursive_func(a - 1)


# worlds = ["Hello", "apple", "Age", "python", "World"]
# worlds.sort(key=str.lower)
# worlds.sort(key=lambda x: x.lower().strip())
# print(worlds)


#  Написать функцию paginator
#  функция принимает:
#  objs - список любых объектов
#  page - номер страницы (положительное целое число)
#  paginate_by - количество объектов на странице (положительное целое число)
#  функция должна вернуть список объектов на указанной странице
#  example:
#  objs = ["Hello", "World", "Python", "PyCharm", "Belhard", "JetBrains", "Apple]
#  page = 2
#  paginate_by = 2
#  result = ["Python", "PyCharm"]

# page = 1
# paginate_by = 2
# # 0:2
#
# page = 2
# paginate_by = 2
# # 2:4
#
# page = 3
# paginate_by = 2
# # 4:6


def paginator(objs, page, paginate_by):
    return objs[page * paginate_by - paginate_by:page * paginate_by]


#  написать функция min_divisor
#  функция принимает положительное натуральное число
#  и должна возвращать наименьший делитель числа отличный от 1


def min_divisor(number):
    for i in range(2, number+1):
        if number % i == 0:
            return i


#  написать функция upper_count
#  функция принимает строку и возвращает количество больших букв


def upper_count(text):
    c = 0
    for i in text:
        if i.isupper():
            c += 1
    return c


#  написать функция factorial
#  функция принимает целое положительное число и возвращает факториал числа
#  ** ДОП: решить через рекурсию


def factorial(number):
    res = 1
    for i in range(2, number+1):
        res *= i
    return res


def recursive_factorial(number):
    if number > 2:
        return number * recursive_factorial(number-1)
    return number


# users = {
#     1: {"name": "Alex"},
#     2: {"name": "Pavel", "email": None},
#     3: {"name": "Max", "email": ""},
#     4: {"name": "Maria", "email": "maria@gmail.com"}
# }


from typing import TypeVar


T = TypeVar("T")


def find_user_without_email(users: dict[int, dict[str, T]]) -> list[str]:
    result = []
    for user in users.values():  # type: dict[str, T]
        if not user.get("email"):
            result.append(user.get("name"))
    return result


# objs = [1, 2, 3, 4, "hello", "world", None, True, "python", 4, 5]
# result = list(filter(lambda x: isinstance(x, str), objs))
# print(result)
# i = 0
# while i < len(objs):
#     if not isinstance(objs[i], str):
#         del objs[i]
#     else:
#         i += 1
