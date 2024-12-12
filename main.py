meme_dict = {
            "CRINGE": "Что-то очень странное или стыдное",
            "LOL": "Что-то очень смешнo",
            "ROFL": 'A JOKE',
            "SHISH": "APPROVAL",
            "KRIPOVIY": "SCARY, TERRYFYING",
            "AGRITSA": "TO BE ANGRY OR AGGRESSIVE",
            "CHILL GUY": "RELAXED PERSON"
            }
while True:
    word = input("Введите непонятное слово (большими буквами!): ")
    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print("There is no such word in the dictionary")
