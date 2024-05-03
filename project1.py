#password managers
from cryptography.fernet import Fernet #encryption
'''
def write_key():#generate key
    key = Fernet.generate_key()
    with open("key.key","wb") as key_file:
        key_file.write(key)


write_key()
'''
def load_key():#decryption
    file = open("key.key","rb")
    key=file.read()
    file.close()
    return key

'''
master_pwd =input("what is the master password? ")
key=load_key() + master_pwd.encode()#.encode turns that string into bytes
'''

key=load_key() 
fer = Fernet(key)
'''
key + password + text to encrypt = random text
random text + key + password = text to  decrypt
'''



def view ():
    with open("passwords.txt","r") as f:
        for line in f.readlines():#f.readline return list of lines but one by one  using for loop
            data = line.rstrip()#strip the carriage return character (do not include next line character after the last )
            user , passw = data.split("|")
            print("user:",user,"| password:",fer.decrypt(passw.encode()).decode())
# .encode turns strings into byte string
# fer.decrypt() this decrypts our encrypted byte string to decrypted bytes string 
#.decode() is to convert our decrpted value which is in decrypted bytes string then we decode it into into decrypted string to view in string format                        
            '''
            "hello|lakshya"
            ["hello" , "lakshya"]
            user: hello | password: lakshya
            '''


def add():
    name= input("account name: ")
    pwd = input("password: ")
    with  open ("passwords.txt", "a") as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")
# .encode turns strings into byte string
# fer.encrypt() this encrypts our byte string to encrypted bytes string 
#.decode() is to store our encrpted value which is in encrypted bytes string then we decode it into into encrypted string 
# to store encrypted string is mandatory so we decode our encrypted bytes string to encrypted string                      
    '''
    if you use it like file=open("passwords.txt","a")
    then you have to close it manually
    '''    


        

while True:
    mode = input("Would you like to add a new password(enter 'add') or view existing ones (enter 'view') and press q to quit? ").lower()
    if mode == "q":
        break
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("invalid mode.")
        continue        
