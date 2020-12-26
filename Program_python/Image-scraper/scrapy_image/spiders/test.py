import os
import csv

with open(
    os.path.join(os.path.dirname(__file__), "../resources/keywords.csv")
) as search_keywords:
    for keyword in csv.DictReader(search_keywords):
        search_text = keyword["keyword"]
        url = "https://www.alibaba.com/trade/search?fsb=y&IndexArea=product_en&CatId=&SearchText={0}&viewtype=G".format(
            search_text
        )
        print(url)
