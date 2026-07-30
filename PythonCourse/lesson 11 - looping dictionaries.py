book = {
    "title": "atomic habits",
    "author": "james clear",
    "year": 2018
}
#mini challenge 1
print("title:", book["title"])
print("author:", book["author"])
print("year:", book["year"])

#mini challenge 2
for key, value in book.items():
    print(key, ":", value)

#mini project

def profile():
    print("===== STUDENT PROFILE =====")


student = {
    "name": "ross",
    "age": 18,
    "course": "Electronics Technology",
    "dream job": "Cybersecurity Engineer"
}
profile()
for key, value in student.items():
    print(key, ":", value)

#teacher challenge
def menu():
    print("===================")
    print("_____USER INFO_____")
    print("> Name")
    print("> Age")
    print("> course")

user = {
    "name": "Ross",
    "age": 18,
    "course": "Electronics Technology"
}

menu()
user_input = input("What information do you want? ").lower().strip() 

while user_input not in user:
    user_input = input("invalid/non existent info! select again: ").lower().strip() 

if user_input in user:
    print(">",user[user_input])


#cyber profile
