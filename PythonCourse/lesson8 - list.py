language = ["Python", "java", "C++", "ross"]


print(language[0])
print(language[1])
print(language[2])
print(language[3])

language.append("yin")#adds to the list
print(language[4])
print(language)

#mini challenge
tools = ["VS code", "Python", "Git"]
print(tools)
#challenge 2
print(tools[1])
#challenge 3
tools.append("Linux")
print(tools[3])

number = [10,20,30]
print(number[0])

#mini project

tools = [
    "Laptop",
    "Keyboard",
    "Mouse"
]
print("My Inventoryt:")
print()
print("1.",tools[0])
print("2.",tools[1])
print("3.",tools[2])

#teacher challenge
dreams = [
    "cybersecurity",
    "Built my own tools",
    "Graduate college"
]

print("my dreams:")
print("1.",dreams[0])
print("2.",dreams[1])
print("3.",dreams[2])

#loops + lists
languages = ["Python", "java", "C++", "ross"]

for languageses in languages:
    print(languageses)

#print everything

#mini challenge1
tools = [
    "Laptop",
    "Keyboard",
    "Mouse"
]

for item in tools:
    print(item)

#challenge 2
dreams = [
    "cybersecurity",
    "Built my own tools",
    "Graduate college"
]
for wish in dreams:
    print("dream:")
    print(wish)

#mini challenge 1
print(len(tools))

#challlenge 2
counts = 1

for item in tools:
    print(counts, item)
    counts += 1

#challenge 3
conts = 1
for wish in dreams:
    print(conts,".",wish)
    conts += 1

#searching the lists
#mini challenge 1
languags = [
    "Python", 
    "java", 
    "C++"
]

if "Python" in languags:
    print("Python Found!")
else:
    print("Python Missing!")
#challenge 2
if "rust" in languags:
    print("Rust Found!")
else:
    print("Rust Missing!")

#mini project
tools = [
    "Python",
    "Git",
    "Linux",
    "Wireshark"
]

tool = input("Enter Tool: ").lower()
if tool in tools:
    print("Tool is Available!")
else:
    print("Tool is Not Available!")

#july 21, 2026 5:22pm 