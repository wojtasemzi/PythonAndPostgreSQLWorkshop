from clcrypto import hash_password


class Message:
    def __init__(self, text: str, from_id: int, to_id: int) -> None:
        self._id = -1
        self.from_id = from_id
        self.to_id = to_id
        self.text = text
        self.creation_date = None

    @property
    def id(self) -> int:
        return self._id

    def save_to_db(self, cursor) -> bool:
        '''Save object `Message` to database or updates it.
        
        :rtype: bool
        :return: Returns True when save or updates.
        '''
        if self._id == -1:
            sql = "INSERT INTO Messages(from_id, to_id, text) VALUES(%s, %s, %s) RETURNING id"
            values = (self.from_id, self.to_id, self.text)
            cursor.execute(sql, values)
            self._id = cursor.fetchone()['id']

            return True
        else:
            sql = """UPDATE Messages SET from_id=%s, to_id=%s, text=%s WHERE id=%s"""
            values = (self.from_id, self.to_id, self.text, self.id)
            cursor.execute(sql, values)

            return True

    @staticmethod
    def load_all_messages(cursor) -> list:
        '''Loads all messages from table Messages

        :rtype: list of `Message`
        :return: List of objects `Message` representing rows in table Messages
        '''
        sql = "SELECT id, from_id, to_id, text, creation_date FROM Messages"
        messages = list()
        cursor.execute(sql)
        for row in cursor.fetchall():
            id_, from_id, to_id, text, creation_date = row
            loaded_message = Message()
            loaded_message._id = id_
            loaded_message.from_id = from_id
            loaded_message.to_id = to_id
            loaded_message.text = text
            loaded_message.creation_date = creation_date 
            messages.append(loaded_message)
        return messages
