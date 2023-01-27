from UserDAO import UserDAO
from logger import log
from User import User
import sys

selection = None
while selection != 5:
    print(f'''
     Options :
    1. List Users
    2. Add User
    3. Update User
    4. Delete User
    5. Exit
    '''
          )

    selection = int(input("Select your option (1-5):"))
    if selection == 1:
        users = UserDAO.select()
        for user in users:
            log.info(user)
    if selection == 2:
        username_var = str(input("Insert Username: "))
        password_var = str(input("Insert Password: "))
        user = User(username=username_var, password=password_var)
        insert_user = UserDAO.insert(user)
        log.info(f"User inserted : {insert_user}")
    if selection == 3:
        username = input("Insert Username: ")
        password = input("Insert Password: ")
        user_id = int(input("User ID:"))
        user = (username, password, user_id)
        UserDAO.update(user)
    if selection == 4:
        user_id = int(input("User ID:"))
        UserDAO.delete(user_id)
    if selection == 5:
        log.info("Exit")
        sys.exit()
    else:
        log.info("Exit")
