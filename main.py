from fastapi import FastAPI
from app.api.users_service.users import client, worker, permission, user
from app.api.users_service.db import metadata, database, engine

metadata.create_all(engine)

app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

app.include_router(client, prefix='/api/users_service/v1/client', tags=['client'])
app.include_router(worker, prefix='/api/users_service/v1/worker', tags=['worker'])
app.include_router(permission, prefix='/api/users_service/v1/permission', tags=['permission'])
app.include_router(user, prefix='/api/users_service/v1/user', tags=['user'])