DROP TABLE IF EXISTS example_table;
DROP TABLE IF EXISTS checkouts;
DROP TABLE IF EXISTS books;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS btype;

CREATE TABLE example_table(
  id SERIAL PRIMARY KEY,
  foo TEXT NOT NULL
);

CREATE TABLE users(
  id SERIAL PRIMARY KEY,
  firstname TEXT,
  lastname TEXT,
  contact TEXT,
  password TEXT,
  sessionKey TEXT
);

CREATE TABLE btype(
  id SERIAL PRIMARY KEY,
  genre TEXT
);

CREATE TABLE books(
  id SERIAL PRIMARY KEY,
  title TEXT,
  author TEXT,
  publish TEXT,
  genre INTEGER NOT NULL,
  FOREIGN KEY (genre) REFERENCES BTYPE(id)
);

CREATE TABLE checkouts(
  id SERIAL PRIMARY KEY,
  bookID INTEGER,
  userID INTEGER,
  reserve BOOLEAN DEFAULT CAST(0 as BOOLEAN),
  FOREIGN KEY (bookID) REFERENCES BOOKS(id) ON DELETE CASCADE,
  FOREIGN KEY (userID) REFERENCES USERS(id) ON DELETE CASCADE
);