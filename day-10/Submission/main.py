import json

name = input("Enter your name: ")
age = input("Enter your age: ")
favoriteFood = input("Enter your favorite food: ")


user = {
    "name": name,
    "age": age,
    "favorite_food": favoriteFood
}


data = json.dumps(user, indent=2)


with open("output.json", "w") as file:
    file.write(data)

