
def orderSerializer(order)-> dict:
    return {
        "order_id": str(order["_id"]),
        "total_amount": order["total_amount"],
        "items": order["items"],
        "createdOn": order["createdOn"],
        "user_address":order['user_address']
    }