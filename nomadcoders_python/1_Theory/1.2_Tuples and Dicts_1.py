# python sequence type(열거형 타입)
    # immutable sequence : (tuple), {dictionary}

days = ("Mon", "Tue", "Wed", "Thur", "Fri") # 변경 불가능
print(type(days))

nico = {
    "name":"Nico", "age":29, "korean":True, "fav_food": ["Kimchi", "Sashimi"]
}
print(type(nico))
print(nico["age"])
print(nico)
nico["handsome"] = True
print(nico)