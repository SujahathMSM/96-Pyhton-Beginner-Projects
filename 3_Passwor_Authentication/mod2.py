import getpass

class UserDatabase:
    def __init__(self):
        self.user_data = {
            "john": "password123",
            "jane": "password456",
            "bob": "password789"
        }

    def add_user(self):
        new_username = input("Enter a new username: ")
        if new_username in self.user_data.keys():
            print("That username already exists.")
            return
        new_password = getpass.getpass(prompt="Enter a new password: ")
        self.user_data[new_username] = new_password
        print("User added successfully.")

    def remove_user(self):
        username_to_remove = input("Enter the username to remove: ")
        if username_to_remove not in self.user_data.keys():
            print("That username does not exist.")
            return
        del self.user_data[username_to_remove]
        print("User removed successfully.")

class Authentication:
    def __init__(self, user_db):
        self.user_db = user_db

    def authenticate(self):
        while True:
            username = input("Enter your username: ")
            if username not in self.user_db.user_data.keys():
                print("Invalid username.")
                continue
            password = getpass.getpass(prompt="Enter your password: ")
            if password == self.user_db.user_data[username]:
                print("Authentication successful.")
                break
            else:
                print("Incorrect password.")

    def run(self):
        self.authenticate()
        while True:
            print("What would you like to do?")
            print("1. Add a new user")
            print("2. Remove a user")
            print("3. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                self.user_db.add_user()
            elif choice == "2":
                self.user_db.remove_user()
            elif choice == "3":
                print("Exiting program.")
                break
            else:
                print("Invalid choice.")

user_db = UserDatabase()
auth = Authentication(user_db)
auth.run()
