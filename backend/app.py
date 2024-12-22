from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from pydantic import BaseModel
import os
# FastAPI instance
app = FastAPI()
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this to your frontend domain for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# MongoDB connection
client = MongoClient("mongodb://masteruser:securepassword123@localhost:27017/?directConnection=true&tls=true&tlsAllowInvalidHostnames=true&tlsCAFile=/home/pushpak/DevOps_Projects/todo-deployment/backend/global-bundle.pem&retryWrites=false")
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

