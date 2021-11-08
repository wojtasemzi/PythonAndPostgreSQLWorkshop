import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-u', '--username', help='username')
parser.add_argument('-p', '--password', help='password')
parser.add_argument('-t', '--to', help='send to')
parser.add_argument('-s', '--send', help='message')
parser.add_argument('-l', '--list', help='list', action='store_true')

args = parser.parse_args()

if args.username and args.password:
    if args.list:  # List messages if username, password is prowided and list is flaged:
        print('List messages if username, password is prowided and list is flaged:')
    elif args.to and args.send:  # Send message if username, password, to and send is provided:
        print('Send message if username, password, to and send is provided:')
    else:
        parser.print_help()
else:
    parser.print_help()
