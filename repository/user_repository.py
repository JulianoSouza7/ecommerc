from xml.dom import NotFoundErr

from bson import ObjectId
from pymongo.errors import DuplicateKeyError

from repository.connection_mongo import insert_collection, find_collection, get_collection
from model.user import UserInDB
from wrapper.request.user import Login_user

__collection= "user"

def create_new_user(user:UserInDB):
   if find_user({'email': user.email}):
      raise Exception("Email ja existe")
   insert_collection(user.dict(),__collection)
   return {'status_code':201, 'mensagem': "Usuario criado com sucesso"}

def find_user(query):
   return get_collection(__collection).find_one(query,__collection)


def valid_user_db(user_request: Login_user):
   user = get_collection(__collection).find_one({'email':user_request.email})
   if user is None:
      raise NotFoundErr("Usuario nao encontrado")

   if user.get('password') != user_request.password:
      return {'status_code': 401 ,'mensagem':  "Senha incorreta" }

   return {'status_code': 201, 'mensagem': "Login com sucesso"}
