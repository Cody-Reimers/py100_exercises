my_list = [
    1, 3, 6, 11,
    4, 2, 4, 9,
    17, 16, 0,
]
parities = []
for number in my_list:
    if number % 2 == 0:
        parities.append("Even")
    else:
        parities.append("Odd")

print(parities)