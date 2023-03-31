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
    customer_id INT NOT NULL,
    invoice_date DATETIME NOT NULL,
		CONSTRAINT invoice_customer_fk FOREIGN KEY(customer_id) REFERENCES customers(customer_id)
	);

DROP TABLE IF EXISTS invoice_products;

CREATE TABLE invoice_products (
	invoice_id INT,
    product_id INT,
    product_quantity INT,
    		CONSTRAINT invoice_prod_invoice_fk FOREIGN KEY(invoice_id) REFERENCES invoices(invoice_id),
			CONSTRAINT invoice_prod_product_fk FOREIGN KEY(product_id) REFERENCES products(product_id));

INSERT INTO vendors(vendor_name, vendor_address, vendor_city, vendor_zip_code, vendor_phone) VALUES ("Blu Team", "12 Sample Street", "Florida", "A1E3K1", "(867)728-1283");

INSERT INTO vendors(vendor_name, vendor_address, vendor_city, vendor_zip_code, vendor_phone) VALUES ("Red Team", "22 Jump Street", "Ohio", "J7A8M4", "(198)826-1392");

INSERT INTO customers(customer_first_name, customer_last_name, customer_phone, customer_email, customer_address) VALUES ("John", "Doe", "(183)472-1876", "johnd@gmail.com", "76 New Road");

INSERT INTO customers(customer_first_name, customer_last_name, customer_phone, customer_email, customer_address) VALUES ("Jane", "Dame", "(917)296-1976", "janed@gmail.com", "99 Saxon Turn");

INSERT INTO products(vendor_id, product_name, product_description, inventory_stock, price) VALUES (1, "Risk", "Classic Board Game", 55, 17.99);

INSERT INTO products(vendor_id, product_name, product_description, inventory_stock, price) VALUES (2, "Scrabble", "Family Board Game", 24, 18.99);

INSERT INTO invoices(customer_id, invoice_date) VALUES (1, '2021-02-11 12:18:44'); 

INSERT INTO invoices(customer_id, invoice_date) VALUES (2, '2022-07-09 06:11:32');

INSERT INTO invoice_products VALUES (1, 1, 12);

INSERT INTO invoice_products VALUES (1, 2, 5);

INSERT INTO invoice_products VALUES (2, 1, 3);

INSERT INTO invoice_products VALUES (2, 2, 6);

SELECT * FROM invoices;

SELECT * FROM products;

SELECT * FROM customers;

SELECT * FROM vendors;

SELECT * FROM invoice_products;

SELECT ip.invoice_id AS 'Invoice ID', SUM(ip.product_quantity * p.price) AS 'Total Cost' FROM invoice_products AS ip JOIN products AS p ON ip.product_id = p.product_id GROUP BY ip.invoice_id;