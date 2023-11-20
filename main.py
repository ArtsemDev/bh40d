# # from psycopg2.extras import NamedTupleCursor, NamedTupleConnection
# # from fastapi import FastAPI
#
# # app = FastAPI()
# # conn = NamedTupleConnection(dsn="postgresql://admin:admin@0.0.0.0:5432/admin")
#
#
# # @app.on_event("shutdown")
# # async def on_shutdown():
# #     print("Connection close")
# #     conn.close()
#
#
# # def main():
# #     with conn.cursor() as cur:  # type: NamedTupleCursor
# #         cur.execute("select * from shops;")
# #         for shop in cur.fetchall():
# #             print(shop.id, shop.address)
#
# from pydantic import BaseModel
#
#
# class Message(BaseModel):
#     text: str
#
#
# class Update(BaseModel):
#     event: Message
#
#
# def depends(func):
#     def wrapper(update: Update):
#         kwargs = {}
#         for k, v in func.__annotations__.items():
#             for k2, v2 in update.__dict__.items():
#                 if isinstance(v2, v):
#                     kwargs[k] = v2
#         return func(**kwargs)
#     return wrapper
#
#
# def validator(func):
#
#     def wrapper(*args, **kwargs):
#         for k, v in kwargs.items():
#             if k in func.__annotations__:
#                 if not isinstance(v, func.__annotations__.get(k)):
#                     raise TypeError
#         return func(**kwargs)
#     return wrapper
#
#
# @validator
# def bar(a: int, b: int, c: int):
#     pass
#
#
# print()
