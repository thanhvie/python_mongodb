from ast import Delete
from mongoengine import connect
from mongoengine import Document, ListField, StringField, URLField

connect(db="rptutorials", host="localhost", port=27017)

class Tutorial(Document):
     title = StringField(required=True, max_length=70)
     author = StringField(required=True, max_length=20)
     contributors = ListField(StringField(max_length=20))
     url = URLField(required=True)


tutorial_item_1 = Tutorial(
     title="Title 1",
     author="Martin",
     contributors=["Aldren", "Geir Arne", "Jaya", "Joanna", "Mike"],
     url="https://realpython.com/beautiful-soup-web-scraper-python/"
)

tutorial_item_1.save()  # Insert the new tutorial

tutorial_item_2 = Tutorial()
tutorial_item_2.title = "Title 2"
tutorial_item_2.author = "Alex"
tutorial_item_2.contributors = ["Aldren", "Jon", "Joanna"]
tutorial_item_2.url = "https://realpython.com/convert-python-string-to-int/"
tutorial_item_2.save()

# retrive all documents in collection
for doc in Tutorial.objects:
    print(doc.title)

# query a document
for doc in Tutorial.objects(author="Alex"):
    print(doc.title)

# delete all documents in collection
# for doc in Tutorial.objects:
#     doc.delete()
