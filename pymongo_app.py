import pymongo
import pprint
from pymongo import MongoClient

client = MongoClient(host="localhost", port=27017)

db = client.rptutorials
print(db)

tutorial = db.tutorial
print(tutorial)

tutorial_item_1 = {
     "title": "Working With JSON Data in Python",
     "author": "Lucas",
     "contributors": [
         "Aldren",
         "Dan",
         "Joanna"
     ],
     "url": "https://realpython.com/python-json/"
}

result = tutorial.insert_one(tutorial_item_1)
print(f"One tutorial: {result.inserted_id}")

tutorial2 = {
     "title": "Python's Requests Library (Guide)",
     "author": "Alex",
     "contributors": [
         "Aldren",
         "Brad",
         "Joanna"
     ],
     "url": "https://realpython.com/python-requests/"
}

tutorial3 = {
     "title": "Object-Oriented Programming (OOP) in Python 3",
     "author": "David",
     "contributors": [
         "Aldren",
         "Joanna",
         "Jacob"
     ],
     "url": "https://realpython.com/python3-object-oriented-programming/"
}

new_result = tutorial.insert_many([tutorial2, tutorial3])
print(f"Multiple tutorials: {new_result.inserted_ids}")


# retrieve documents from collection
for doc in tutorial.find():
    pprint.pprint(doc)

# query a document
jon_tutorial = tutorial.find_one({"author": "Alex"})
pprint.pprint(jon_tutorial)

client.close()
