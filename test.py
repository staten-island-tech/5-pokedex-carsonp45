import json
pokedex = open("./pokedex.json", encoding="utf8")
data = json.load(pokedex)
 
language = input("Would you like to set your pokedex to english, japanese, chinese, or french>")
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
      if type in item['type']:
        print(f"{index}: {item['name']['english']}")
"""   if type == "Fire":
        print(f"{index}: {item["type"]["Fire"]}")
    elif type == "Water":
        print(f"{index}: {item["name"]["type"]["Water"]}")
    elif type == "Grass":
        print(f"{index}: {item["name"]["type"]["Grass"]}")
    elif type == "Flying":
        print(f"{index}: {item["name"]["type"]["Flying"]}")
    elif type == "Rock":
        print(f"{index}: {item["name"]["type"]["Rock"]}")   
    elif type == "Fairy":
        print(f"{index}: {item["name"]["type"]["Fairy"]}") 
 """