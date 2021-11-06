USER = 'postgres'
HOST = 'localhost'
PASSWORD = 'coderslab'
PORT = 5435

DB = 'messanger_db'

CREATE_DB = f"CREATE DATABASE {DB};"
CREATE_TABLE_USERS = """CREATE TABLE Users (
    id serial PRIMARY KEY,

    username varchar(255) UNIQUE,
    hashed_password varchar(80)
);"""
CREATE_TABLE_MESSAGES = """CREATE TABLE Messages (
    id serial PRIMARY KEY,

    from_id int REFERENCES Users(id) ON DELETE CASCADE,
    to_id int REFERENCES Users(id) ON DELETE CASCADE,

    creation_date timestamp DEFAULT CURRENT_TIMESTAMP,
    text varchar(255)
);"""

