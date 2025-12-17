from app_functionality import login, user_dashboard, prompt_login_or_create_account, display_welcome_message


user_data = None
display_welcome_message()
while True:
    choice = prompt_login_or_create_account()
    if choice == 1:
        user_data = login()
        break
    
    elif choice not in [1, 2]:
        print("Enter either 1 or 2\n")
        continue
    
# If user_data is present then display tailored dashboard for user
if user_data:
    user_dashboard(user_data)
