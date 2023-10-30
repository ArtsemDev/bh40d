# file = open(
#     file="/Users/milvus/PycharmProjects/belhard40d/input.txt",
#     mode="a",
#     encoding="utf-8",
# )
# file.close()


# with (
#     open(
#         file="/Users/milvus/PycharmProjects/belhard40d/input.txt",
#         mode="r",
#         encoding="utf-8"
#     ) as input_file,
#     open(
#         file="output.txt",
#         mode="w",
#         encoding="utf08"
#     ) as output_file
# ):
#     pass


class A:

    def __init__(self):
        self.closed = False

    def close(self):
        self.closed = True

    def __enter__(self):
        self.closed = False
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()


# with A():
#     pass
#     print(obj.closed)
# print(obj.closed)


# with open(file="input.txt", mode="r", encoding="utf-8") as file:
#     file.read()
#     file.seek(0)
#     print(file.read())

from json import load, loads, dumps, dump

# text = '''
# {
#   "name": "Alex",
#   "age": 32,
#   "is_human": true,
#   "city": null,
#   "languages": ["ru", "en"]
# }
# '''
# data = loads(text)
# print(data)
# with open("input.json", "r") as file:
#     data = load(file)
#     print(data)

# data = {"name": "Вася", "email": "vasya@gmail.com"}
#
# with open(file="output.json", mode="w", encoding="utf-8") as file:
#     dump(data, file, indent=2, ensure_ascii=False)

from csv import reader, DictReader, writer, DictWriter


# with open("input.csv", "r") as file:
    # r = reader(file)
    # for line in r:
    #     print(line)
    # for line in file:
    #     print(line.strip().split(","))
    # r = DictReader(file)
    # for line in r:
    #     print(line)

# with open("out.csv", "w") as file:
#     w = DictWriter(file, fieldnames=("name", "email"))
#     w.writeheader()
#     w.writerow({"name": "vasya", "email": "vasya@gmail.com"})

# from configparser import ConfigParser
#
#
# parser = ConfigParser()
# parser.read(filenames="config.ini", encoding="utf-8")
# from yaml import safe_load
#
#
# with open("config.yml", "r") as file:
#     data = safe_load(file)
#     print(data)
