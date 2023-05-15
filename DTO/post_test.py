from pydantic import BaseModel


class PostTestRequestDTO(BaseModel):
    name: str
