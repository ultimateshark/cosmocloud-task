from app.extentions import database
from typing import Optional
from pydantic import BaseModel, Field

product_collection = database.get_collection("products")

class ProductSchema(BaseModel):
    product_name: str = Field(...)
    price: float = Field(...)
    quantity_available: int = Field(...)
    class Config:
        schema_extra = {
            "example": {
                "product_name": "Macbook pro",
                "price": 115000,
                "quantity_available": 4
            }
        }

class UpdateProductModel(BaseModel):
    product_name: Optional[str]
    price: Optional[float]
    quantity_available: Optional[int]
    class Config:
        schema_extra = {
            "example": {
                "product_name": "Macbook pro",
                "price": 115000,
                "quantity_available": 4
            }
        }