from repository.connection_mongo import db, insert_collection
from model.user import UserInDB

__collection= "user"

def create_new_user(user:UserInDB):
   return insert_collection(user,__collection)