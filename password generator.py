import random
import string
print(" ===== Password Generator===== ")
length = int(input("How many characters do you want in your password? "))
characters = string.ascii_letters + string.digits + string.punctuation
password=""
for i in range(length):
    password += random. choice(characters)
print("Your generated password is:",password);
print(" --- Keep your pass word safe --- ")
