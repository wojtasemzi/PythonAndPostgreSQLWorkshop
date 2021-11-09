from clcrypto import hash_password


class User:
    def __init__(self, username = "", password = "", salt = "") -> None:
        self._id = -1
        self.username = username
        self._hashed_password = hash_password(password, salt)

    @property
    def id(self) -> int:
        return self._id

    @property
    def hashed_password(self) -> str:
        return self._hashed_password

    def set_password(self, password: str, salt = "") -> None:
        self._hashed_password = hash_password(password, salt)

    def save_do_db(self, cursor):
        '''Save object `User` to database or updates it.
        
        :rtype: bool
        :return: Returns True when save or updates.
        '''
        if self._id == -1:
            sql = "INSERT INTO Users(username, hashed_password) VALUES(%s, %s) RETURNING id"
            values = (self.username, self.hashed_password)
            cursor.execute(sql, values)
            self._id = cursor.fetchone()[0]

            return True
        else:
            sql = "UPDATE Users SET username=%s, hashed_password=%s WHERE id=%s"
            values = (self.username, self.hashed_password, self.id)
            cursor.execute(sql, values)

            return True

    @staticmethod
    def load_users_by_username(cursor, username: str):
        '''Loads object `User` from User Table witch provided username.

        :param cursor cursor:
        :param str username: User Name

        :rtype: User
        :return: Object `User` representing row in table Users or `None` if user do not exist.'''
        sql = "SELECT id, username, hashed_password FROM Users WHERE username=%s"
        cursor.execute(sql, (username,))  # (username, ) - cause we need a tuple
        data = cursor.fetchone()
        if data:
            id_, username, hashed_password = data
            loaded_user = User(username)
            loaded_user._id = id_
            loaded_user._hashed_password = hashed_password
            return loaded_user
        else:
            return None

    @staticmethod
    def load_users_by_id(cursor, id_: int):
        '''Loads object `User` from User Table witch provided id_.

        :param cursor cursor:
        :param int id_: User ID

        :rtype: User
        :return: Object `User` representing row in table Users or `None` if user do not exist.'''
        sql = "SELECT id, username, hashed_password FROM users WHERE id=%s"
        cursor.execute(sql, (id_,))  # (id_, ) - cause we need a tuple
        data = cursor.fetchone()
        if data:
            id_, username, hashed_password = data
            loaded_user = User(username)
            loaded_user._id = id_
            loaded_user._hashed_password = hashed_password
            return loaded_user
        else:
            return None

    @staticmethod
    def load_all_users(cursor) -> list:
        '''Loads all users from User Table.

        :param cursor cursor: 

        :rtype: list
        :return: List of objects User representing rows in table Users'''
        sql = "SELECT id, username, hashed_password FROM Users"
        users = list()
        cursor.execute(sql)
        for row in cursor.fetchall():
            id_, username, hashed_password = row
            loaded_user = User()
            loaded_user._id = id_
            loaded_user.username = username
            loaded_user._hashed_password = hashed_password
            users.append(loaded_user)
        return users

    def delete(self, cursor) -> bool:
        '''Delete user from DB.
        
        :rtype: bool
        :return: True if deleted'''
        sql = "DELETE FROM Users WHERE id=%s"
        cursor.execute(sql, (self.id,))
        self._id = -1
        return True
