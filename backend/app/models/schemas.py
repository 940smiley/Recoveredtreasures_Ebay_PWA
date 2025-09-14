from typing import Optional
from pydantic import BaseModel

class ImageOut(BaseModel):
    id: int
    file_path: str

class DraftOut(BaseModel):
    id: int
    item_id: int
    state: str
    title: Optional[str]
    description: Optional[str]
    category: Optional[str]
    price: Optional[float]
    image: Optional[ImageOut] = None

class DraftUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    category: Optional[str] = None
    price: Optional[float] = None
