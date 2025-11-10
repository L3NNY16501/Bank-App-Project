from user_accounts import users

# Module contains functionality for app (Login, Deposit, Withdraw, View Balance)

def login():
    print("Welcome to Banking App!\n")
    username = input("Please enter your username: ").lower().rstrip().lstrip()
    if username in users.keys():
        print("Username valid\n")
                
        password = input("Please enter your password: ")
        if password == users[username]["password"]:
            print("Password Correct. Login Successful!\n")
            user_data = users[username]
            return user_data
        else:
            print("Password Incorrect!")
            
    else:
        print(f"Username: {username} not found!")
            
def main_menu(user_data):
    print("""Please Select from the following:
          
            1) Display Balance
            2) Deposit
            3) Withdraw
            
            Enter Quit to logout at any time.
            
            """)
    while True:
        prompt = input("Enter Selection: ") 
        if prompt.lower() == "quit":
            print("Logout Successful\n")
            exit()
        try:
            user_choice = int(prompt)
            if user_choice not in [1,2,3]:
                print("Please select a Valid Choice.\n")
                continue
        except Exception as e:
            print("Please select a Valid Choice.\n")
            continue
            

    