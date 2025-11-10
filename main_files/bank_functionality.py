from user_accounts import users

# Module contains functionality for app (Login, Deposit, Withdraw, View Balance)

def login():
    logged_in = False
    print("Welcome to Banking App!\n")
    username = input("Please enter your username: ").lower().rstrip().lstrip()
    if username in users.keys():
        print("Username valid\n")
        
        password = input("Please enter your password: ")
        if password == users[username]["password"]:
            print("Password Correct. Login Successful!")
            logged_in = True
        else:
            print("Password Incorrect!")
    
    else:
        print(f"Username: {username} not found!")