class User:
    idCounter = 0

    def __init__(self, username, password):
        User.idCounter += 1
        self.user_id = User.idCounter
        self.username = username
        self.password = password

    def __str__(self):
        return f'''
User {self.user_id} : {self.username}
'''
