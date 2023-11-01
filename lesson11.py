# from abc import ABC, abstractmethod
# from decimal import Decimal
# from json import load, dump
# from os import PathLike
# from typing import Type
#
# from pydantic import BaseModel, Field, PositiveInt
#
#
# class ProductDetail(BaseModel):
#     id: PositiveInt = Field(default=...)
#     name: str = Field(default=..., min_length=2, max_length=32)
#     price: Decimal = Field(default=..., max_digits=8, decimal_places=2)
#
#     @classmethod
#     def from_csv(cls, filename: str | bytes | PathLike, separator: str = ",") -> list["ProductDetail"]:
#         with open(file=filename, mode="rt", encoding="utf-8") as file:
#             keys = file.readline().strip().split(separator)
#             return [cls(**dict(zip(keys, line.strip().split(separator)))) for line in file]
#
#     @classmethod
#     def to_csv(cls, objs: list["ProductDetail"], filename: str | bytes | PathLike, separator: str = ",") -> None:
#         objs = [obj.model_dump() for obj in objs]
#         keys = separator.join(objs[0].keys())
#         values = [separator.join([f"{val}" for val in obj.values()]) for obj in objs]
#         values.insert(0, keys)
#         data = "\n".join(values)
#         with open(file=filename, mode="wt", encoding="utf-8") as file:
#             file.write(data)
#
#
# #  Написать класс JsonRepository
# #  Задача класса управлять данными в файле JSON
# #  В файле в ключе objects хранится список словарей с данными продукте (id, name, price)
# #  1. Метод класса get принимает id товара и возвращает экземпляр схемы с данными о товаре из json файла
# #  2. Метод класса insert принимает экземпляр схемы и записывает данные в json при условии, что там
# #  нет товара с таким id и/или названием
# #  3. Метод класса update принимает схемы, и заменяет данные в json на данные из схемы
# #  у объекта с указанным id, если в файле нет такого id то эти данные записываться не должны
# #  4. Метод класса delete принимает id и удаляет из файла при наличии такого товара
#
#
# class AbstractRepository(ABC):
#     SCHEMA: Type[BaseModel]
#
#     @classmethod
#     @abstractmethod
#     def get(cls, pk: int) -> BaseModel:
#         raise NotImplementedError
#
#     @classmethod
#     @abstractmethod
#     def insert(cls, obj: BaseModel) -> None:
#         raise NotImplementedError
#
#     @classmethod
#     @abstractmethod
#     def update(cls, obj: BaseModel) -> None:
#         raise NotImplementedError
#
#     @classmethod
#     @abstractmethod
#     def delete(cls, pk: int) -> None:
#         raise NotImplementedError
#
#
# class JSONRepository(AbstractRepository):
#     FILENAME: str
#     SCHEMA: Type[BaseModel]
#     JSON_SERIALIZER = dump
#     JSON_DESERIALIZER = load
#
#     @classmethod
#     def read(cls) -> dict:
#         with open(file=cls.FILENAME, mode="rt", encoding="utf-8") as file:
#             return cls.JSON_DESERIALIZER(file)
#
#     @classmethod
#     def write(cls, data: dict) -> None:
#         with open(file=cls.FILENAME, mode="wt", encoding="utf-8") as file:
#             cls.JSON_SERIALIZER(data, file, indent=2)
#
#     @classmethod
#     def get(cls, pk: int) -> BaseModel:
#         objects = cls.read().get("objects")
#         for obj in objects:
#             if obj.get("id") == pk:
#                 return cls.SCHEMA(**obj)
#
#     @classmethod
#     def is_exist(cls, obj: BaseModel) -> bool:
#         objects = cls.read().get("objects")
#         for i in objects:
#             if i.get("id") == obj.id:
#                 return True
#         else:
#             return False
#
#     @classmethod
#     def insert(cls, obj: BaseModel) -> None:
#         if cls.is_exist(obj=obj):
#             raise ValueError
#         data = cls.read()
#         data["objects"].append(obj.model_dump(mode="json"))
#         cls.write(data)
#
#     @classmethod
#     def update(cls, obj: BaseModel) -> None:
#         if not cls.is_exist(obj=obj):
#             raise ValueError
#         data = cls.read()
#         for i, val in enumerate(data.get("objects")):
#             if val.get("id") == obj.id:
#                 data["objects"][i] = obj.model_dump(mode="json")
#                 cls.write(data=data)
#                 break
#
#     @classmethod
#     def delete(cls, pk: int) -> None:
#         obj = cls.get(pk=pk)
#         if obj is not None:
#             data = cls.read()
#             for i, val in enumerate(data.get("objects")):
#                 if val.get("id") == obj.id:
#                     del data["objects"][i]
#                     cls.write(data=data)
#                     break
#
#
# class CSVRepository(AbstractRepository):
#
#     @classmethod
#     def get(cls, pk: int) -> BaseModel:
#         pass
#
#     @classmethod
#     def insert(cls, obj: BaseModel) -> None:
#         pass
#
#     @classmethod
#     def update(cls, obj: BaseModel) -> None:
#         pass
#
#     @classmethod
#     def delete(cls, pk: int) -> None:
#         pass
#
#
# class CategoryDetail(BaseModel):
#     id: PositiveInt
#     title: str
#
#
# class ProductRepository(JSONRepository):
#     SCHEMA = ProductDetail
#     FILENAME = "output.json"
#
#
# class CategoryRepository(JSONRepository):
#     SCHEMA = CategoryDetail
#     FILENAME = "categories.json"
#
#
# # from datetime import *
#
#
# # print(datetime.utcnow().strftime("%d %m %Y"))
# # delta = timedelta(weeks=2)
#
# # print(datetime.now() - (datetime.now() - delta))
#
#
# from pathlib import *
#
# BASE_DIR = Path(__file__).resolve().parent
# input_file = BASE_DIR / "input.txt"
# with input_file.open(mode="r", encoding="utf-8") as file:
#     print(file.read())


# import logging
#
# logging.basicConfig(
#     format="[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s",
#     datefmt="%d/%b/%Y %H:%M:%S",
#     level=logging.INFO, filename="log.log"
# )
#
#
# try:
#     age = int(input("Enter age: "))
# except ValueError:
#     logging.error("Пользователь тупица, не может ввести возраст")

# ACID
# A - atomicity
# C - consistency
# I - Isolation
# D - Durability

# CAP
# C - consistency
# A - availability
# P - partition tolerance


from sqlite3 import connect


conn = connect(database="db.sqlite3")
cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS categories (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(32) NOT NULL UNIQUE CHECK ( length(name) >= 2 ),
        is_published BOOLEAN NOT NULL DEFAULT (false)
    );
""")
conn.commit()
cur.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR (32) NOT NULL UNIQUE CHECK ( length(name) >= 2 ),
        price DECIMAL (8, 2) NOT NULL CHECK ( price > 0 ),
        category_id INTEGER NOT NULL,
        FOREIGN KEY ( category_id ) REFERENCES categories ( id ) ON DELETE RESTRICT
    );
""")
conn.commit()

# cur.execute("ALTER TABLE products ADD descr TEXT NOT NULL default '';")
# conn.commit()

cur.execute("CREATE INDEX category_id_index ON products ( category_id );")
conn.commit()
