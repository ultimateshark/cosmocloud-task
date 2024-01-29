from app.extentions import database
from typing import Optional
from pydantic import BaseModel, Field

order_collection = database.get_collection("orders")

class ItemModel(BaseModel):
    product_id:str
    quantity:int

class AddressModel(BaseModel):
    city:str
    country:str
    pincode:int


class UpdateOrderModel(BaseModel):
    items: list[ItemModel]
    user_address:AddressModel


