from psycopg2 import connect

from clcrypto import check_password

from ClassUserForTableUsers import User
from ClassMessageForTableMessages import Message
from CONSTANT import USER, HOST, PASSWORD, PORT, DB

def connect_to_db():
    '''Connect to database messanger_db
    
    :rtype: object `cursor` from psycopg2'''

    connection = connect(host=HOST, user=USER, password=PASSWORD, port=PORT, dbname=DB)
    connection.autocommit = True
    return connection.cursor()

def create_user(cursor, username: str, password: str):
    if len(password) < 8:
        print('Provided password is to short. 8 characters is minium.')
    else:
        user = User(username, password)
        
        try:
            user.save_do_db(cursor)
            print(f'User {username} created')
        except UniqueViolation as error:
            print(f'User {username} already exists. {error}')

def edit_user_password(cursor, username: str, password: str, new_password: str):
    if len(new_password) < 8:
        print('Provided password is to short. 8 characters is minium.')
    else:
        user = User.load_users_by_username(cursor, username)
        if user:  # user exists in db?
            if check_password(password, user.hashed_password):
                user.set_password(new_password)
                user.save_do_db(cursor)
                print(f'User {username} password was changed')
            else:
                print('Password is not correct')
        else:
            print(f'User {username} do not exist.')

def delete_user(cursor, username, password):
    user = User.load_users_by_username(cursor, username)
    if user:
        if check_password(password, user.hashed_password):
            user.delete(cursor)
            print(f'User {username} was deleted.')
        else:
            print('Password is not correct')
    else:
        print(f'User {username} do not exist.')

def list_users(cursor):
    users = User.load_all_users(cursor)

    for user in users:
        print(f'{user.id}. {user.username}')

def send_message(cursor, username: str, password: str, to_username: str, message: str):
    '''Save message to database.'''
    user_from = User.load_users_by_username(cursor, username)
    if user_from:
        if check_password(password, user_from.hashed_password):
            user_to = User.load_users_by_username(cursor, to_username)
            if user_to:
                if len(message) <= 255:
                    message = Message(message, user_from.id, user_to.id)
                    message.save_to_db(cursor)
                else:
                    print('Message is to long. 255 charactes is maximum.')
            else:
                print(f'User {to_username} do not exist.')    
        else:
            print('Password is not correct')
    else:
        print(f'User {username} do not exist.')

def list_messages(cursor, username: str, password: str):
    '''Shows all messages send by user.'''
    user_from = User.load_users_by_username(cursor, username)
    if user_from:
        if check_password(password, user_from.hashed_password):
            messages = Message.load_all_messages(cursor)
            for message in messages:
                if message.from_id == user_from.id:
                    user = User.load_users_by_id(cursor, message.to_id)
                    print(f'Message to: {user.username} {message.creation_date}\n' \
                          f'{message.text}')
        else:
            print('Password is not correct')
    else:
        print(f'User {username} do not exist.')
    