from pydantic import BaseModel, EmailStr

# ----------------------------
# Item Schemas
# ----------------------------
class ItemBase(BaseModel):
    name: str
    price: float

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int
    class Config:
        orm_mode = True


# ----------------------------
# User Schemas
# ----------------------------
class UserBase(BaseModel):
    name: str
    email: EmailStr

class UserCreate(UserBase):
    pass 

class UserUpdate(BaseModel):
    name: str | None = None
    email: EmailStr | None = None

class User(UserBase):
    id: int
    class Config:
        orm_mode = True
