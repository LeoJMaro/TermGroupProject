
DROP DATABASE IF EXISTS pgp;

CREATE DATABASE pgp;

USE pgp;

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
INSERT INTO vendors(vendor_name, vendor_address, vendor_city, vendor_zip_code, vendor_phone) VALUES ("Red Team", "22 Jump Street", "Ohio", "J7A8M4", "(198)826-1392");INSERT INTO vendors(vendor_name, vendor_address, vendor_city, vendor_zip_code, vendor_phone) VALUES ("Green Team", "34 Elm Street", "California", "H3C9B7", "(986)756-1245");
INSERT INTO vendors(vendor_name, vendor_address, vendor_city, vendor_zip_code, vendor_phone) VALUES ("Yellow Team", "56 Park Avenue", "Texas", "F8R6N2", "(463)251-7309");
INSERT INTO vendors(vendor_name, vendor_address, vendor_city, vendor_zip_code, vendor_phone) VALUES ("Purple Team", "78 Cedar Street", "New York", "D5P2M8", "(574)316-0285");
INSERT INTO vendors(vendor_name, vendor_address, vendor_city, vendor_zip_code, vendor_phone) VALUES ("Orange Team", "90 Maple Road", "Arizona", "K2B4H9", "(801)947-1647");
INSERT INTO vendors(vendor_name, vendor_address, vendor_city, vendor_zip_code, vendor_phone) VALUES ("Silver Team", "44 Diamond Street", "Illinois", "L3T7A1", "(287)715-9504");
INSERT INTO vendors(vendor_name, vendor_address, vendor_city, vendor_zip_code, vendor_phone) VALUES ("Gold Team", "32 Platinum Lane", "Kansas", "G7E6P3", "(152)034-7891");
INSERT INTO vendors(vendor_name, vendor_address, vendor_city, vendor_zip_code, vendor_phone) VALUES ("Green Team", "123 Main St", "California", "90210", "(555)555-5555");
INSERT INTO vendors(vendor_name, vendor_address, vendor_city, vendor_zip_code, vendor_phone) VALUES ("Violet Team", "456 Old Road", "Boston", "J2Z8M3", "(123)456-7890");
INSERT INTO vendors(vendor_name, vendor_address, vendor_city, vendor_zip_code, vendor_phone) VALUES ("Indigo Team", "65 Hangmans Way", "Alaska", "G3V8K1", "(555)555-5555");

INSERT INTO customers(customer_first_name, customer_last_name, customer_phone, customer_email, customer_address) VALUES ("John", "Doe", "(183)472-1876", "johnd@gmail.com", "76 New Road");
INSERT INTO customers(customer_first_name, customer_last_name, customer_phone, customer_email, customer_address) VALUES ("Jane", "Dame", "(917)296-1976", "janed@gmail.com", "99 Saxon Turn");
INSERT INTO customers(customer_first_name, customer_last_name, customer_phone, customer_email, customer_address) VALUES ("Emily", "Smith", "(617)555-1212", "emily.smith@example.com", "123 Main St");
INSERT INTO customers(customer_first_name, customer_last_name, customer_phone, customer_email, customer_address) VALUES ("James", "Brown", "(212)555-1212", "james.brown@example.com", "456 Oak St");
INSERT INTO customers(customer_first_name, customer_last_name, customer_phone, customer_email, customer_address) VALUES ("Maggie", "Johnson", "(415)555-1212", "maggie.johnson@example.com", "789 Elm St");
INSERT INTO customers(customer_first_name, customer_last_name, customer_phone, customer_email, customer_address) VALUES ("Henry", "Lee", "(312)555-1212", "henry.lee@example.com", "555 Maple St");
INSERT INTO customers(customer_first_name, customer_last_name, customer_phone, customer_email, customer_address) VALUES ("Sophia", "Davis", "(202)555-1212", "sophia.davis@example.com", "321 Pine St");
INSERT INTO customers(customer_first_name, customer_last_name, customer_phone, customer_email, customer_address) VALUES ("Michael", "Wilson", "(404)555-1212", "michael.wilson@example.com", "234 Cedar St");
INSERT INTO customers(customer_first_name, customer_last_name, customer_phone, customer_email, customer_address) VALUES ("Lily", "Chen", "(305)555-1212", "lily.chen@example.com", "987 Birch St");
INSERT INTO customers(customer_first_name, customer_last_name, customer_phone, customer_email, customer_address) VALUES ("William", "Kim", "(214)555-1212", "william.kim@example.com", "567 Walnut St");

