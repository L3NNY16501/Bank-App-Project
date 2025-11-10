import user_accounts
from bank_functionality import login, user_dashboard

# Login and store users data if successful
user_data = login()

if user_data:
    user_dashboard(user_data)
