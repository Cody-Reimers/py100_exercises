print("My job is extracting the individual digits in a big integer!")
number = int(input("Can you give me an integer so I can practice? "))
result = []
temp = number
for i in range(len(str(number))):
    result.append(temp % 10)
    temp //= 10
result.reverse()
print("The number you gave me was: " + str(number) + "!")
print("The individual digits are: " + str(result))