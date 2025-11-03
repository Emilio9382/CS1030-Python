
import random

letters = "abcdefghijklmnopqrstuvwxyz"

userChoice = input("How many letters do you want in your password: ")
numbers = input("how many passwords do you want: ")

for numberOfPassword in range (int(numbers)):
    wholePassword = ''
    for passwordLength in range (int(userChoice)): 
         wholePassword += random.choice(letters)
    print(wholePassword)
    
