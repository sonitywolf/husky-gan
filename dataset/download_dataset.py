# Script to download all the images contained in husky_images.json

import urllib.request , json

os.makedirs(path, exist_ok=True) #create directory if it doesn't exists

with open('husky_images.json') as json_data:
    huskies = json.load(json_data)
    huskies_total = len(huskies)
    print(f"{huskies_total} loaded")

for index, husky in enumerate(huskies):
    print(f"Downloading {index}/{huskies_total}")
    try:
        urllib.request.urlretrieve(husky, f"img/{index}.jpg")
    except:
        print("\033[93mError!")