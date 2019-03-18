from pymongo import MongoClient
uri = "mongodb+srv://thaovit98:phamthaothanh2312@cluster0-xodo5.mongodb.net/test?retryWrites=true"

# 1.connect
client = MongoClient (uri)

# 2.Get database
db = client.hello

# 3.collection
food_collection = db["food"]

#4. Create a new document
new_food = {
    "name" : "com",
    "price" : 50000,
}#document

#5. Insert new document into collection
food_collection.insert_one(new_food)

#6. Close connection
print (new_food)
def close ():
    client.close()