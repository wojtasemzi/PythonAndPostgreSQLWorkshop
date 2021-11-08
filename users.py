import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-u', '--username', help='username')
parser.add_argument('-p', '--password', help='password')
parser.add_argument('-n', '--new_pass', help='new_pass')
parser.add_argument('-l', '--list', help='list', action='store_true')
parser.add_argument('-d', '--delete', help='delete', action='store_true')
parser.add_argument('-e', '--edit', help='edit', action='store_true')

args = parser.parse_args()

if args.username and args.password:
    if args.new_pass and args.edit:  # Edit user password if username, password, new password is provided
                                     # and edit is flaged:
        print('Edit user password if username, password, new password is provided and edit is flaged:')
    elif args.delete: # Delete user if username, password is provided and delete is flaged:
        print('Delete user if username, password is provided and delete is flaged:')
    else: # Create user if username and password is provided:
        print('Create user if username and password is provided:')
elif args.list:  # List users if list is flaged:
    print('List users if list is flaged:')
else:
    parser.print_help()