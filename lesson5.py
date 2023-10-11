# a = 4
# if a > 0:
#     print("a is positive")
# elif a == 0:
#     print("a is zero")
# else:
#     print("a is negative")

# text = "qwertyu"
# if not text.isalpha():
#     pass

# numbers = []
# if not numbers:
#     pass

# a = int(input())
# is_even = "No" if a % 2 else "Yes"
#
# if a % 2:
#     is_even = "No"
# else:
#     is_even = "Yes"
#

# a = 5
# if a == 0 or a > 0 and a % 2:
#     pass

# a = 5
# if a > 6 and a % 2:
#     pass

# a = 5
# if isinstance(a, str) and a.isdigit():
#     pass

# x = True
# y = False
# z = False
# if not x or y:
#     print(1)
# elif not x or not y and z:
#     print(2)
# elif not x or y or not y and x:
#     print(3)
# else:
#     print(4)

# BAD
# a = "hello"
# if a.isdigit():
#     pass
# else:
#     print()

# text = ""

# for i in range(100):
#     i *= 2
#     print(i)

# numbers = [2 ** i for i in range(1, 5) if i % 2]
# for i in range(1, 100):
#     if i % 2:
#         numbers.append(2 ** i)


# text = ["world", "python", "pycharm"]
# for i in text:
#     print(i)

# data = {
#     "key1": "value1",
#     "key2": "value2",
#     "key3": "value3",
#     "key4": "value4",
#     "key5": "value5",
# }
# for i, j in data.items():
#     print(i, j)

# text = "Hello"
# for i, value in enumerate(text):
#     print(i, value)

# data = [(1, 2, 3, 11, 12), (4, 5, 6, 10), (7, 8, 9)]
# for i, j, k, *m in data:
#     print(i, j, k, m)


# users = ({"name": "alex"}, {"name": "pavel"}, {"name": "maria"})
# for user in users:
#     pass

# for i in range(1, 100):
#     if i % 7 == 0:
#         continue
#     print(i)

# for i in range(10):
#     if i == 10:
#         break
#     print(i)
# else:
#     print("finish")

# a = 0
# while a < 10:
#     a += 1
#     print(a)

#  Пользователь в 1 день пробегает 100 м, каждый последующий день
#  он пробегает на 10 % больше чем в предыдущий
#  на какой день пользователь будет пробегать больше 200м
# start = 100
# days = 1
# while start < 200:
#     start += start * 0.1
#     # start *= 1.1
#     days += 1
# print(start)
# print(days)


#  Пользователь вводит целое положительное число
#  вывести True если число является простым, и False в противном случае
# n = int(input())
# if n < 2:
#     print(False)
# else:
#     for i in range(2, n // 2):
#         if n % i == 0:
#             print(False)
#             break
#     else:
#         print(True)


# words = ["hello", "python", "world"]
#
# for word in words:
#     for letter in word:
#         print(letter)


#  Дан список строк, в каждой строке через запятую написаны следующие данные:
#  НазваниеГорода,колличествоНаселенияНа2010,колличествоНаселенияНа2020
#  objs = ["Idaho,1567582,1839106", "Hawaii,1360301,1455271"]
#  Необходимо сформировать словарь, где в качестве ключей будет выступать название города
#  а в качестве значений, прирост населения с 2010 по 2020
#  data = {"Idaho": 271524, "Hawaii": 94970}


# cities = ["Idaho,1567582,1839106", "Hawaii,1360301,1455271"]
# data = {}
# for city in cities:
#     # VAR 1
#     city = city.split(",")
#     print(city)
#     data[city[0]] = int(city[2]) - int(city[1])
#     # VAR 2
#     # name, count2010, count2020 = city.split(",")
#     # count2010 = int(count2010)
#     # count2020 = int(count2020)
#     # data[name] = count2020 - count2010
# print(data)


# numbers = [1, 2, 3, 4]
# for number in numbers:
#     numbers.append(number)

# numbers = [5, 5, 4, 4, 3, 4, 3, 5, 6, 6, 7, 8]
# for number in numbers.copy():
#     if number % 2:
#         numbers.remove(number)
# print(numbers)


# numbers = [5, 5, 4, 4, 3, 4, 3, 5, 6, 6, 7, 8]
# for i in range(len(numbers)):
#     print(numbers[i])

# try:
#     a = float(input())
#     b = float(input())
#     c = a / b
# except ValueError as e:
#     print("введено не число")
#     print(e)
# except ZeroDivisionError:
#     print("на 0 делить нельзя")
# except Exception:
#     print()
# else:
#     print("ошибок не было")
# finally:
#     print("выполняется в любом случае")

# try:
#     print()
# finally:
#     print()

# raise ValueError("error")

# N = 5
# M = 3
# K = -10
# -9 -6 -3 0 3


# N = 34
# 2 4 6 8 10
# 12 14 16 18 20
# 22 24 26 28 30
# 32 34

# from dis import dis

# 7.458031177520752e-06 28
# print(
#     dis(
#         """n = 5
# numbers = [2 ** i for i in range(1, n+1)]"""
#     )
# )

# 8.917064405977726e-06 27
# print(
#     dis(
#         """n = 5
# numbers = []
# for i in range(1, n+1):
#     numbers.append(2 ** i)"""
#     )
# )
# a = []
# a.append(a)
# print(a)
