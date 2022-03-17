#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password? (max 51)\n")) 
nr_symbols = int(input(f"How many symbols would you like? (max 9)\n"))
nr_numbers = int(input(f"How many numbers would you like? (max 10)\n"))

# 52 letters
# 10 numbers
# 9 symbols
password = ""
if 1 <= nr_letters <= 52:
	for char in range (1, nr_letters + 1):
		password += random.choice(letters)
	
if 1 <= nr_symbols <= 9:
	for symb in range (1, nr_symbols + 1):
		password += random.choice(symbols)

if 1 <= nr_numbers <= 10:
	for num in range (1, nr_numbers + 1):
		password += random.choice(numbers)
		
else:
	print("Pick between 52 letters, 9 symbols and 10 numbers")

password = list(password) # have to make list from str before shuffle
random.shuffle(password) # shuffle characters 
result = "".join(password) # make string from shuffled list again
print("Your random password is: " + result)
	
		
		
