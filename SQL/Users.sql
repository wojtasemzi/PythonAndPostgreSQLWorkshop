CREATE TABLE Users (
    id serial PRIMARY KEY,

    username varchar(255) UNIQUE,
    hashed_password varchar(80)
);
