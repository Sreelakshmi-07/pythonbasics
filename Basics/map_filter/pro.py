products=[
    {"pid":100,"p_name":"samsungA52","band":"5g","price":30000,"display":"amoled"},
    {"pid": 101, "p_name": "samsungf41", "band": "4g", "price": 15000, "display": "amoled"},
    {"pid":102,"p_name":"mi10promax","band":"4g","price":19000,"display":"amoled"},
    {"pid": 103, "p_name": "mi11lite", "band": "5g", "price": 22000, "display": "led"},
    {"pid":104,"p_name":"iphone12pro","band":"5g","price":80000,"display":"amoled"},
    {"pid": 105, "p_name": "realme", "band": "4g", "price": 12000, "display": "led"},

]
print(len(products))
print()
mob_names=list(map(lambda item:item["p_name"],products ))
print(mob_names)
print()
amoled = list(filter(lambda p:p["display"]=="amoled",products))
print(amoled)
print()
g = list(filter(lambda band:band["band"]=="5g",products))
print(g)
print(list(map(lambda p:p["p_name"],g)))
print()
products.sort(key=lambda p:p["price"],reverse=True)
print(products)
print()
print(max(products,key=lambda pro:pro["price"]))
print()
print(min(products,key=lambda pro:pro["price"]))
