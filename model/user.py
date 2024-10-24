from bson import ObjectId
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, Field, EmailStr
from typing import Optional


class UserInDB(BaseModel):
    id: Optional[ObjectId] = Field(None, alias="_id")
    username: str
    password : str
    email : EmailStr
    role : str = "basic"

    class Config:
        def to_json(self):
            return jsonable_encoder(self, exclude_none=True)

        def to_bson(self):
            data = self.__dict__
            if data["_id"] is None:
                data.pop("_id")
            return data