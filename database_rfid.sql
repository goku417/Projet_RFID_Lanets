CREATE TABLE Benevoles (
ID int NOT NULL AUTO_INCREMENT,
Prenom varchar(255) NOT NULL,
Nom varchar(255) NOT NULL,
rfid varchar(255) NOT NULL,
UNIQUE (ID),
PRIMARY KEY (rfid)
);

CREATE TABLE Admins(
ID int NOT NULL AUTO_INCREMENT,
username varchar(255),
password varchar(255),
PRIMARY KEY (ID)
);

CREATE TABLE Horaires(
Debut varchar(255),
Fin varchar(255),
user_rfid varchar(255)
);
