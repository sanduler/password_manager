# Name: Ruben Sanduleac
# Date: 01/14//2022
# Description:

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

password = [letters, numbers, symbols]

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

total = ''
random.shuffle(letters)
random.shuffle(numbers)
random.shuffle(symbols)


# add a letter to the total based on the number the user entered
for letter in range(0, nr_letters):
    # determine the length of the list
    length = len(letters) - 1
    # generate a random number based on the amount of lower case and uppercase letters -1
    rand_number = random.randint(0, length)
    # pull a random letter from the list
    let = letters[rand_number]
    # increment the string
    total += let

# add a number to the total based on the number the user entered
for number in range(0, nr_numbers):
    # determine the length of the list
    length = len(numbers) - 1
    # generate a random number based on the amount of integers in the list -1
    rand_number = random.randint(0, length)
    # pull a random number from the list
    num = numbers[rand_number]
    # increment the string
    total += num

# add a symbol to the total based on the number the user entered
for symbol in range(0, nr_symbols):
    # determine the length of the list
    length = len(symbols) - 1
    # generate a random symbol based on the amount of symbols in the list -1
    rand_number = random.randint(0, length)
    # pull a random symbol from the list
    sym = symbols[rand_number]
    # increment the string
    total += sym

# create a new line
print("\n")

# shuffle the total string and print the password
print("You password is: " + ''.join(random.sample(total, len(total))))