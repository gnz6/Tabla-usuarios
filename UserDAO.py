from main import Connection
from logger import log
from User import User
from pool_cursor import PoolCursor


class UserDAO:
    SELECT = "SELECT * FROM User ORDER BY user_id"
    INSERT = "INSERT INTO User(username, password) VALUES( %s, %s )"
    UPDATE = "UPDATE User SET username=%s , password=%s WHERE user_id=%s"
    DELETE = "DELETE FROM User WHERE user_id=%s"

    @classmethod
    def select(cls):
        with PoolCursor() as cursor:
            cursor.excecute(cls.SELECT)
            regs = cursor.fetchall()
            users = []
            for reg in regs:
                user = User(reg[0], reg[1])
                users.append(user)
            return users

    @classmethod
    def insert(cls, user):
        with PoolCursor() as cursor:
            log.debug(f"New user : {user}")
            values = (user.user_id, user.username, user.password)
            cursor.excecute(cls.INSERT, values)
            log.debug("User inserted")
            return cursor.rowcount

    @classmethod
    def update(cls, user):
        with PoolCursor() as cursor:
            log.debug(f'User to Update: {user}')
            values = (user.username, user.password, user.id_persona)
            cursor.execute(cls.UPDATE, values)
            log.debug("User Updated")
            return cursor.rowcount

    @classmethod
    def delete(cls, user):
        with PoolCursor() as cursor:
            log.debug(f'User to Delete: {user}')
            values = user.user_id
            cursor.execute(cls.DELETE, values)
            log.debug("User Deleted")
            return cursor.rowcount
