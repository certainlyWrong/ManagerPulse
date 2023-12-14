from datetime import datetime

from typing import Optional
from pydantic import BaseModel, Field


class ProductModel(BaseModel):
    name: str
    price: float = Field(default=0.0)
    quantity: int = Field(default=0)
    description: Optional[str] = Field(default=None)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: Optional[datetime] = Field(default=None)
