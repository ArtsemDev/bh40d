# from psycopg2.extras import NamedTupleCursor, NamedTupleConnection
# from fastapi import FastAPI


# app = FastAPI()
# conn = NamedTupleConnection(dsn="postgresql://admin:admin@0.0.0.0:5432/admin")


# @app.on_event("shutdown")
# async def on_shutdown():
#     print("Connection close")
#     conn.close()


# def main():
#     with conn.cursor() as cur:  # type: NamedTupleCursor
#         cur.execute("select * from shops;")
#         for shop in cur.fetchall():
#             print(shop.id, shop.address)
