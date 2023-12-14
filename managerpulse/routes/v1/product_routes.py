from fastapi import APIRouter
import httpx
import os

from managerpulse.core.models.product_model import ProductModel

product_router = APIRouter(prefix='/product', tags=['product'])
product_url = os.getenv(
    'PRODUCT_SERVICE_URL'
) or 'http://localhost:8000/api/v1/product/'


@product_router.get('/')
async def find_all_products():
    async with httpx.AsyncClient() as client:
        response = await client.get(product_url)
        return response.json()


@product_router.get('/{uid}/')
async def find_product_by_uid(uid: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(f'{product_url}{uid}/')
        return response.json()


@product_router.post('/')
async def create_product(body: ProductModel):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            product_url,
            content=body.model_dump_json(
                exclude_none=True,
                exclude_unset=True,
            )
        )
        return response.json()


@product_router.patch('/{uid}/')
async def update_product(uid: int, body: ProductModel):
    async with httpx.AsyncClient() as client:
        response = await client.patch(
            f'{product_url}{uid}/',
            content=body.model_dump_json(
                exclude_none=True,
                exclude_unset=True,
            )
        )
        return response.json()


@product_router.delete('/{uid}/')
async def delete_product(uid: int):
    async with httpx.AsyncClient() as client:
        response = await client.delete(f'{product_url}{uid}/')
        return response.json()
