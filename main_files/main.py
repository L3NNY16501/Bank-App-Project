from app_functionality import login, user_dashboard, prompt_login_or_create_account, create_account


user_data = None

print("Welcome to Leonard Bank")

while True:
    choice = prompt_login_or_create_account()
    
    if choice == 1:
        user_data = login()
        break
    
    # Will create functionality for creating an account
    elif choice == 2:
        create_account()
    
    elif choice not in [1, 2]:
        print("Enter either 1 or 2\n")
        continue
    
# If user_data is present then display tailored dashboard for user
if user_data:
    user_dashboard(user_data)
