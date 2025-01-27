import string
import random

def password_generator(length):
    letters= string.ascii_letters
    special_characters= string.punctuation
    numbers=string.digits
    CharacterSet=""
    password=""
    choice=0 
    while (choice!=4): #Loop until user needs to exit menu
        print("What characters would you like to include in your password.\nMenu:\n1.Letters \n2.Numbers\n3.Special characters\n4.Exit Menu")
        choice= int(input("Please enter your option:"))
        if (choice==1):
            CharacterSet+= letters
        elif (choice==2):
            CharacterSet+= numbers
        elif (choice==3):
            CharacterSet+= special_characters
        elif (choice==4):
            break
        else:
            choice= input("Enter a valid option:")
    while(len(password)<length):
        password+=random.choice(CharacterSet)
    print("Your password is: "+password)

length= int(input("What is the length of the password?: "))
password_generator(length) #calling the function
        

        
    






