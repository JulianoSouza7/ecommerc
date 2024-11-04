from fastapi import FastAPI
from pymongo import MongoClient
from pymongo.server_api import ServerApi

app = FastAPI()

def get_data_base():
    url = "mongodb+srv://ecommerc:ecommerc@ecom.f7nnw.mongodb.net/ecommerc?retryWrites=true&w=majority&appName=Ecom"
    client = MongoClient(url,server_api=ServerApi('1'))
    db = client["ecommerc"]
    return db

def get_collection(collection:str):
    db = get_data_base()
    return db[collection]



def insert_collection(obj , collection ):
   return get_collection(collection).insert_one(obj)

def find_collection(query, collection):
    return get_collection(collection).find(query)


