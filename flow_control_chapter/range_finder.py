def find_range(integer):
    if integer < 0:
        print(f"{integer} is less than 0")
    elif integer <= 50:
        print(f"{integer} is between 0 and 50")
    elif integer <= 100:
        print(f"{integer} is between 51 and 100")
    else:
        print(f"{integer} is greater than 100")

find_range(int(input("Give me an integer! ")))