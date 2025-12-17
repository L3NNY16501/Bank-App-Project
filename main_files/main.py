from app_functionality import login, user_dashboard


# Prompt user for either login or account creation
while True:
    user_data = None
    print("""Welcome to Leonard Bank
    Please select a following option:
    1) Login
    2) Create an Account
        """)
    prompt = input("Selection: \n")

    try:
        choice = int(prompt)
        if choice == 1:
            # Login and store users data if successful
            user_data = login()
            break
        elif choice not in [1, 2]:
            print("Enter either 1 or 2\n")
            continue
    except ValueError:
        print("Please Select a valid choice.\n")
        continue
    
# If user_data is present then display tailored dashboard for user
if user_data:
    user_dashboard(user_data)
