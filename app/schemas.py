from pydantic import BaseModel

class ProductBase(BaseModel):
    name: str
    price: float
    description: str | None = None

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id: int

    class Config:
        orm_mode = True

class OrderBase(BaseModel):
    product_id: int
    quantity: int

class OrderCreate(OrderBase):
    pass

class Order(OrderBase):
    id: int
    product: Product

    class Config:
        orm_mode = True
