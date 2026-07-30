profile = {
    "name": "Ross",
    "dream": "Cybersecurity engineer",
    "language": "Python",
    "goal": "Build cybersecurity tools"
}

def menu():
    print("===================")
    print("> Name")
    print("> Dream")
    print("> Language")
    print("> Goal")
    print("===================")
    
def correct():
    print("===================")
    print("____INFORMATION____")
    print("===================")


menu()
user_input = input("Select Info: ").lower().strip()

while user_input not in profile:
    user_input = input("Invalid! Select Info Again: ").lower().strip()

if user_input in profile:
    correct()
    print(user_input, ":", profile[user_input])