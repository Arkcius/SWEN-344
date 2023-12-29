DROP TABLE IF EXISTS CHECKEDOUT;
DROP TABLE IF EXISTS LIBRARYINVENTORY;
DROP TABLE IF EXISTS USERS;
DROP TABLE IF EXISTS INVENTORY;
DROP TABLE IF EXISTS BTYPE;
DROP TABLE IF EXISTS LIBRARY;



CREATE TABLE USERS(
    userID SERIAL PRIMARY KEY,
    username VARCHAR(40),
    contact VARCHAR(40),
    active BOOLEAN DEFAULT CAST(1 as BOOLEAN)
);

INSERT INTO USERS(username,contact) VALUES('Ada Lovelace','ada@gmail.com');
INSERT INTO USERS(username,contact) VALUES('Mary Shelley','mary@gmail.com');
INSERT INTO USERS(username,contact) VALUES('Jackie Gleason','jackie@gmail.com');
INSERT INTO USERS(username,contact) VALUES('Art Garfunkel','art@gmail.com');

CREATE TABLE BTYPE(
    ID SERIAL PRIMARY KEY,
    types varchar(50)
);

INSERT INTO BTYPE(types) VALUES('Fiction');
INSERT INTO BTYPE(types) VALUES('Non-Fiction');

CREATE TABLE INVENTORY(
    bookID SERIAL PRIMARY KEY,
    title VARCHAR(100),
    author VARCHAR(100),
    publish CHAR(10),
    copies INTEGER,
    type INTEGER NOT NULL,
    subtype INTEGER,
    comments varchar(128),
    FOREIGN KEY (type) REFERENCES BTYPE(ID)
);

INSERT INTO INVENTORY(title,author,publish,copies,type) VALUES('Book1','Ry','09/10/2023',4,1);
INSERT INTO INVENTORY(title,author,publish,copies,type) VALUES('Kare','Ryl','09/10/2023',3,1);
INSERT INTO INVENTORY(title,author,publish,copies,type) VALUES('Book3','Ryan','09/10/2023',10,1);
INSERT INTO INVENTORY(title,author,publish,copies,type) VALUES('Book4','bob','09/10/2023',5,2);
INSERT INTO INVENTORY(title,author,publish,copies,type) VALUES('Book5','car','09/10/2023',6,2);
INSERT INTO INVENTORY(title,author,publish,copies,type) VALUES('Book','tim','09/10/2023',0,2);

CREATE TABLE LIBRARY(
    libID SERIAL PRIMARY KEY,
    libName varchar(50)
);

INSERT INTO LIBRARY(libName) VALUES('Towns of Penfield');
INSERT INTO LIBRARY(libName) VALUES('Fairport');
INSERT INTO LIBRARY(libName) VALUES('Henrietta');
INSERT INTO LIBRARY(libName) VALUES('Pittsford');

CREATE TABLE LIBRARYINVENTORY(
    IDlib int not null,
    IDbooks int not null,
    localcopies int,
    FOREIGN KEY (IDlib) REFERENCES LIBRARY(libID),
    FOREIGN KEY (IDbooks) REFERENCES INVENTORY(bookID)
);

INSERT INTO LIBRARYINVENTORY(IDlib,IDbooks,localcopies) VALUES(1,2,3);
INSERT INTO LIBRARYINVENTORY(IDlib,IDbooks,localcopies) VALUES(1,1,2);
INSERT INTO LIBRARYINVENTORY(IDlib,IDbooks,localcopies) VALUES(2,3,3);
INSERT INTO LIBRARYINVENTORY(IDlib,IDbooks,localcopies) VALUES(3,5,2);
INSERT INTO LIBRARYINVENTORY(IDlib,IDbooks,localcopies) VALUES(4,1,3);
INSERT INTO LIBRARYINVENTORY(IDlib,IDbooks,localcopies) VALUES(3,6,0);


CREATE TABLE CHECKEDOUT(
    IDuser INTEGER NOT NULL,
    IDbook INTEGER NOT NULL,
    IDlib INTEGER NOT NULL,
    outday DATE NOT NULL,
    returnday DATE,
    reserve BOOLEAN default CAST(0 as BOOLEAN),
    overdueday DATE,
    overdue BOOLEAN DEFAULT CAST(0 as BOOLEAN),
    fee FLOAT,
    FOREIGN KEY (IDuser) REFERENCES USERS(userID),
    FOREIGN KEY (IDbook) REFERENCES INVENTORY(bookID),
    FOREIGN KEY (IDlib) REFERENCES LIBRARY(libID)
);

INSERT INTO CHECKEDOUT(IDuser,IDbook,IDlib,outday,overdueday) VALUES(1,2,2,'09/10/2021','09/24/2021');
INSERT INTO CHECKEDOUT(IDuser,IDbook,IDlib,outday,overdueday) VALUES(1,1,1,'09/10/2041','09/24/2041');
INSERT INTO CHECKEDOUT(IDuser,IDbook,IDlib,outday,overdueday) VALUES(2,4,3,'09/10/2021','09/24/2021');
INSERT INTO CHECKEDOUT(IDuser,IDbook,IDlib,outday,overdueday,returnday) VALUES(3,5,4,'10/10/2023','10/24/2023','10/23/2023');
INSERT INTO CHECKEDOUT(IDuser,IDbook,IDlib,outday,overdueday,returnday) VALUES(3,2,2,'08/10/2021','08/24/2021','10/23/2021');
INSERT INTO CHECKEDOUT(IDuser,IDbook,IDlib,outday,overdueday) VALUES(3,6,1,'09/10/2023','09/24/2023');

