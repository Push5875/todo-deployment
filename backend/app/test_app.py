# import mongomock
# from fastapi.testclient import TestClient
# from app.app import app, Item

# # Mock MongoDB collection with mongomock
# @app.on_event("startup")
# def startup_db():
#     app.mongodb_client = mongomock.MongoClient()
#     app.db = app.mongodb_client["my_database"]
#     app.collection = app.db["item"]

# client = TestClient(app)

# def test_create_item():
#     new_item = {"name": "item3", "description": "description3", "price": 30.0}
#     response = client.post("/items/", json=new_item)
#     assert response.status_code == 200
#     assert response.json() == {"message": "Item added successfully!"}
    
# def test_list_items():
#     # Insert mock data
#     app.collection.insert_one({"name": "item1", "description": "description1", "price": 10.0})
#     app.collection.insert_one({"name": "item2", "description": "description2", "price": 20.0})

#     response = client.get("/items/")
#     assert response.status_code == 200
#     assert len(response.json()["items"]) == 2
