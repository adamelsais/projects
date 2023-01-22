# Adam's password generator

import random
import string
#import requests

r_str = string.ascii_letters

r_sc = ['~', '`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-','+', '=', '{', '[', '}', ']', '|', ':', ';', "'", '<', ',', '>', '.', '?', '/']
sc = ''.join(map(str,r_sc))

characters = string.ascii_letters + string.digits + sc
# print(characters)


def random_pass():
    ''' sig: None-> None
    takes user input for pass len, prints a randomized
    password'''
    
    # length is input from user
    length = int(input("Enter password length: "))

    r_pass = []
    # appends random characters into the list
    for x in range(length):
        r_pass.append(random.choice(characters))

    # shuffle list to be randomized
    random.shuffle(r_pass)

    # print random password as a string

    print(''.join(r_pass))



def pass_prob():
    ''' sig: none -> none
    takes length of password, prints a random password
    uses probability (1-10) to choose the character to use
    (str, int, special characters)
    '''

    # length is input from user
    length = int(input("Enter password length: "))
    
    #list where password is stored
    ran_pass = []

    # appends a int, str, or spec. char depending on randomizer
    for x in range(length):
        r_int = random.randint(0,9)
        randomizer = random.randint(1,10)
        #print(randomizer)
        if randomizer>=1 and randomizer < 4:
            ran_pass.append(r_int)
        elif randomizer >= 4 and randomizer < 9:
            ran_pass.append(random.choice(r_str))
        else:
            ran_pass.append(r_sc[random.randint(0, len(r_sc) - 1)])
    final_pass = ''.join(map(str,ran_pass))
    print(final_pass)
    
    
def pass_choice():
    '''sig: none -> none
    user inputs number of:
    letters, numbers, & special characters wanted in rand pass
    '''

    nstr = int(input("Enter number of letters wanted in password: "))
    ndigits = int(input("Enter number of digits wanted in password: "))
    nsc = int(input("Enter number of special characters wanted in password: "))

    r_int = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    password = []
    length = nstr + ndigits + nsc

    for x in range(nstr):
        password.append(random.choice(r_str))
    for x in range(ndigits):
        password.append(str(random.choice(r_int)))
    for x in range(nsc):
        password.append(random.choice(r_sc))

    
    random.shuffle(password)

    print(''.join(map(str, password)))
    
        
    
    






