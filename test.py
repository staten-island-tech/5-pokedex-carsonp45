import json
pokedex = open("./pokedex.json", encoding="utf8")
moves = open("./moves.json", encoding="utf8")
data = json.load(pokedex)
data_2 = json.load(moves)
""" language = input("Would you like to set your pokedex to english, japanese, chinese, or french>")
for index, item in enumerate(data):
    if language == "french":
        print(f"{index}: {item["name"]["french"]}")
    if language == "japanese":
        print(f"{index}: {item["name"]["japanese"]}")
    if language == "english":
        print(f"{index}: {item["name"]["english"]}")
    if language == "chinese":
        print(f"{index}: {item["name"]["chinese"]}") 
type = input("What type(s) would you like?")  
for index, item in enumerate(data):
      if type in item["type"]:
        print(f"{index}: {item["name"]["english"]}") """
pokemon = input("Which pokemon would you like?")
for index, item in enumerate(data):
    if pokemon in (f"{index}: {item["name"]["english"]}"):
        print(f"{index}: {item["name"]["english"]}")
        print(f"{index}: {item["type"]}")
for index, item in enumerate(data_2):
    if pokemon in item["type"]:
        print(f"{index}: {item["ename"]}")