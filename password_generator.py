import random
import string

#what type of password
def generate_password(min_length, numbers=True, special_characters=True):
   
   #here i just defined what different characters mean with string
    letters = string.ascii_letters
    digits =string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special
    
    #pwd = password

    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False

#len = length
    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char

#this is to know if the password includes digits and special characters
        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True
#conditions
        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_characters:
            meets_criteria = meets_criteria and has_special
    return pwd

#input
min_length = int(input("Enter the minium length:"))
has_number = input("Do you have numbers (Y/N)? ").lower()=="y"
has_special = input("Do you have special characters (Y/N)? ").lower() =="y"
pwd = generate_password(min_length, has_number, has_special)
print("The generated password is:", pwd)
#added even this so it doesnt close instantly when the password is given
input("Press enter to exit;")