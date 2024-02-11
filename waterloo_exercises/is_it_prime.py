# Stores whether or not a number is prime, from 0 to 1,000,000
# And lets the user ask if a number is prime, or quit the program
def is_it_prime(n):
    for d in range(2, n+1):
        if not is_prime[d]:
            continue
        if (d * d > n):
            return True
        if n % d == 0:
            return False

is_prime = [False, False]
is_prime += [True] * 999999
for i in range(2, 1001):
    if is_prime[i] == False:
        continue
    is_prime[i] = is_it_prime(i)
    if is_prime[i] == True:
        for n in range(i * 2, len(is_prime), i):
            is_prime[n] = False

print("I know all prime numbers up to 1,000,000!")
while True:
    print("Would you like to know if a number is prime?")
    response = input("(Input q to quit or submit an integer)")
    if response == "q":
        print("Goodbye!")
        break
    elif is_prime[int(response)] == True:
        print("That is a prime number!")
    else:
        print("That is not a prime number.")