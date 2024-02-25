pets = {
    "Cat": "Meow",
    "Dog": "Bark",
    "Bird": "Tweet",
}

print(pets["Dog"])
print(pets.get("Lizard"))
pets["Lizard"] = "<silence>"
print(pets["Lizard"])