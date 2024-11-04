from bson import ObjectId
from pydantic import BaseModel, EmailStr


class UserInDB(BaseModel):
    _id: str = str(ObjectId())
    username: str
    password : str
    email : EmailStr
    role : str = "basic"

    # class Config:
    #     def to_json(self):
    #         return jsonable_encoder(self, exclude_none=True)

        # def to_bson(self):
        #     data = self.__dict__
        #     if data["_id"] is None:
        #         data.pop("_id")
        #     return data