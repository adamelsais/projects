# Adam's password manager
from cryptography.fernet import Fernet
import os

# function used to create the key.key file; only use once then comment out
""""
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

write_key()"""

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

master_pass = input("What is the master password? ")
key = load_key() + master_pass.encode()
fer = Fernet(key)


# view passwords
def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("Username:",user, "| Password:", 
                            fer.decrypt(passw.encode()).decode())

# add accounts & passwords
def add():
    name = input("Account name: ")
    pswd = input("Password: ")
    # open file to append new acc & pass
    with open("passwords.txt", "a") as f:
        f.write(name + "|" + fer.encrypt(pswd.encode()).decode() + "\n")
'''
def delete():
    u = input("User to delete: ")
    psw = input("Password to authorize: ")
    with open("passwords.txt", "r") as f:
        lines =  f.readlines()
        for line in lines:
            data = line.rstrip()
            user, passw = data.split("|")
            if user == u:
                # this is the decrypted password that matches the input username
                passDecrypt = fer.decrypt(passw.encode()).decode()
                print(passDecrypt)
                break
            else:
                continue
    
    with open("passwords.txt", "w") as file:
        for line in lines:
            stripUser = line.strip(u)
            strip = stripUser.strip("|")
            if strip != psw and strip !=passDecrypt :
                file.write(line)
    
    with open("passwords.txt", "r") as input: 
         with open("temp.txt", "w") as output:
            for line in input:
                if line.strip("\n") != user:
                    output.write(line)
    # replace file with original name
    os.replace('temp.txt', "passwords.txt")             
'''

# runs program continously 
while True:
    mode = input("Add new password, view existing, or delete existing (add, view, delete), or press q to quit: ")
    if mode.lower() == "q":
        break
    if mode.lower() == "view":
        view()
    elif mode.lower() == "add":
        add()
    elif mode.lower() == "delete":
       #delete()
       pass
    else:
        print("invalid mode")
        continue
