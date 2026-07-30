tasks = [
    "study_python",
    "exercise",
    "read_book"
]
count = 0

def taskss():
       print("To Do Tasks")
       print("1. Study Python")
       print("2. Exercise")
       print("3. Read Book")

print("====================")
print()
taskss()
user = input("Which task did you finish?: ")
print()
print("====================")

if "study python" in user:
        print("Study python, Done!")
        tasks.remove("study_python")

elif "exercise" in user:
        print("Exercise, Done!")
        tasks.remove("exercise")

elif "read book" in user:
        print("Read book, Done!")
        tasks.remove("read_book")
else:
       print("Task Not Available!")

print("====================")
print("Your remaining tasks: ")
for single_tasks in tasks:
    count += 1
    print(count, tasks)
print("====================")