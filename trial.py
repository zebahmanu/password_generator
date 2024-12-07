import string
import random

length= int(input("What is the length: "))

choice= int(input(" Press 1 for letters, Press 2 for digits, Press 3 for both"))


def password_generator(choice, length):
    letters= string.ascii_letters
    numbers= map(str, range(0,9))
    print(numbers)
    lettersAndNumbers= [letters, numbers] #initialzing variable for both 
    password=""
    while(len(password)<=length):
        if (choice==1):
            password+=random.choice(letters)
        elif (choice==2):
            password+=random.choice(numbers)
        elif (choice==3):
            password+=random.choice(lettersAndNumbers)
        else:
            choice= input("Enter a valid option")
    print("Your password: "+password)

password_generator(choice,length)







