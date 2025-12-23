from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Literal, Optional, Type, TypeAlias, Annotated
from pydantic.types import conint

# =========================================================
# POST SCHEMAS
# =========================================================

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


class PostCreate(PostBase):
    pass


class PostUpdate(PostBase):
    pass


# =========================================================
# USER SCHEMAS
# =========================================================

class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserPublic(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        from_attributes = True


# =========================================================
# POST OUTPUT SCHEMAS
# =========================================================

class PostPublic(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserPublic

    class Config:
        from_attributes = True


class PostWithVotes(BaseModel):
    post: PostPublic
    votes: int

    class Config:
        from_attributes = True


# =========================================================
# AUTH SCHEMAS
# =========================================================

class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: Literal["bearer"]


class TokenData(BaseModel):
    user_id: Optional[int] = None


# =========================================================
# VOTE SCHEMA
# =========================================================

class VoteCreate(BaseModel):
    post_id: int
    dir: Annotated[int, conint(ge=0, le=1)]