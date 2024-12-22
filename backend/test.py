import pymongo
import sys

##Create a MongoDB client, open a connection to Amazon DocumentDB as a replica set and specify the read preference as secondary preferred
client = pymongo.MongoClient("mongodb://masteruser:securepassword123@localhost:27017/?directConnection=true&tls=true&tlsAllowInvalidHostnames=true&tlsCAFile=/home/pushpak/DevOps_Projects/todo-deployment/backend/global-bundle.pem&retryWrites=false") 

##Specify the database to be used
db = client.sample_database

##Specify the collection to be used
col = db.sample_collection

##Insert a single document
col.insert_one({'hello':'Amazon DocumentDB'})

##Find the document that was previously written
x = col.find_one({'hello':'Amazon DocumentDB'})

##Print the result to the screen
print(x)

##Close the connection
client.close()