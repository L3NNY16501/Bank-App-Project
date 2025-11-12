

def display_balance(user_data: dict) -> None:
    balance = user_data["balance"]
    print(f"Current balance: £{balance:,.2f}\n")
    
    
def deposit(user_data: dict) -> None:
    while True:
        deposit_amount_prompt = input("Please enter deposit amount: ")
        try:
            deposit_amount = float(deposit_amount_prompt)
        except ValueError:
            print("Please enter a valid amount.\n")
            continue
                
        if deposit_amount <= 0:
            print(f"Cannot deposit £{deposit_amount:,.2f}.")
            continue
        else:
            user_data["balance"] += deposit_amount
            print(f"Deposit of £{deposit_amount:,.2f} succesful.\n")
            break
            

def withdraw(user_data: dict) -> None:
    while True:
        withdrawal_amount_prompt = input("Please Select a withdrawal amount: ")
        try:
            withdrawal_amount = float(withdrawal_amount_prompt)
        except:
            print("Please enter a valid number.\n")
            continue
        
        if withdrawal_amount > user_data["balance"]:
            print("Insufficient Balance.\n")
            continue
        
        if withdrawal_amount <= 0:
            print("Invalid Withdrawal Amount.\n")
            continue
        
        user_data["balance"] -= withdrawal_amount
        print(f"You have succesfully made a withdrawal of £{withdrawal_amount:,.2f}.")
        break
                    