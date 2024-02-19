import json

name = input("Enter your name: ")
age = input("Enter your age: ")
favorite_food = input("Enter your favorite food: ")


user_info = {
    "name": name,
    "age": age,
    "favorite_food": favorite_food
}


json_data = json.dumps(user_info, indent=2)


with open("output.json", "w") as file:
    file.write(json_data)

