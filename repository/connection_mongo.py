from fastapi import FastAPI
from pymongo import MongoClient

app = FastAPI()

client = None
db = None

def get_data_base():
    client = MongoClient("mongodb+srv://ecommerc:ecommerc@ecom.f7nnw.mongodb.net/ecommerc?retryWrites=true&w=majority&appName=Ecom&ssl=false")
    db = client["ecommerc"]
    return db

def get_collection(collection:str):
    db = get_data_base()
    return db[collection]



def insert_collection(obj , collection ):
    get_collection(collection).insert_one(obj)

def find_collection(query, collection):
    get_collection(collection).find(query)


