

def display_balance(user_data) -> None:
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
            
        
        
                