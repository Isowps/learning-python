filess = open("cyber_notes.txt", "a")
filess.write("\nlinux")
filess.write("\nwireshark")
filess.close()

#eacher challenge

user_input = input("Write a note: ")

file = open("notetaking.txt", "w")
file.write(user_input)
file.close()

#project
user_input = input("Write a note: ")

file = open("notetaking.txt", "a")
file.write(user_input + "\n")
file.close()