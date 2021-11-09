import argparse

from functions import connect_to_db
from functions import create_user, delete_user, edit_user_password, list_users
from ClassUserForTableUsers import User

parser = argparse.ArgumentParser()

parser.add_argument('-u', '--username', help='username')
parser.add_argument('-p', '--password', help='password')
parser.add_argument('-n', '--new_password', help='new_password')
parser.add_argument('-l', '--list', help='list', action='store_true')
parser.add_argument('-d', '--delete', help='delete', action='store_true')
parser.add_argument('-e', '--edit', help='edit', action='store_true')

args = parser.parse_args()

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