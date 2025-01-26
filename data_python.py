shop_fruits = {
    "apples": 2,
    "watermelons": 4,
    "bananas": 6
}

print(shop_fruits["watermelons"])
print(shop_fruits.get("watermelons"))

# print(shop_fruits["jcknc"])
print(shop_fruits.get("mczcsc"))


products = [
    {"id": 1, "name": "chocolate", "quantity": 5},
    {"id": 2, "name": "popcorn", "quantity": 10},
    {"id": 3, "name": "peanut butter", "quantity": 20}
]

print(products[1]['quantity'])
print(products[1]['name'])
print(products[2]["name"])


#set

clothes = {"t-shirt", "trousers", "skirt"}
is_present = "skirt" in clothes
print(is_present)

clothes.add("hat")
print(clothes)

clothes.remove("trousers")
print(clothes)

clothes.update(["suit"])
print(clothes)

#tuple
animals = ("lion" , "dog" , "cat")
print(animals[1])

#tuple with nested dictionaries
products = (
    {"id": 1, "name": "chocolate", "quantity": 5},
    {"id": 2, "name": "popcorn", "quantity": 10},
    {"id": 3, "name": "peanut butter", "quantity": 20}
)
print(products[2]["quantity"])


#ex 1:
#1. variable for checking if user is active or not
#Your favourite phrase from the book or film etc
# Number of people in the house
# How much the dinners cost




#ex2 Calculate area of triangle
areas = []
areas_dict = {"triangle": 0,"circle1": 0, "circle2": 0, "trapeze": 0}


b = 10
h = 6

area = 0.5 * b * h
print(area)
areas.append(area)
areas_dict["triangle"] = area


pi = 3.14
r = 10
area = pi * (r ** 2)
print (area)
areas.append(area)
areas_dict["circle1"] = area

a = 5
b = 12
h = 16

area = ((a+b)/2) * h 
print(area)
areas.append(area)
areas_dict["trapeze"] = area
print(areas)
print(areas_dict)