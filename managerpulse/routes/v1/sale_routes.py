
import httpx
from typing import List
from fastapi import APIRouter

from managerpulse.db_connection import mongo_db

from managerpulse.core.models.sale_model import SaleModel
from managerpulse.environment import Environment
sale_router = APIRouter(prefix='/sale', tags=['sale'])

client_url = Environment.get_instance.client_url
product_url = Environment.get_instance.product_url


async def verify_client_exists(id_client: int) -> bool:
    client_exists = False
    async with httpx.AsyncClient() as client:
        response = await client.get(f'{client_url}{id_client}/')
        if 'id' in response.json():
            client_exists = True
    return client_exists


async def verify_product_exists(id_product: int) -> bool:
    product_exists = False
    async with httpx.AsyncClient() as client:
        response = await client.get(f'{product_url}{id_product}/')
        if 'id' in response.json():
            product_exists = True
    return product_exists


# Retorna se o produto tem estoque suficiente para a venda
# se tiver, diminui o estoque;
async def decrease_stock(id_product: int, sale_quantity: int):
    async with httpx.AsyncClient() as client:
        response = await client.get(f'{product_url}{id_product}/')
        product = response.json()
        if product['quantity'] >= sale_quantity:
            product['quantity'] -= sale_quantity
            result = await client.patch(
                f'{product_url}{id_product}/',
                json=product
            )
            if result.status_code == 200:
                return True
        return False


@sale_router.get('/')
async def get_sales() -> List[SaleModel]:
    sales = mongo_db.db.get_collection('sale').find({})
    result = [SaleModel(**sale) for sale in sales]
    return result


@sale_router.post('/')
async def create_sale(sale: SaleModel) -> SaleModel | dict:
    client_exists = await verify_client_exists(sale.id_client)
    product_exists = await verify_product_exists(sale.id_product)
    if client_exists and product_exists:
        stock_available = await decrease_stock(
            sale.id_product,
            sale.quantity
        )
        if not stock_available:
            return {
                'error': 'Product out of stock'
            }
        mongo_db.db.get_collection('sale').insert_one(sale.model_dump())
        return sale
    return sale
