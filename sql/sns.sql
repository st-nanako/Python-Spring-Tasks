CREATE DATABASE python_sns;

CREATE TABLE users(
    id INTEGER AUTO_INCREMENT not null,
    name VARCHAR(64) not null,
    mail VARCHAR(64) not null UNIQUE,
    pw VARCHAR(64) not null,
    salt VARCHAR(20) not null,
    PRIMARY KEY(id)
);

CREATE TABLE posting(
    id INTEGER AUTO_INCREMENT not null,
    user_id INTEGER not null,
    post_text VARCHAR(400) not null,
    PRIMARY KEY(id),
    FOREIGN KEY(user_id) REFERENCES users(id)
);

CREATE TABLE evaluation(
    id INTEGER AUTO_INCREMENT not null,
    user_id INTEGER not null,
    posting_id INTEGER not null,
    PRIMARY KEY(id),
    FOREIGN KEY(user_id) REFERENCES users(id),
    FOREIGN KEY(posting_id) REFERENCES posting(id)
);

CREATE TABLE user_icon(
    id INTEGER AUTO_INCREMENT not null,
    user_id INTEGER not null,
    user_icon_path VARCHAR(400) not null,
    PRIMARY KEY(id),
    FOREIGN KEY(user_id) REFERENCES users(id)
);
