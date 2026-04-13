import json
pokedex = open("./pokedex.json", encoding="utf8")
data = json.load(pokedex)
""" print(data[0]) """ 

""" language = input("Would you like to set your pokedex to english, japanese, chinese, or french>")
for index, item in enumerate(data):
    if language == "french":
        print(f"{index}: {item["name"]["french"]}")
    if language == "japanese":
        print(f"{index}: {item["name"]["japanese"]}")
    if language == "english":
        print(f"{index}: {item["name"]["english"]}")
    if language == "chinese":
        print(f"{index}: {item["name"]["chinese"]}")" """
type = input("What type(s) would you like?") 
for index, item in enumerate(data):
    if type == "fire":
        print(f"{index}: {item["name"]["fire"]}")
    elif type == "water":
        print(f"{index}: {item["name"]["type"]["water"]}")
    elif type == "grass":
        print(f"{index}: {item["name"]["type"]["grass"]}")
    elif type == "flying":
        print(f"{index}: {item["name"]["type"]["flying"]}")
    elif type == "rock":
        print(f"{index}: {item["name"]["type"]["rock"]}")   