INSERT INTO products(vendor_id, product_name, product_description, inventory_stock, price) VALUES (1, "Risk", "Classic Board Game", 55, 17.99);
INSERT INTO products(vendor_id, product_name, product_description, inventory_stock, price) VALUES (2, "Scrabble", "Family Board Game", 24, 18.99);
INSERT INTO products(vendor_id, product_name, product_description, inventory_stock, price) VALUES (3, "Sorry", "Board Game", 40, 24.99);
INSERT INTO products(vendor_id, product_name, product_description, inventory_stock, price) VALUES (4, "Uno", "Card Game", 0, 7.99);
INSERT INTO products(vendor_id, product_name, product_description, inventory_stock, price) VALUES (5, "Chess Set", "Wooden Board Game", 10, 39.99);
INSERT INTO products(vendor_id, product_name, product_description, inventory_stock, price) VALUES (6, "Jenga", "Wooden Block Game", 30, 14.99);
INSERT INTO products(vendor_id, product_name, product_description, inventory_stock, price) VALUES (7, "Pictionary", "Drawing Game", 0, 21.99);
INSERT INTO products(vendor_id, product_name, product_description, inventory_stock, price) VALUES (8, "Battleship", "Naval Board Game", 15, 16.99);
INSERT INTO products(vendor_id, product_name, product_description, inventory_stock, price) VALUES (9, "Checkers", "Tabletop Board Game", 0, 12.99);


INSERT INTO invoices(customer_id, invoice_date) VALUES (1, '2021-02-11 12:18:44'); 
INSERT INTO invoices(customer_id, invoice_date) VALUES (1, '2022-03-01 08:32:15');
INSERT INTO invoices(customer_id, invoice_date) VALUES (2, '2022-04-15 12:47:22');
INSERT INTO invoices(customer_id, invoice_date) VALUES (3, '2022-05-23 14:15:03');
INSERT INTO invoices(customer_id, invoice_date) VALUES (4, '2022-06-30 09:20:41');
INSERT INTO invoices(customer_id, invoice_date) VALUES (5, '2022-07-18 16:55:08');
INSERT INTO invoices(customer_id, invoice_date) VALUES (6, '2022-08-05 10:10:10');
INSERT INTO invoices(customer_id, invoice_date) VALUES (7, '2022-09-22 13:27:47');
INSERT INTO invoices(customer_id, invoice_date) VALUES (8, '2022-10-11 15:40:22');
INSERT INTO invoices(customer_id, invoice_date) VALUES (2, '2022-07-09 06:11:32');

INSERT INTO invoice_products VALUES (1, 1, 12);

INSERT INTO invoice_products VALUES (1, 2, 5);

INSERT INTO invoice_products VALUES (2, 1, 3);

INSERT INTO invoice_products VALUES (2, 2, 6);
INSERT INTO invoice_products VALUES (3, 1, 2);
INSERT INTO invoice_products VALUES (5, 9, 14);
INSERT INTO invoice_products VALUES (2, 5, 9);
INSERT INTO invoice_products VALUES (7, 4, 10);
INSERT INTO invoice_products VALUES (6, 9, 6);
INSERT INTO invoice_products VALUES (4, 7, 2);
INSERT INTO invoice_products VALUES (10, 3, 3);



SELECT * FROM vendors;
SELECT * FROM invoices;
SELECT * FROM customers;
SELECT * FROM products;
SELECT * FROM invoice_products;

SELECT 
    ip.invoice_id AS 'Invoice ID',
    SUM(ip.product_quantity * p.price) AS 'Total Cost', GROUP_CONCAT(ip.product_quantity * p.price) AS "Cost Per Product", GROUP_CONCAT(p.product_id) AS 'ID Numbers of Products Included', GROUP_CONCAT(ip.product_quantity) AS "Quantity of Products"
FROM
    invoice_products AS ip
		JOIN
    products AS p ON ip.product_id = p.product_id
		JOIN
	invoices AS i ON ip.invoice_id = i.invoice_id
GROUP BY ip.invoice_id;

SELECT 
    ip.invoice_id AS 'Invoice ID',
    SUM(ip.product_quantity * p.price) AS 'Cost of Selected Product'
FROM
    invoice_products AS ip
		JOIN
    products AS p ON ip.product_id = p.product_id
		JOIN
	invoices AS i ON ip.invoice_id = i.invoice_id
    WHERE p.product_id = 1
GROUP BY ip.invoice_id;

SELECT 
    ip.invoice_id AS 'Invoice ID',
    SUM(ip.product_quantity * p.price) AS 'Total Cost'
FROM
    invoice_products AS ip
        JOIN
    products AS p ON ip.product_id = p.product_id
        JOIN
    invoices AS i ON ip.invoice_id = i.invoice_id
WHERE
    i.customer_id = 1
GROUP BY ip.invoice_id;

SELECT 
    p.product_name AS 'Product',
    p.price AS 'Price Per Unit',
    ip.product_quantity AS 'Quantity',
    (p.price * ip.product_quantity) AS 'Total Per Product'
FROM
    products AS p
        JOIN
    invoice_products AS ip ON p.product_id = ip.product_id
WHERE
    ip.invoice_id = 2 
UNION ALL SELECT 
    'Total', " ", " ", SUM(p.price * ip.product_quantity)
FROM
    products AS p
        JOIN
    invoice_products AS ip ON p.product_id = ip.product_id
WHERE
    ip.invoice_id = 2;
