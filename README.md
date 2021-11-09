# Python_i_bazy_danych_-_Warsztat

How to start program:
1. Create PostgreSQL server.
2. Database cridential put in file `CONSTANT.py` into constants `USER`, `HOST`, `PASSWORD`, `PORT`.
3. Create database by running program `create_db.py`.

## `user.py`
Terminal program for creating users. U can:
python3 user.py -u username -p password
Create user.

python3 user.py -u username -p password -n new_password -e
Edit user password.

python3 user.py -u username -p password -d
Delets user.

python3 user.py -l
List all Users.

## `messanger.py`
python3 user.py -u username -p password -l
List all messages send by User.

python3 user.py -u user1name -p password -t user2name -s message
Send message from User1 to User2.
