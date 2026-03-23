import json
pokedex = open("./pokedex.json", encoding="utf8")
data = json.load(pokedex)
""" print(data[0]) """

language = input("Would you like to set your pokedex to English, Japanese, Chinese, or French")
for index, item in enumerate(data):
    if language == "french":
        print(f"{index}: {item["name"]["french"]}")
    if language == "japanese":
        print(f"{index}: {item["name"]["japanese"]}")
    if language == "english":
        print(f"{index}: {item["name"]["english"]}")
    if language == "chinese":
        print(f"{index}: {item["name"]["chinese"]}")