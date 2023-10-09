# text = "Hello World"
# symbols = list(text)
# print(symbols)


# objs = [1, 2, 3, 4, "hello", 3, True, None]

# objs.extend(["hello", "world", "python"])
# print(objs)
# objs.insert(2, "python")
# objs.append("python")
# print(objs)
# objs.remove(3)
# a = objs.pop(0)
# print(objs)
# print(a)
# del objs[0]
# print(objs)
# print(len(objs))
# objs[0] = "World"
# print(objs)

# a = [1, 2, 3]
# b = [4, 5, 6]
# c = a + b
# print(c * 2)

# a = [5, -4, 6, -2, -7, 5]
# b = a[::-1]
# print(a)
# a.sort(key=abs)
# print(a)

# words = ["hello", "py", "pycharm", "Yep"]
# words.sort(key=str.lower)
# print(words)
# print(sorted("HeLlO"))

#
# c = [7, 8, 9]
# a = [3, 5, 4, c]
# b = deepcopy(a)
# a[-1].append(10)
# print(c)
# print(a)
# # print(a[-1] is b[-1] is c)
# b[-1].append(10)
# print(a)
# print(b)
# print(c)
# a.append(8)
# print(b[0] is a[0])

# a = [1, 2, "hello", [4, 5, 6], 7, 8, 9]
# print(a[2][3])

# a = [3, 4, 5]
# b = [3, 4, 5, 6]
# c = a + b
# e = 3
# print(c[0] is c[3] is e)
# a = (4, 5, 6, 7, [1, 2, 3])
# print(hash(a))

# a = [1, 2, 3, 4]
# b = (5, 6, 7, a)
# a.append(8)
# b *= 3
# print(b)
# a = [1, 2, 3]
# b = a
# del a
# print(b)


# data = {"age": 34, "name": "Masha"}
# data2 = {"age": 35, "city": "Minsk"}

# data3 = {**data, **data2}
# data3 = data | data2
# print(data3)
# data.update([("age", 35), ("city", "Minsk")])
# print(data)
# print(data.items())
# a = data.popitem()
# print(a)
# print(data)
# a = data.pop("city", None)
# print(data)
# print(a)
# del data["age"]
# print(data)
# print(data.setdefault("age", "Н/У"))
# print(data)
# print("name" in data)
# data["age"] = 35
# data["city"] = "Minsk"
# print(data)

# data = dict([("name", "Alex"), ("age", 34)])
# print(data)

# data = dict.fromkeys(("name", "age"))
# print(data)


# s = {4, 3, 5, 45, 6, 4, 31, 5, 4, 6, 7, 8, 9}
# print(s)
# s = set("Hello")
# print(s)


# s = {5, 6, 4, 5, 3, 4}
# s2 = {6, 5, 4, 7, 8}
# s3 = frozenset("hello")
# print(hash(s3))
# print(s.symmetric_difference(s2))
# print(s.intersection((3, 6, 7), s2))
# print(s.difference(s2))
# print(
#     s.union(
#         s2,
#         (
#             4,
#             5,
#             2,
#             4,
#         ),
#         "hello",
#     )
# )
# s.add(10)
# print(s)
# print(s.isdisjoint([41, 52, 33]))
# print(s2.issubset(s))
# print(s.issuperset(s2))


# a = [5, 6, 3, 4]
# a[1], a[3] = "Hello", "world"
# print(a)


# a = {i * 2 for i in range(1, 10, 2)}
# print(a)

# data = {i: i * 2 for i in range(10)}
# print(data)

# n = 3
# data = {
#     0: {"name": "alex", "email": "alex@gmail.com"},
#     1: {"name": "masha", "email": "masha@mail.com"},
#     2: {"name": "alex", "email": "alex@gmail.com"},
#
# }


# User = namedtuple("User", ("name", "email", "age"))
#
# vasya = User(name="Vasya", email="vasya@gmail.com", age=34)
# print(hash(vasya))

# c = Counter("Hello world")
# print(c)
# c2 = Counter("Hellq")
# print(c2)
# print(c - c2)
# # c.subtract(c2)
# # print(c)


# data = defaultdict(int)
# data["a"] += 5
# print(data)

# q = deque([2, 4, 6, 8, 10])
# q.rotate(-2)
# print(q)


#  пользователь вводит строку с клавиатуры
#  используя list comprehension заполнить список символами из строки умноженными на 3
#  примет:
#  text = "Hey"
#  result = ["HHH", "eee", "yyy"]
# text = input("Enter text: ")
# result = [text[i] * 3 for i in range(len(text))]
# print(result)

#  Пользователь вводит строку (input) сформировать словарь используя
#  dict comprehension где в качестве ключей будут использованы символы из стоки
#  а в качестве значений - номер символа из таблицы ASCII
#  example:
#  text = "Hello"
#  result = {"H": 72, "e": 101, "l": 108, "o": 111}
#  Дополнительно: найти сумму значений полученного словаря
#  с = 392
text = input("Enter text: ")
data = {i: ord(i) for i in text}
c = sum(data.values())
print(data)
print(c)
