from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.8aucclw.mongodb.net/pytech"
client = MongoClient(url)

db=client.pytech
students = db.students

student_list=students.find({})

print("\n -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

for doc in student_list:
    print(" Student ID: " + doc["student_id"] + "\n First Name: " + doc["first_name"] + "\n Last Name: " + doc["last_name"] + "\n")
    

result = students.update_one({"student_id": "1007"}, {"$set": {"last_name": "Smith"}})

thorin = students.find_one({"student_id": "1007"})

print(" Student ID: " + thorin["student_id"] + "\n First Name: " + thorin["first_name"] + "\n Last Name: " + thorin["last_name"] + "\n")


input("\n\n Press any key to continue...")

