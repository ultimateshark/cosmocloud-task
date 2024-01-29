from app.models.orderModel import order_collection
from app.serializers.orderSerializer import orderSerializer

async def add_order(order_data: dict) -> dict:
    order = await order_collection.insert_one(order_data)
    new_order = await order_collection.find_one({"_id": order.inserted_id})
    return orderSerializer(new_order)
