from fastapi_class import View
from fastapi import APIRouter
from app.utils.exceptions import NOT_AUTHORIZED
from app.services.productService import get_all_products
from app.utils.helpers import responseFormatter

router = APIRouter()

@View(router=router,path="/product")
class MyView:
    exceptions = {
        "__all__": [NOT_AUTHORIZED]
    }

    async def get(self,offset:int = 0,limit:int = 10,min_price:float = 0,max_price:float=5000000000):
        products,page = await get_all_products(offset,limit,min_price,max_price)
        return responseFormatter(products,page)