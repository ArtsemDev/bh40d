# text = r"C:\\Users\Documents" + "\\"
# print(text)
# text = "C:\\\\Users\\Documents\\"
# print(text)

# name = "Alex"
# age = 34
# text1 = "Hello %s your age %d" % (name, age)
# text2 = "Hello {} your age {}"
# text2 = text2.format(name, age)
# text3 = f"Hello {name} your age {age}"
# print(text1)
# print(text2)
# print(text3)

# a = 4.2376239
# print(f"{a:.3f}")

# print(f"\N{FIRE} {345 * 4}")


# text = "Hello world python"
# words = text.split()
# text2 = " | ".join(words)
# print(text2)

# words = text.split("--", maxsplit=1)
# words = text.rsplit("--", maxsplit=1)

# text = "Hello world python"
# text2 = text.replace("o", "", 2)
# print(text2)
# print(text.rfind("o"))
# print(text.index("O"))
# print(text.rindex("o"))
# print(text.count("o", 5, 10))
# print(text.partition(" | "))
# print(text.rpartition(" | "))
# print("34567".isdigit())
# print("34567".isdecimal())
# print("34567".isnumeric())
# text = "Hello world"
# print(text.startswith(("Hell", "hell")))
# print(text.endswith("rld"))
# a = "ß"
# print(a.lower())
# print(a.upper())
# print(a.title())
# print(a.swapcase())
# print(a.capitalize())
# print(a.casefold())

# text = "Hello\tworld\tpython\t"
# print(text.expandtabs(8))

# text = "-,-.-/.,hello...,/.,/world-----,./,./,/"
# print(text.lstrip(",./-"))
# print(text.rstrip(",./-"))
# print(text.strip(",./-"))
# text = "Hello world"
# print(text.removeprefix("Hell"))
# print(text.removesuffix("rld"))

# text = "Hello"
# print(text.center(10, "-"))
# print(text.ljust(10, "-"))
# print(text.rjust(10, "-"))
# print(text.zfill(10))

# a = "1010"
# print(a.zfill(8))

# text = "Привет"
# print(len(text.encode()))
# text = "Hello\nworld".splitlines(keepends=True)
# print(text)

# print("Alex" not in "alex@gmail.com")
# a = 4
# b = (4 * 2) // 2
# print(a is b)
# print(id(a) == id(b))
# print(id(b))


# print((-4) ** 0.5)


# a = "hello"
# b = "Hello world"
# print(b > a)

# print(bin(ord("H")))
# print(bin(ord("Ю")))
# print(chr(65))

# print(bin(14))
# print(bin(11))
# print(14 & 11)
# print(14 | 11)
# print(14 ^ 11)
# print(~-100)
# text = "Hello world"
# print(text[1], text[~1])
# print(bin(15 << 3))
# print(12 >> 2)


# Пользователь вводит предложение состоящее минимум из 2х слов
#  необходимо переставить местами первое и последнее слово
text = "Hello world python"
first_space_index = text.find(" ")
first_word = text[:first_space_index]
last_space_index = text.rfind(" ")
last_word = text[last_space_index + 1 :]
# text = text.replace(last_word, first_word, 1).replace(first_word, last_word, 1)
center = text[first_space_index : last_space_index + 1]
result = last_word + center + first_word
# print(result)

# result = text.split()
# result[0], result[-1] = result[-1], result[0]
# result = " ".join(result)
# print(result)

# a = "Hello world python"
# b = "Hello world python"
# print(a is b)
