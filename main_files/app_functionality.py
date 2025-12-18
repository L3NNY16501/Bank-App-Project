from json_file_handling import load_users, save_users
from bank_account_functionality import display_balance, deposit, withdraw

# Module contains functionality for app (Login, Deposit, Withdraw, View Balance)

    
def prompt_login_or_create_account() -> int:
    while True:  
        print("""
    Please Select a following option:
    1) Login
    2) Create an Account
    """)  
        
        prompt = input("Select: ")
        try:
            choice = int(prompt)
        except ValueError:
            print("Please Select a valid choice.\n")
            continue
        
        return choice
    

def login(users) -> dict: 
            
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
        

def create_account() -> dict:
    try:
        users = load_users()
    except FileNotFoundError:
        print("Error: File not found!")
        return None   
    
    # Ask for a username
    while True: 
        prompt = input("Please create a username: ")
        
        if prompt.lower().strip() in users:
            print("Username taken.\n")
            continue
        else:
            username = prompt.strip().lower()
            print("username created Successfully!\n")
            break
        
    while True:    
        initial_password = input("Please create a password: ")
        confirm_password = input("Please confirm your password: ")
        
        if confirm_password == initial_password:
            password = initial_password
            print("Password created Successfully!\n")
            break
        else:
            print("Passwords do not match.\n")
            continue
        
    while True:
        initial_deposit_prompt = input("Please enter your initial deposit: ")
        
        try:
            deposit = round(int(initial_deposit_prompt), 2)
            break
        except ValueError:
            print("Please enter a valid number\n")
            continue
            
    users[username] = {
        "username": username,
        "password": password,
        "balance" : deposit
                       }
    
    save_users(users)
    print("Account created Successfully!\n")


def user_dashboard(user_data: dict) -> None:
    """
    If login successful and user_data is found then user_dashboard() will display
    the available options within the banking app and prompt the user for 
    their selection
    """
    print(f"Welcome {user_data["username"]}")
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
        except ValueError:
            print("Please select a Valid Choice.\n")
            continue
        
        if selection == 1:
            display_balance(user_data)
            continue
        
        if selection == 2:
            deposit(user_data)
            continue
        
        if selection == 3:
            withdraw(user_data)
            continue
            

    