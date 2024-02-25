def multiply(a, b):
    return a * b

def get_number(prompt):
    return float(input(prompt))

input1 = get_number("Enter the first number: ")
input2 = get_number("Enter the second number: ")
print(f"{input1} + {input2} = {multiply(input1, input2)}")