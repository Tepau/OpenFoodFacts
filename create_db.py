import mysql
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="********"
)
mycursor = mydb.cursor()

mycursor.execute("""DROP DATABASE IF EXISTS appli""")

mycursor.execute("""CREATE DATABASE appli""")

mycursor.execute("""use appli""")


mycursor.execute(""" CREATE TABLE Product (
	id SMALLINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
	code BIGINT UNSIGNED NOT NULL UNIQUE,
	product_name_fr VARCHAR(150) NOT NULL ,
	nutrition_grade_fr CHAR(1) NOT NULL,
	url VARCHAR(400),
	generic_name_fr VARCHAR(200)
	)""")


mycursor.execute("""CREATE TABLE Category (
	id SMALLINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
	category_name VARCHAR(150) UNIQUE
	)""")


mycursor.execute(""" CREATE TABLE Store (
	id SMALLINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
	store_name VARCHAR(150) UNIQUE NOT NULL
	)""")

mycursor.execute("""CREATE TABLE Store_product(
	id SMALLINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
	product_id BIGINT UNSIGNED NOT NULL,
	store_id SMALLINT UNSIGNED,
	CONSTRAINT fk_store_id
		FOREIGN KEY (store_id)
		REFERENCES Store (id),
	CONSTRAINT fk_product_id
		FOREIGN KEY (product_id)
		REFERENCES Product (code)
	)""")
	

mycursor.execute("""CREATE TABLE Category_product(
	id SMALLINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
	product_id BIGINT UNSIGNED NOT NULL,
	category_id SMALLINT UNSIGNED,
	CONSTRAINT fk_product_id_id
		FOREIGN KEY (product_id)
		REFERENCES Product(code),
	CONSTRAINT fk_category_id
		FOREIGN KEY (category_id)
		REFERENCES Category (id)
	)""")

mycursor.execute(""" CREATE TABLE Favorite (
	product_id BIGINT UNSIGNED NOT NULL,
	substitute_id BIGINT UNSIGNED NOT NULL,
	date_heure DATETIME,
	pseudo VARCHAR(30) NOT NULL,
	PRIMARY KEY(product_id,substitute_id, pseudo),
	CONSTRAINT fk_product_id_code
		FOREIGN KEY (product_id)
		REFERENCES Product(code),
	CONSTRAINT fk_substitute_id_code
		FOREIGN KEY (substitute_id)
		REFERENCES Product(code)
	)""")
mydb.commit()