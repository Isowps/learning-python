tools = [
    "python",
    "git",
    "linux",
    "wireshark"
]
print(tools)

user = input("pop or remove: ")

if user == "remove":
    tools.remove("git")
    print(tools)
if user == "pop":
    tools.pop(2)
    print(tools)

#mini challenge 1
shopping = [
    "milk",
    "bread",
    "eggs"
]

shopping.remove("bread")
print(shopping)

#challenge 2
numbers = [1, 2, 3, 4]
numbers.pop()
print(numbers)

#challenge 3
games = [
    "minecraft",
    "valorant",
    "terraria"
]

games.remove("valorant")
if "valorant" not in games:
    print(games)


#task manager