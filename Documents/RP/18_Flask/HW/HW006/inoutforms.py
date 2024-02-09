from pydantic import BaseModel
from datetime import datetime


class UserCreate(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str


class UserRead(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str


class ProductCreate(BaseModel):
    name: str
    description: str
    price: float


class ProductRead(BaseModel):
    id: int
    name: str
    description: str
    price: float


class OrderCreate(BaseModel):
    user_id: int
    product_id: int
    status: str


class OrderRead(BaseModel):
    id: int
    user_id: int
    product_id: int
    order_date: datetime
    status: str