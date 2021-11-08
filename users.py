import argparse
from psycopg2 import connect
from psycopg2.errors import UniqueViolation

from clcrypto import check_password
from ClassUserForTableUsers import User
from CONSTANT import USER, HOST, PASSWORD, PORT, DB

parser = argparse.ArgumentParser()

parser.add_argument('-u', '--username', help='username')
parser.add_argument('-p', '--password', help='password')
parser.add_argument('-n', '--new_password', help='new_password')
parser.add_argument('-l', '--list', help='list', action='store_true')
parser.add_argument('-d', '--delete', help='delete', action='store_true')
parser.add_argument('-e', '--edit', help='edit', action='store_true')

args = parser.parse_args()

def connect_to_db():
    '''Connect to database messanger_db
    
    :rtype: cursor'''
    connection = connect(host=HOST, user=USER, password=PASSWORD, port=PORT, dbname=DB)
    connection.autocommit = True
    return connection.cursor()

def create_user(cursor, username: str, password: str):
    if len(password) < 8:
        print('Provided password is to short. 8 characters is minium.')
    else:
        user = User(args.username, args.password)
        
        try:
            user.save_do_db(cursor)
            print(f'User {username} created')
        except UniqueViolation as error:
            print(f'User {args.username} already exists. {error}')

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

if args.username and args.password:
    if args.new_password and args.edit:  # Edit user password if username, password, new password is provided
                                         # and edit is flaged:
        edit_user_password(connect_to_db(), args.username, args.password, args.new_password)
    elif args.delete: # Delete user if username, password is provided and delete is flaged:
        delete_user(connect_to_db(), args.username, args.password)
    else: # Create user if username and password is provided:
        create_user(connect_to_db(), args.username, args.password)
elif args.list:  # List users if list is flaged:
    list_users(connect_to_db())
else:
    parser.print_help()