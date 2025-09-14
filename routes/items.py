from fastapi import APIRouter
from typing import List
import schemas

router = APIRouter(prefix="/items", tags=["items"])

# In-memory storage (mock up)
items: list[schemas.Item] = []

@router.get("/", response_model=List[schemas.Item])
def get_items():
    return items