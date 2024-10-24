import uvicorn
from fastapi import FastAPI

from model.user import UserInDB
from repository.user_repository import create_new_user
from wrapper.request.user import Create_user

app = FastAPI()


@app.put("/create_user")
def create_user(user: Create_user):
    return create_new_user(UserInDB(**user.model_dump()))



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)