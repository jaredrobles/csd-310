from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.8aucclw.mongodb.net/pytech"
client = MongoClient(url)

db=client.pytech
students = db.students

student_list = students.find({})

print("\n -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

for doc in student_list:
    print(" Student ID: " + doc["student_id"] + "\n First Name: " + doc["first_name"] + "\n Last Name: " + doc["last_name"] + "\n")
    
thorin = students.find_one({"student_id": "1007"})
bilbo = students.find_one({"student_id": "1008"})
frodo = students.find_one({"student_id": "1009"})

input("\n\n End of program, press any key to continue...")


