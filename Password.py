import random
import string

length = int(input("Enter password length: "))

characters = string.ascii_letters + string.digits  # a-z, A-Z, 0-9

password = ""

for i in range(length):
    password += random.choice(characters)

print("Generated Password:", password)
