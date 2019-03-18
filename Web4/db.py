from pymongo import MongoClient
uri = "mongodb+srv://admin:admin1@tk-c4e-zz290.mongodb.net/test?retryWrites=true"

# 1.connect
client = MongoClient (uri)

# 2.Get database
db = client.test

# 3.collection
food_collection = db["food"]
user = db["user"]
# #4. Create a new document
# new_food = {
#     "name" : "Bun cha",
#     "price" : 30000,
# }#document
new_food = {
    "name" : "com rang",
    "price" : "30000"
}
new_user ={
    "user": "thaovit.2312@gmail.com",
    "password": "Phamthaothanh.2312"
}

# #5. Insert new document into collection
# food_collection.insert_one(new_food)
user.insert_one(new_user)

#6. Close connection
def close ():
    client.close()