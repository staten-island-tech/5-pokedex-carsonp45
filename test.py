import json
pokedex = open("./pokedex.json", encoding="utf8")
data = json.load(pokedex)
""" print(data[]) """
for index, item in enumerate(data):
    print(index, ":", item["name"])
language = (input("English, Japanese, Chinese, or French"))
if language == "French":
    print(f"{index}: {item["name"]["French"]}")