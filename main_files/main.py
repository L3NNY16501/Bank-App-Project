import user_accounts
from bank_functionality import login, main_menu

# Login and store users data if successful
user_data = login()

if user_data:
    main_menu(user_data)
