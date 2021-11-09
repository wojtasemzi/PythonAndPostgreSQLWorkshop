import argparse

from functions import connect_to_db
from functions import send_message, list_messages

parser = argparse.ArgumentParser()

parser.add_argument('-u', '--username', help='username')
parser.add_argument('-p', '--password', help='password')
parser.add_argument('-t', '--to', help='send to')
parser.add_argument('-s', '--send', help='message')
parser.add_argument('-l', '--list', help='list', action='store_true')

args = parser.parse_args()

if args.username and args.password:
    if args.list:  # List messages if username, password is provided and list is flaged:
        list_messages(connect_to_db(), args.username, args.password)
    elif args.to and args.send:  # Send message if username, password, to and send is provided:
        send_message(connect_to_db(), args.username, args.password, args.to, args.send)
    else:
        parser.print_help()
else:
    parser.print_help()
