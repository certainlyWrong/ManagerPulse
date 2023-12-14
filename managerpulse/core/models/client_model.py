from typing import Optional
from pydantic import BaseModel, Field


class ClientModel(BaseModel):
    name: str
    phone: Optional[str] = Field(default=None)
    email: Optional[str] = Field(default=None)
    address: Optional[str] = Field(default=None)
    description: Optional[str] = Field(default=None)
