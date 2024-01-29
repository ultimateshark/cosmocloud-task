from fastapi_class import View
from fastapi import APIRouter
from app.services.orderService import create_order
from app.models.orderModel import UpdateOrderModel

router = APIRouter()

@View(router=router,path="/order")
class MyView:
    async def post(self,order_data:UpdateOrderModel):
        order = await create_order(order_data)
        return order