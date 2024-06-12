import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# xài .choice() trong random
print("Welcome to PythonPassword Generator!")
amount_letters = int(input("How many letters would you like in your password?\n"))
amount_numbers = int(input("How many numbers would you like in your password?\n"))
amount_symbols = int(input("How many symbols would you like in your password?\n"))

password = []
for i in range(amount_letters):
    password += random.choice(letters)
for i in range(amount_numbers):
    password += random.choice(numbers)
for i in range(amount_symbols):
    password += random.choice(symbols)

# random.shuffel() : trộn thứ tự
random.shuffle(password)
pass_str = ""
for item in password:
    pass_str += item

print(f"Your password is: {pass_str}")