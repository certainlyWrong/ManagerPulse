from fastapi import APIRouter
import httpx
import os

from managerpulse.core.models.client_model import ClientModel

client_router = APIRouter(prefix='/client', tags=['client'])
client_url = os.getenv(
    'CLIENT_SERVICE_URL'
) or 'http://localhost:3000/api/v1/client/'


@client_router.get('/')
async def find_all_clients():
    async with httpx.AsyncClient() as client:
        response = await client.get(client_url)
        return response.json()


@client_router.get('/{uid}/')
async def find_client_by_uid(uid: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(f'{client_url}{uid}/')
        return response.json()


@client_router.post('/')
async def create_client(body: ClientModel):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            client_url,
            content=body.model_dump_json(
                exclude_none=True,
                exclude_unset=True,
            )
        )
        return response.json()


@client_router.patch('/{uid}/')
async def update_client(uid: int, body: ClientModel):
    async with httpx.AsyncClient() as client:
        response = await client.patch(
            f'{client_url}{uid}/',
            content=body.model_dump_json(
                exclude_none=True,
                exclude_unset=True,
            )
        )
        return response.json()


@client_router.delete('/{uid}/')
async def delete_client(uid: int):
    async with httpx.AsyncClient() as client:
        response = await client.delete(f'{client_url}{uid}/')
        return response.json()
