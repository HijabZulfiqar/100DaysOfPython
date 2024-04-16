import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i,', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['+', '-', '_', '!', '@', '$', '#', '%', '^', '&', '*', '(', ')', '=']
print("Welcome to the PyPassword Generator")
letters_in = int(input("How many letters would you like in your password?"))
numbers_in = int(input("How many numbers would you like in your password?"))
symbols_in = int(input("How many symbols would you like in your password?"))
password = ""
for i in range(1, letters_in + 1):
    password += random.choice(letters)
for i in range(1, numbers_in + 1):
    password += random.choice(numbers)
for i in range(1, symbols_in + 1):
    password += random.choice(symbols)
print(password)
# Hard Level
password_list = []
for i in range(1, letters_in + 1):
    password_list.append(random.choice(letters))
for i in range(1, numbers_in + 1):
    password_list.append(random.choice(numbers))
for i in range(1, symbols_in + 1):
    password_list.append(random.choice(symbols))
    print(password_list)
random.shuffle(password_list)
print(password_list)
final_password = ""
for password in password_list:
    final_password +=password
print(final_password)


