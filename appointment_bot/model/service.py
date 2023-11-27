import uuid

from pydantic import (
    BaseModel,
    Field,
)


class Service(BaseModel):
    id: uuid.UUID = Field(alias='_id')
    title: str
    description: str
    price: float
