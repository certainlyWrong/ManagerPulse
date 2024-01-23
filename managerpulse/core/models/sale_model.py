from datetime import datetime

from typing import Optional
from pydantic import BaseModel, Field


class SaleModel(BaseModel):
    id_client: int
    id_product: int
    quantity: int
    date: Optional[datetime] = Field(default_factory=datetime.now)
