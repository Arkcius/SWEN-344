-- We specify our primary key here to be as repeatable as possible
INSERT INTO example_table(id, foo) VALUES
  (1, 'hello, world!');
INSERT INTO users(id, firstname,lastname,contact) VALUES(1, 'Ada','Lovelace','ada@gmail.com');
INSERT INTO users(id, firstname,lastname,contact) VALUES(2, 'Mary','Shelley','mary@gmail.com');
INSERT INTO users(id, firstname,lastname,contact) VALUES(3, 'Jackie','Gleason','jackie@gmail.com');
INSERT INTO users(id, firstname,lastname,contact) VALUES(4, 'Art','Garfunkel','art@gmail.com');

INSERT INTO btype(id,genre) VALUES(1,'Fiction');
INSERT INTO btype(id,genre) VALUES(2,'Non-Fiction');

INSERT INTO books(id,title,author,publish,genre) VALUES(1,'Hobbit','LOTR guy','10/15/1899',1);
INSERT INTO books(id,title,author,publish,genre) VALUES(2,'Land Before Time','dinosaurs','10/15/0001',2);
INSERT INTO books(id,title,author,publish,genre) VALUES(3,'Library rest','Api','10/15/2023',2);
INSERT INTO books(id,title,author,publish,genre) VALUES(4,'a book','a dude','10/15/2021',1);

INSERT INTO checkouts(id,bookID,userID) VALUES(1,1,4);
INSERT INTO checkouts(id,bookID,userID) VALUES(2,1,3);
INSERT INTO checkouts(id,bookID,userID) VALUES(3,2,1);
INSERT INTO checkouts(id,bookID,userID) VALUES(4,3,1);
INSERT INTO checkouts(id,bookID,userID) VALUES(5,2,3);

-- Restart our primary key sequences here so inserting id=DEFAULT won't collide
ALTER SEQUENCE users_id_seq RESTART 1000;
ALTER SEQUENCE books_id_seq RESTART 1000;
ALTER SEQUENCE btype_id_seq RESTART 1000;
ALTER SEQUENCE checkouts_id_seq RESTART 1000;
ALTER SEQUENCE example_table_id_seq RESTART 1000;