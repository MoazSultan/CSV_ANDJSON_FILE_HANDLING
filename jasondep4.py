import jason_manager

file = open("student2.json", "r")

data = jason_manager.load(file)

print(data)
print(data["university"]["name"])

print(data["university"]["department"]["name"])

print(data["university"]["department"]["students"][0]["name"])
print(data["university"]["department"]["students"][1]["name"])


file.close()