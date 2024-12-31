from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from pydantic import BaseModel
import os
from fastapi.middleware.cors import CORSMiddleware
# FastAPI instance
app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this to your frontend domain for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# MongoDB connection

# Get the directory of the current file (app.py)
current_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the path to the global-bundle.pem file
pem_file_path = os.path.join(current_dir, 'global-bundle.pem')
# mongo_uri = os.getenv("MONGO_URI")
# print(mongo_uri)
client = MongoClient(f"mongodb://masteruser:securepassword123@docdb-instance-1.cxqkqmmkq3qy.us-east-1.docdb.amazonaws.com:27017/my_database?tls=true&tlsCAFile={pem_file_path}&authMechanism=SCRAM-SHA-1&retryWrites=false")
db = client["my_database"]
collection = db["item"]

# Data model
class Item(BaseModel):
    name: str
    description: str
    price: float

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI DocumentDB demo!"}

@app.post("/items/")
def create_item(item: Item):
    item_dict = item.dict()
    collection.insert_one(item_dict)
    return {"message": "Item added successfully!"}

@app.get("/items/")
def list_items():
    items = list(collection.find({}, {"_id": 0}))
    return {"items": items}

@app.delete("/items/{name}")
def delete_item(name: str):
    result = collection.delete_one({"name": name})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": f"Item '{name}' deleted successfully"}