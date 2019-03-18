from db import food_collection
from bson import ObjectId
# soluong = input (print("Ban muon nhap bao nhieu mon"))
# for i in soluong:
def add_food (name,price):
    new_food = {
        "name": name,
        "price": price,
    }
    food_collection.insert_one(new_food)
def get(query): #filter, limit, skip
    food_list = food_collection.find(query)
    return food_list

def get_by_id(id):
    f = food_collection.find_one ({ "_id" : ObjectId(id) })
    return f
    
def delete_by_id(id):
    d = food_collection.delete_one({ "_id":ObjectId(id) })
    return d
def update_by_id(id,name,price):
    query = { "_id" : ObjectId(id)}
    updater = { 
        "$set": {"price" : price},
        "$set": {"name" : name},

    }
    food_collection.find_one_and_update(query,updater)


if __name__ == "__main__":
    query = { "_id" : ObjectId('5c8a58499145aa22c47a0bc6')}
    updater = { "$set": {"price" : 24000},
                "$set": {"name" : "hi tieu"}  
    } #$inc, $dec, $set, $unset
    # food_collection.find_one_and_update(query,updater)
    food_collection.delete_one(query)
    print (*get({}), sep = "\n")
    
    # while True:
    #     n = input ("Enter name: ")
    #     p = input ("Enter pirce: ")

    #     add_food(n,p)
    # food_list = food_collection.find(
    #     {
    #         "price":{ "$gte":30000 , "$lt": 45000}
    #     }
    # )
    # for food in get( {"_id" : ObjectId("5c82350fac83390607465362") }):
    # food_collection.delete_one({"id" : ObjectId( "5c82350fac83390607465362") })
    # food_collection.delete_one({"id" : ObjectId("5c82350fac83390607465362") })
    # f = get_by_id("5c82350fac83390607465362")

    # if f != None:
    #     print (f)
    # else:
    #     print ("Not found")

