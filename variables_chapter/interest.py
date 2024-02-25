import textwrap
balance = float(input("How much money are you starting with? "))
interest = float(input("How much interest does your bank give? "))
time = float(input("How many years do you let it grow? "))
balance = int(balance * interest ** time * 100) / 100
print(f"Your new balance is {balance}")