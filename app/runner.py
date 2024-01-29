from fastapi import FastAPI
from app.controllers.productController import router as ProductRouter
from app.controllers.orderController import router as OrderRouter
from fastapi.middleware.cors import CORSMiddleware
from config.cors import origins
def create_app():
    app = FastAPI()
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )
    app.include_router(ProductRouter)
    app.include_router(OrderRouter)
    return app