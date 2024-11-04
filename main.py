from urllib.request import Request

import uvicorn
from fastapi import FastAPI
from pymongo.errors import DuplicateKeyError
from starlette.responses import JSONResponse

from model.user import UserInDB
from repository.user_repository import create_new_user, find_user, valid_user_db
from wrapper.request.user import Create_user, Login_user

app = FastAPI()


@app.exception_handlers(Exception)
async def duplicate_key_exception_handler(request: Request, exc: DuplicateKeyError):
    return JSONResponse(
        status_code=409,
        content={str(exc)}
    )


@app.put("/create_user")
def create_user(user: Create_user):
    user = UserInDB(**user.dict())
    return create_new_user(user)

@app.get("/valid_user")
def valid_user(user:Login_user):
    valid_user_db(user)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)