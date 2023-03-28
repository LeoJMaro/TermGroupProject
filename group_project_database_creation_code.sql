DROP DATABASE IF EXISTS programming_group_project;

CREATE DATABASE programming_group_project;

USE programming_group_project;

DROP TABLE IF EXISTS vendors;

CREATE TABLE vendors (
	vendor_id INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL,
    vendor_name VARCHAR(45) NOT NULL,
    vendor_address VARCHAR(50) NOT NULL,
    vendor_city VARCHAR(45) NOT NULL,
    vendor_zip_code VARCHAR(20) NOT NULL,
    vendor_phone VARCHAR(15) NOT NULL
	);

DROP TABLE IF EXISTS products;

CREATE TABLE products (
	product_id INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL,
    vendor_id INT NOT NULL,
    product_name VARCHAR(45) NOT NULL,
    product_description VARCHAR(100) NOT NULL,
    inventory_stock INT NOT NULL,
    price DECIMAL(9,2) NOT NULL,
		CONSTRAINT vendor_product_relationship FOREIGN KEY(vendor_id) REFERENCES vendors(vendor_id)
	);

DROP TABLE IF EXISTS customers;

CREATE TABLE customers (
	customer_id INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL,
    customer_first_name VARCHAR(45) NOT NULL,
    customer_last_name VARCHAR(45) NOT NULL,
    customer_phone VARCHAR(15) NOT NULL,
    customer_email VARCHAR(45) NOT NULL,
    customer_address VARCHAR(45)
    );

DROP TABLE IF EXISTS invoices;

CREATE TABLE invoices (
	invoice_id INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL,
    vendor_id INT NOT NULL,
    invoice_number VARCHAR(45),
    invoice_date DATE NOT NULL,
    invoice_total DECIMAL(9,2) NOT NULL,
    payment_total DECIMAL(9,2) NOT NULL,
    invoice_due_date DATE NOT NULL,
    payment_date DATE NOT NULL,
		CONSTRAINT invoice_vendor_fk FOREIGN KEY(vendor_id) REFERENCES vendors(vendor_id)
	);

