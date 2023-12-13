-- Creates a database 'hbtn_0d_usa'
-- Creates a table states
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (
	id INT UNIQUE AUTO_INCREMENT NOT NULL,
	name VARCHAR(256),
	PRIMARY KEY (id)
);
