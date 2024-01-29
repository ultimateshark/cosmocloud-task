from bson.objectid import ObjectId
from app.models.productModel import product_collection
from app.serializers.productSerializer import productSerializer


async def retrieve_products(offset,limit,min_price,max_price):
    products = []
    async for product in product_collection.find(
        {
            "price": {"$gte": min_price, "$lte": max_price}
        }
    ).skip(offset).limit(limit):
        products.append(productSerializer(product))
    return products

async def retrieve_product(id: str) -> dict:
    product = await product_collection.find_one({"_id": ObjectId(id)})
    if product:
        return product
    
async def update_product(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    product = await product_collection.find_one({"_id": ObjectId(id)})
    if product:
        updated_product = await product_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_product:
            return True
        return False

async def get_total_count(min_price,max_price):
    return  await product_collection.count_documents({"price": {"$gte": min_price, "$lte": max_price}})