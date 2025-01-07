import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# easy level
password=""

for char in range(1,nr_letters+1):
     password +=random.choice(letters)

for char in range(1,nr_symbols+1):
     password +=random.choice(symbols)
     
for char in range(1,nr_numbers+1):
     password +=random.choice(numbers)

print(f"simple version of your password is :{password}\n")

#hard level
password_list=[]

for char in range(1,nr_letters+1):
     password_list.append(random.choice(letters))

for char in range(1,nr_symbols+1):
     password_list.append(random.choice(symbols))
     
for char in range(1,nr_numbers+1):
     password_list.append(random.choice(numbers))

numpass= ""
random.shuffle(password_list)
for char in password_list:
    numpass += char
print(f"Advanced version of your Password is:{numpass}\n")
     
     
    