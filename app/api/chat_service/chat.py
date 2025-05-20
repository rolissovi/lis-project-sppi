from fastapi import APIRouter, HTTPException

from app.api.users_service import db_manager
from app.api.users_service.models import UserIn, UserOut
from app.api.users_service.models import ClientIn, ClientOut
from app.api.users_service.models import PermissionIn, PermissionOut
from app.api.users_service.models import WorkerIn, WorkerOut

client = APIRouter()

@client.post('/', response_model=ClientOut, status_code=201)
async def create_cast(payload: ClientIn):
    client_id = await db_manager.add_client(payload)

    response = {
        'id': client_id,
        **payload.dict()
    }

    return response

@client.get('/{id}/', response_model=ClientOut)
async def get_cast(id: int):
    client = await db_manager.get_client(id)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    return client

worker = APIRouter()

@worker.post('/', response_model=WorkerOut, status_code=201)
async def create_cast(payload: WorkerIn):
    worker_id = await db_manager.add_worker(payload)

    response = {
        'id': worker_id,
        **payload.dict()
    }

    return response

@worker.get('/{id}/', response_model=WorkerOut)
async def get_cast(id: int):
    worker = await db_manager.get_worker(id)
    if not worker:
        raise HTTPException(status_code=404, detail="Worker not found")
    return worker

permission = APIRouter()

@permission.post('/', response_model=PermissionOut, status_code=201)
async def create_cast(payload: PermissionIn):
    permission_id = await db_manager.add_permission(payload)

    response = {
        'id': permission_id,
        **payload.dict()
    }

    return response

@permission.get('/{id}/', response_model=PermissionOut)
async def get_cast(id: int):
    permission = await db_manager.get_permission(id)
    if not permission:
        raise HTTPException(status_code=404, detail="Permission not found")
    return permission

user = APIRouter()

@user.post('/', response_model=UserOut, status_code=201)
async def create_cast(payload: UserIn):
    user_id = await db_manager.add_user(payload)

    response = {
        'id': user_id,
        **payload.dict()
    }

    return response

@user.get('/{id}/', response_model=UserOut)
async def get_cast(id: int):
    user = await db_manager.get_user(id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user