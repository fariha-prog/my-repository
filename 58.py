usernames = ['admin', 'jaden', 'sara', 'ali', 'haris', 'chris']
for username in usernames:
    if username == 'admin':
        print(f"Hello {username}, would you like to see a status report?")
    elif username!="admin":
        print(f"Hello {username}, thank you for logging in again.")
        #5.9
usernames = []
for username in usernames:
    if username == 'admin':
        print(f"Hello {username}, would you like to see a status report?")
    elif username=='jaden':
        print(f"Hello {username.capitalize()}, thank you for logging in again.")
    else:
        print('we need to find some users')
#5.10
current_users=['ali', 'haider', 'sara', 'fari', 'amna']
new_users = ['ali', 'zara', 'sara', 'bilal', 'fari']
for new_user in new_users:
    if new_user in current_users:
        print(f"Sorry, '{new_user}' is already taken. Please enter a new username.")
    elif new_users !=current_users:
        print(f"'{new_user}' is available. Welcome!")
    else:
        print("choose another name")
        #5.11
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for number in numbers:
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else:
        print(f"{number}th")