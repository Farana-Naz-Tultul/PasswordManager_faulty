from cryptography.fernet import Fernet #this module allows us to encrypt texts.

def write_key():
    key = Fernet.generate_key()
    with open('key.key','wb') as key_file: #wb is write/bytes, a module, not important to know.
        key_file.write(key)

#write_key() #has to be commented out if I run it for the second time,
# otherwise it's giving out an exception, as a key is already generated.
# Every time I run, it will try to generate another key, which iks why had to comment it out.

def load_key():
    file = open('key.key','rb') #rb is read/bytes
    key = file.read()
    file.close()
    return key

"""key + password is what we are going to use to encrypt the text.
   A key takes a string of text and turns it into a random string of text that we 
   cannot get back into without the key and the password combined.
   So,
   key + password + text to encrypt = random text
   random text + key + password = text to encrypt
   """
#need two functions. one to create a key another to retrieve a key.

#master_pwd = input("What is the master password? ")
key = load_key() #+ master_pwd.encode() #key is in bytes so need to convert master password into bytes, hence .bytes.
fer = Fernet(key)


    #pass
    #we open files with the line below, which also closes the file because of the "with". f is the variable for the file
def view(): #this is a function.
    with open('passwords.txt', 'r') as f: #'a' = append, 'w' = write and 'r' = read
        for line in f.readlines():
            #print(line.rstrip()) --- .rstrip removes the next line from the end, \n.

            data = line.rstrip()
            username, passw = data.split("|") #.split() splits the data by the "|" symbol and stores into a list."
            print("Username:" , username , "Password:", fer.decrypt(passw.encode()).decode())

def add():
    #pass
    name = input("Account name: ")
    pwd = input("Password: ")

    """file = open('passwords.txt', 'a')
    file.close()"""

    with open('passwords.txt', 'a') as f:
        #f.write(name + "|" + str(fer.encrypt(pwd.encode())) + "\n") #encoding converts into bytes.
        #we cannot have str(). we need to decode instead. Because  that put a b in front of the string, making it a byte.

        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n") #takes a byte string and decodes to regular string

while True:
    #pass
    mode = input("Would you like to add a new password, view or quit (add/view/q)? ").lower()
    if mode == "q":
        break

    if mode == "add":
        #pass
        add()
    elif mode == "view":
        #pass
        view()
    else:
        #pass
        print("Invalid mode.")
        continue