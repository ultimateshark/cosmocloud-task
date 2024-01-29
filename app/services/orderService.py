from datetime import datetime
from app.repository.orderRespository import add_order
from app.repository.productRepository import retrieve_product,update_product

async def create_order(order_data):
    items = []
    to_update={}
    total_amount = 0
    for item in order_data.items:
        product = await retrieve_product(item.product_id)
        if product and product["quantity_available"] > item.quantity:
            to_update[item.product_id]={
                "product_name":product["product_name"],
                "price":product["price"],
                "quantity_available":product["quantity_available"] - item.quantity,
            }
            total_amount += product.get('price') * item.quantity
        items.append({"product_id":item.product_id,"quantity":item.quantity})
    created_order = await add_order({
        "total_amount":total_amount,
        "items":items,
        "createdOn":str(datetime.now()),
        "user_address":{
            "city":order_data.user_address.city,
            "country":order_data.user_address.country,
            "pincode":order_data.user_address.pincode
        }
    })
    for _k in to_update.keys():
        await update_product(_k,to_update[_k]) 
    return created_order