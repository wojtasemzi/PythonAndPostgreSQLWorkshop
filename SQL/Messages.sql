CREATE TABLE Messages (
    id serial PRIMARY KEY,

    from_id int (from_id) REFERENCES Users(id) ON DELETE CASCADE,
    to_id int (to_id) REFERENCES Users(id) ON DELETE CASCADE,

    creation_date timestamp DEFAULT CURRENT_TIMESTAMP,
    text varchar(255)
);