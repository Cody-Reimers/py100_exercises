def factorial(integer):
    result = 1
    for number in range(2, integer + 1):
        result *= number
    return result

for number in range(1, 9):
    print(factorial(number))
print(factorial(25))