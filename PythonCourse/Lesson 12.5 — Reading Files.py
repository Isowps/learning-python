#mini challenge 1
#already added tocino 
file = open("food.txt", "a")
file.write("\nadobo")
file.write("\nhotdog")
file.close()

#challenge 2
file = open("motivation.txt", "r")
contents = file.read()
print(contents)
file.close()