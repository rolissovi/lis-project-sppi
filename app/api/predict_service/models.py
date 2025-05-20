from pydantic import BaseModel
from typing import List, Optional

class WorkerIn(BaseModel):
    permission_sk: int
    login: str
    password: str


class WorkerOut(WorkerIn):
    worker_sk: int


class WorkerUpdate(WorkerIn):
    permission_sk: Optional[int] = None
    login: Optional[str] = None
    password: Optional[str] = None



class ClientIn(BaseModel):
    permission_sk: int
    login: str
    password: str


class ClientOut(ClientIn):
    client_sk: int


class ClientUpdate(ClientIn):
    permission_sk: Optional[int] = None
    login: Optional[str] = None
    password: Optional[str] = None

class PermissionIn(BaseModel):
    description: str



class PermissionOut(PermissionIn):
    permission_sk: int


class PermissionUpdate(PermissionIn):
    description: Optional[str] = None

class UserIn(BaseModel):
    user_sk: int


class UserOut(UserIn):
    user_sk: int
