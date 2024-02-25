import textwrap
def remainders(numbers, divisor):
    return [number % divisor for number in numbers]

def divisible(numbers, divisor):
    moduluses = remainders(numbers, divisor)
    does_divide = []
    for number in moduluses:
        if number == 0:
            does_divide.append(True)
        else:
            does_divide.append(False)
    return does_divide

print(textwrap.dedent("""
    I can help you create a list of
    numbers and check if any of them
    are divisible by another number!
    """)
)

numbers = []
while True:
    if numbers == []:
        print("Let's start making a new list!")
    number = input("Enter a number or press \"e\" to end the list: ")
    if number == "e":
        divisor = input("What number should I try to divide these with? ")
        does_divide = divisible(numbers, int(divisor))
        print(f"The list you gave me evaluates to: {does_divide}")
        if any(does_divide):
            if all(does_divide):
                print("All of those were divisble!")
            else:
                print("At least one of those was divisible!")
        else:
            print("None of those were divisible.")
        if input("Are you done? Enter \"q\" to quit! ") == "q":
            print("Goodbye!")
            break
        else:
            print("Resetting...")
            numbers = []
            continue
    elif number >= "0" and number <= "9":
        numbers.append(int(number))
    else:
        print("Sorry, that doesn't look like a number.")