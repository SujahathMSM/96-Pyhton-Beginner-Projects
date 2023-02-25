import getpass

# Define a dictionary of usernames and passwords
user_data = {
    "john": "password123",
    "jane": "password456",
    "bob": "password789"
}

# Define a function to add a new user to the dictionary
def add_user():
    new_username = input("Enter a new username: ")
    if new_username in user_data.keys():
        print("That username already exists.")
        return
    new_password = getpass.getpass(prompt="Enter a new password: ")
    user_data[new_username] = new_password
    print("User added successfully.")

# Define a function to remove a user from the dictionary
def remove_user():
    username_to_remove = input("Enter the username to remove: ")
    if username_to_remove not in user_data.keys():
        print("That username does not exist.")
        return
    del user_data[username_to_remove]
    print("User removed successfully.")

# Main authentication loop
while True:
    # Prompt the user for a username
    username = input("Enter your username: ")

    # Check if the username is in the dictionary
    if username not in user_data.keys():
        print("Invalid username.")
        continue

    # Prompt the user for a password
    password = getpass.getpass(prompt="Enter your password: ")

    # Check if the password is correct
    if password == user_data[username]:
        print("Authentication successful.")
        break
    else:
        print("Incorrect password.")

# After successful authentication, offer additional functionality
while True:
    print("What would you like to do?")
    print("1. Add a new user")
    print("2. Remove a user")
    print("3. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_user()
    elif choice == "2":
        remove_user()
    elif choice == "3":
        print("Exiting program.")
        break
    else:
        print("Invalid choice.")
