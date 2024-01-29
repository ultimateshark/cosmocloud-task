
def productSerializer(product)-> dict:
    return {
        "product_id": str(product["_id"]),
        "product_name": product["product_name"],
        "price": product["price"],
        "quantity_available": product["quantity_available"]
    }