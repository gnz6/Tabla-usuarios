class UserDAO:
    SELECT = "SELECT * FROM User ORDER BY user_id"
    INSERT = "INSERT INTO User(user_id, username, password) VALUES( %s, %s, %s )"
    UPDATE = "UPDATE User SET username=%s , password=%s WHERE user_id=%s"
    DELETE = "DELETE FROM User WHERE user_id=%s"

    @classmethod
    def select(cls):
        pass

    @classmethod
    def insert(cls):
        pass

    @classmethod
    def update(cls, user):
        pass

    @classmethod
    def delete(cls, user):
        pass
