import string
import random

def generatePassword(minimumLength, numbers = True, specialCharacters = True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if specialCharacters:
        characters += special

    password = ""
    meetsCriteria = False
    hasNumber = False
    hasSpecial = False

    while not meetsCriteria or len(password) < minimumLength:
        newChar = random.choice(characters)
        password += newChar

        if newChar in digits:
            hasNumber = True
        elif newChar in special:
            hasSpecial = True

        meetsCriteria = True
        if numbers:
            meetsCriteria = hasNumber
        if specialCharacters:
            meetsCriteria = meetsCriteria and hasSpecial

    return password

minimumLength = int(input("Enter the minimum legth: "))
hasNumber = input("Do you want to have numbers? (yes / no) ").lower() == "yes"
hasSpecial = input("Do you want to have special characters? (yes / no) ").lower() == "yes"
password = generatePassword(minimumLength, hasNumber, hasSpecial)
print("The generated password is:", password)