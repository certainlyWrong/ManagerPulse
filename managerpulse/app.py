from .routes.v1.client_routes import client_router
from .routes.v1.product_routes import product_router

from fastapi import FastAPI

app = FastAPI(
    debug=True,
    title="Manager Pulse",
    description="Manager Pulse API",
)

app.include_router(client_router, prefix='/api/v1', tags=['v1'])
app.include_router(product_router, prefix='/api/v1', tags=['v1'])
