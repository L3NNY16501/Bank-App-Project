from user_accounts import users
from bank_account_functionality import display_balance

# Module contains functionality for app (Login, Deposit, Withdraw, View Balance)


def login() -> dict: 
    print("Welcome to Banking App!\n")
    username = input("Please enter your username: ").lower().strip()
    
    if username in users:
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


def user_dashboard(user_data):
    """
    If login successful and user_data is found then user_dashboard() will display
    the available options within the banking app and prompt the user for 
    their selection
    """
    
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
            selection = int(prompt)
            if selection not in [1,2,3]:
                print("Please select a Valid Choice.\n")
                continue
        except Exception as e:
            print("Please select a Valid Choice.\n")
            continue
        
        if selection == 1:
            display_balance(user_data)
            continue
            

    