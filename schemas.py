from decimal import Decimal
from typing import *
from datetime import datetime
from http import HTTPMethod

from pydantic import BaseModel, Field, PositiveInt, field_validator, model_validator, validate_call, AfterValidator, \
    ConfigDict


class ProductDetail(BaseModel):
    id: PositiveInt
    title: str = Field(
        default=...,
        min_length=4,
        max_length=32
    )
    price: Decimal = Field(
        default=...,
        max_digits=8,
        decimal_places=2
    )


db = ["Coffee", "Tea", "Phones"]


class CategoryDetail(BaseModel):
    id: PositiveInt
    title: str = Field(
        default=...,
        min_length=4,
        max_length=32
    )
    products: list[ProductDetail] = Field(
        default=...,
        min_length=1
    )
    subcategories: Optional[list["CategoryDetail"]] = Field(default=None)

    @field_validator("title", mode="after")
    def title_validator(cls, value: str) -> str:
        if not value.isalnum():
            raise ValueError("incorrect category title")
        value = value.title()

        if value is db:
            raise ValueError("title must be unique")

        return value

    @model_validator(mode="after")
    def validator(self):
        if str(self.id) in self.title:
            raise ValueError
        return self


data = {
    "id": 5,
    "title": "coffee",
    "products": [
        {
            "id": 1,
            "title": "Latte",
            "price": 5
        }
    ],
    "subcategories": [
        {
            "id": 5,
            "title": "Coffee",
            "products": [
                {
                    "id": 1,
                    "title": "Latte",
                    "price": 5
                }
            ],
        }
    ]
}
cat = CategoryDetail(**data)
# print(cat.model_json_schema())
# print(cat.model_dump_json(indent=2))
# print(cat.title)


def is_alpha_str(v: str) -> str:
    if not v.isalpha():
        raise ValueError
    return v


AlphaStr = Annotated[str, AfterValidator(func=is_alpha_str)]
DigitStr = ""
PasswordStr = ""
ZipCodeStr = ""


class A(BaseModel):
    # name: AlphaStr = Field()
    model_config = ConfigDict()

    method: HTTPMethod
