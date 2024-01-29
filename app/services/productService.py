from app.repository.productRepository import retrieve_products,get_total_count

async def get_all_products(offset,limit,min_price,max_price):
    products =  await retrieve_products(offset,limit,min_price,max_price)
    total = await get_total_count(min_price,max_price)
    page = {
        "nextOffset": min(offset + limit,(total//limit) * 10 if limit else 0),
        "prevOffset":max(offset - limit, 0),
        "limit":limit,
        "total":total
    }
    return products,page