# Password Authentication using python
import getpass
data_base = {
    "aman.kharwal": "123456",
    "kharwal.aman" : "654321"
}

count = 0
while True:
    username = input("Enter user name: ")
    if username not in data_base.keys():
        print("User does not exist.. Please enter again..")
        continue
    break
        
password = getpass.getpass(prompt="Enter the password here.. ")

for i in data_base.keys():
    if i == username:
        while password != data_base.get(i):
            password = getpass.getpass(prompt="Wrong password.. Enter again: ")
        break
print("Welcome to the system..")