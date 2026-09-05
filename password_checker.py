# Password Strength Checker Project - easy task 2

def check_password(password):

    length = False
    uppercase = False
    lowercase = False
    number = False
    special = False

#to check all the conditions (using in built functions)

    for i in password:

        if i.isupper():
            uppercase = True

        if i.islower():
            lowercase = True

        if i.isdigit():
            number = True

        if not i.isalnum():
            special = True

    if len(password) >= 8:
        length = True

#to check the score

    score = 0

    if length == True:
        score = score + 1

    if uppercase == True:
        score = score + 1

    if lowercase == True:
        score = score + 1

    if number == True:
        score = score + 1

    if special == True:
        score = score + 1

#password strenght checker

    print("\n--------Password Strength Checker--------")

    if length:
        print("At least 8 characters  : Satisfied")
    else:
        print("At least 8 characters  : Not Satisfied")

    if uppercase:
        print("Uppercase letter  : Satisfied")
    else:
        print("Uppercase letter  : Not Satisfied")

    if lowercase:
        print("Lowercase letter  : Satisfied")
    else:
        print("Lowercase letter  : Not Satisfied")

    if number:
        print("Number  : Satisfied")
    else:
        print("Number  : Not Satisfied")

    if special:
        print("Special character  : Satisfied")
    else:
        print("Special character  : Not Satisfied")

   
    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    else:
        strength = "Strong"

    print("Score:", score, "/ 5")
    print("Strength:", strength)


password = input("Enter your password: ")
check_password(password)

# end of code