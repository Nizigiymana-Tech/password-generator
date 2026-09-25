# Imports Here
import random

# Variables

characters = "abcdefghijklmaopqrstuvwxynz123456789!@#$%^&*~"
main_password = {}

# Functions

# ----------------------------------------

# generate random password using a for-Loop
def generate_password():
    password = ""

    for char in range(1, random.randint(8, 12)):
        password += characters[random.randint(0, len(characters) - 1)]

    return password

# reset password
def reset_password():
    Name = input("What is your password name? ")
    if not Name or Name.isalnum() or not main_password[Name]:
        print("Not avaliable")
        return
    
    main_password[Name] = None

# print all passwords
def show_passwords():
    for name, password in main_password.items():
        print(f"{name}: {password}")

# ----------------------------------------

# Main Code
while True:
    if len(main_password) > 0:
        bool = input("Do you want to quit? (Y/N) ")

        if bool == "Y":
            break
    else:
        print("🔒 Welcome to Password Generator 🔒")

    print("All Passwords")
    show_passwords()
    Bool2 = input("Do you want to reset one of your passwords? ").lower().strip()

    if Bool2 == "y" or Bool2 == "yes":
        reset_password()

    websiteName = input("What website is the password for? ")

    randomPassword = generate_password()
    print(f"You're password is {randomPassword}")

    choice = input("Do you want this as your password, or do you want a different one? (Y/N) ").lower().strip()
    if choice == "y" or choice == "yes":
        main_password[websiteName] = randomPassword
        print("Success! Do you want to add another one")
    elif choice == "n" or choice == "no":
        continue