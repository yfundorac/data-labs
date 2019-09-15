CREATE DATABASE lab_mysql;
USE lab_mysql;
CREATE TABLE cars (
  id INTEGER AUTO_INCREMENT PRIMARY KEY,
  vin VARCHAR(17) NOT NULL,
  manufacturer VARCHAR (45) NOT NULL,
  model VARCHAR(30) NOT NULL,
  year integer NOT NULL,
  color VARCHAR(30) NOT NULL
);

CREATE TABLE customers (
  id INTEGER AUTO_INCREMENT PRIMARY KEY,
  customer_id integer(5) NOT NULL,
  name VARCHAR (45) NOT NULL,
  phone VARCHAR(30) NOT NULL,
  email VARCHAR(45),
  address VARCHAR(50) NOT NULL,
  city VARCHAR(50) NOT NULL,
  state VARCHAR(50) NOT NULL,
  country VARCHAR(50) NOT NULL,
  zip integer
);

CREATE TABLE salespersons (
  id INTEGER AUTO_INCREMENT PRIMARY KEY,
  staff_id integer(5) NOT NULL,
  name VARCHAR (45) NOT NULL,
  store VARCHAR(30)
);

CREATE TABLE invoices (
  id INTEGER AUTO_INCREMENT PRIMARY KEY,
  invoice_number integer(9) NOT NULL,
  date date NOT NULL,
  car_id integer NOT NULL,
  customer_id integer NOT NULL,
  salesperson_id integer NOT NULL
);