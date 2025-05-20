from models import UserIn
from models import PermissionIn
from models import ClientIn
from models import WorkerIn

from app.api.users_service.db import worker,user,permission,client, database


async def add_worker(payload: WorkerIn):
    query = worker.insert().values(**payload.dict())

    return await database.execute(query=query)

async def get_worker(id):
    query = worker.select(worker.c.id==id)
    return await database.fetch_one(query=query)

async def add_client(payload: ClientIn):
    query = client.insert().values(**payload.dict())

    return await database.execute(query=query)

async def get_client(id):
    query = client.select(client.c.id==id)
    return await database.fetch_one(query=query)

async def add_permission(payload: PermissionIn):
    query = permission.insert().values(**payload.dict())

    return await database.execute(query=query)

async def get_permission(id):
    query = permission.select(permission.c.id==id)
    return await database.fetch_one(query=query)

async def add_user(payload: UserIn):
    query = user.insert().values(**payload.dict())

    return await database.execute(query=query)

async def get_user(id):
    query = user.select(permission.c.id==id)
    return await database.fetch_one(query=query)

