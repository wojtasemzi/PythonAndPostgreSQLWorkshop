from psycopg2 import connect, OperationalError
from psycopg2.errors import DuplicateDatabase, DuplicateTable

from CONSTANT import CREATE_DB, CREATE_TABLE_MESSAGES, CREATE_TABLE_USERS
from CONSTANT import USER, HOST, PASSWORD, PORT, DB

try:
    connection = connect(host=HOST, user=USER, password=PASSWORD, port=PORT)
    connection.autocommit = True

    cursor = connection.cursor()

    try:
        cursor.execute(CREATE_DB)
    except DuplicateDatabase as error:
        print(f'Database exist. {error}')

    connection.close()
except OperationalError as error:
    print(f'Connection failed: {error}')

try:
    connection = connect(host=HOST, user=USER, password=PASSWORD, port=PORT, dbname=DB)
    connection.autocommit = True

    cursor = connection.cursor()

    try:
        cursor.execute(CREATE_TABLE_USERS)
    except DuplicateTable as error:
        print(f'Table Users exist. {error}')

    try:
        cursor.execute(CREATE_TABLE_MESSAGES)
    except DuplicateTable as error:
        print(f'Table Messages exist. {error}')

    connection.close()
except OperationalError as error:
    print(f'Connection failed: {error}')
