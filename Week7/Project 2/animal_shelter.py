#Abdulrahman Al-Nachar

from pymongo import MongoClient
from bson.objectid import ObjectId


class AnimalShelter(object):
    #CRUD operations in MongoDB

    def __init__(self):
        USER = 'aacuser'
        PASS = 'SNHU1234'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 31393
        DB = 'AAC'
        COL = 'animals'

        # connect to MongoDB
        self.client = MongoClient('mongodb://%s:%s@%s:%d/AAC?authSource=AAC' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]
    # create function
    def create(self, data):
        if data is not None:
            try:
                # this creates it into the animals collection
                self.database.animals.insert_one(data)  # data should be a dictionary
                return True
            except Exception as e:
                # print the error
                print(f"error: {e}")
                return False
            else:
                # displays a message when the data is empty
                raise Exception("the data is empty")


    # read
    def read(self, searchData):
        
        try:
            # this is used to filter the query
            if searchData:
                # If search criteria is given, use it to filter the results
                data = self.collection.find(searchData, {"_id": False})
            else:
                # If no search criteria is given, return all the documents
                data = self.collection.find({}, {"_id": False})
            return list(data)
        except Exception as e:
            # Just like in create(), this helps catch and show any error that happens
            print(f"error: {e}")
            return []
        

    # update function
    def update(self, query, new_values):
        if query is not None and new_values is not None:
            try:
                # this updates all documents matching the query
                result = self.collection.update_many(query, {"$set": new_values})
                return result.modified_count  # returns how many documents were updated
            except Exception as e:
                print(f"error: {e}")
                return 0
        else:
            raise Exception("query or new_values parameter is empty")

    # delete function
    def delete(self, query):
        if query is not None:
            try:
                # this deletes all documents matching the query
                result = self.collection.delete_many(query)
                return result.deleted_count  # returns how many documents were deleted
            except Exception as e:
                print(f"error: {e}")
                return 0
        else:
            raise Exception("query parameter is empty")

    