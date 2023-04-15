from sql_functions import executeQueryAndCommit, executeQueryAndReturnResult, executeQueryAndReturnResultNoColumnName

"""Functions that return results. Numbering Lines 7-45. IMPORTANT NOTE: All members contributed to this code, my name will only be on most functions 
because I was the one who sorted them within this file after they were created"""


def get_customer_by_name(customer_full_name):
    """
    Retrieves customer information using their full name
    :param customer_full_name: (str) Full name of the customer
    :return: (tuple) A tuple containing the column headers of the customers table
        as the first element and a list of rows as the second element
    """
    sql = f"SELECT * FROM customers WHERE CONCAT(customer_first_name, ' ', customer_last_name) = '{customer_full_name}';"
    return executeQueryAndReturnResult(sql)


def get_customer_id_by_customer_name(customer_first_name, customer_last_name):
    """
    Retrieves the customer id by their first and last name
    :param customer_first_name: (str) First name of the customer
    :param customer_last_name: (str) Last name of the customer
    :return: (str) The customer id of the matching customer
    """
    sql = f"SELECT customer_id FROM pgp.customers WHERE customer_first_name = '{customer_first_name}' and customer_last_name = '{customer_last_name}';"
    query = str(executeQueryAndReturnResultNoColumnName(sql)[0])
    return query[1]


def get_customer_names():
    """
    Retrieves the full names of all customers
    :return: (tuple) A tuple containing the column header 'customer_full_name'
        as the first element and a list of rows as the second element
    """
    sql = f"SELECT concat(customer_first_name,' ', customer_last_name) as customer_full_name FROM pgp.customers;"
    return executeQueryAndReturnResult(sql)


def get_product_names():
    """
    Retrieves the names of all products
    :return: (tuple) A tuple containing the column header 'product_name'
        as the first element and a list of rows as the second element
    """
    sql = f"SELECT product_name FROM pgp.products;"
    return executeQueryAndReturnResult(sql)


def get_price_with_product_name(product_name):
    """
    Retrieves the price of a product by its name
    :param product_name: (str) Name of the product
    :return: (str) The price of the product
    """
    sql = f"SELECT price FROM pgp.products WHERE product_name = '{product_name}';"
    query = str(executeQueryAndReturnResultNoColumnName(sql))
    return query


def get_most_recent_invoice_id_by_date():
    """
    Retrieves the invoice id of the most recent invoice based on invoice date
    :return: (int) The invoice id of the most recent invoice
    """
    sql = f"SELECT invoice_id FROM invoices ORDER BY invoice_date DESC LIMIT 1;"
    return executeQueryAndReturnResultNoColumnName(sql)[0][0]


def get_customers_last_month():
    """
    Retrieves a list of customers who have had activity within the last month, including their customer ID,
    first name, last name, and date of their last activity.
    :return: (tuple) A tuple containing the columns 'CustomerID', 'First Name', 'Last Name', and 'Date of Last Activity'
        as the first element and a list of rows as the second element
    """
    sql = f"SELECT customers.customer_id AS 'Customer ID', customer_first_name AS 'First Name', customer_last_name AS 'Last Name', Max(invoice_date) AS 'Date of Last Activity' FROM customers JOIN invoices ON customers.customer_id = invoices.customer_id GROUP BY customers.customer_id, customer_first_name HAVING MAX(invoice_date) > NOW() - INTERVAL 1 MONTH;"
    return executeQueryAndReturnResult(sql)


def get_product_id(product_choice):
    """
    Retrieves the product ID of a given product name.
    :param: product_choice: (str) The name of the product to retrieve the ID for
    :return: (int) The product ID of the given product name
    """
    sql = f"SELECT product_id FROM pgp.products WHERE product_name = '{product_choice}';"
    query = executeQueryAndReturnResultNoColumnName(sql)[0][0]
    return query


def get_invoice_by_customer_id(customer_id):
    """
    Retrieves a list of invoices and their total cost for a given customer ID.
    :param customer_id: (int) The customer ID to retrieve invoices for
    :return: (tuple) A tuple containing the column headers 'Invoice ID' and 'Total Cost' as the first element and a list
                     of rows as the second element
    """
    sql = f"SELECT ip.invoice_id AS 'Invoice ID', SUM(ip.product_quantity * p.price) AS 'Total Cost' FROM invoice_products AS ip JOIN products AS p ON ip.product_id = p.product_id JOIN invoices AS i ON ip.invoice_id = i.invoice_id WHERE i.customer_id = {customer_id} GROUP BY ip.invoice_id;"
    return executeQueryAndReturnResult(sql)


def get_product_by_id(product_id):
    """
    Retrieves information about a product given its ID, including the product name, description, current inventory stock, and price.
    :param product_id: (int) The ID of the product to retrieve information for
    :return: (tuple) A tuple containing the column headers 'product_name', 'product_description', 'inventory_stock', and
                     'price' as the first element and a list of rows as the second element
    """
    sql = f"SELECT product_name, product_description, inventory_stock, price FROM products WHERE product_id = {product_id};"
    return executeQueryAndReturnResult(sql)


def get_product_quantity_by_id(product_id):
    """
    Retrieves the current inventory stock of a product given its ID.
    :param: product_id: (int) The ID of the product to retrieve inventory stock for
    :return: (list) A list of tuples containing the product ID and inventory stock level
    """
    sql = f"SELECT product_id, inventory_stock FROM pgp.products WHERE product_id = {product_id};"
    return executeQueryAndReturnResultNoColumnName(sql)


def generate_finished_invoice(invoice_id):
    """
    Generates a finished invoice for a given invoice ID, including each product in the invoice, its price per unit,
    quantity ordered, and total cost.
    :param invoice_id: (int) The ID of the invoice to generate the finished invoice for
    :return: (tuple) A tuple containing the column headers 'Product', 'Price Per Unit', 'Quantity', and
                     'Total Per Product' as the first element and a list of rows as the second element
    """
    sql = f"SELECT p.product_name AS 'Product',p.price AS 'Price Per Unit',ip.product_quantity AS 'Quantity',(p.price * ip.product_quantity) AS 'Total Per Product' FROM products AS p JOIN invoice_products AS ip ON p.product_id = ip.product_id WHERE ip.invoice_id = {invoice_id} UNION ALL SELECT 'Total', " ", " f", SUM(p.price * ip.product_quantity) FROM products AS p JOIN invoice_products AS ip ON p.product_id = ip.product_id WHERE ip.invoice_id = {invoice_id};"
    return executeQueryAndReturnResult(sql)


def show_products():
    """
    Retrieves information about all products in the database, including the product ID, name, description,
    current inventory stock, and price.
    :return: (tuple) A tuple containing all column headers in the 'products' table as the first element and a
    list of rows as the second element
    """
    sql = "SELECT product_id AS 'Product ID', vendor_id AS 'Vendor ID', product_name AS 'Product Name', product_description AS 'Product Description', inventory_stock AS 'Inventory Stock', price AS 'Price' FROM pgp.products;"
    return executeQueryAndReturnResult(sql)


def show_out_of_stock_products():
    """
    Retrieves information about all products in the database that are out of stock, including the product ID, name,
    description, current inventory stock, and price.
    :return: (tuple) A tuple containing all column headers in the 'products' table where inventory stock is less than 1
     as the first element and a list of rows as the second element
    """
    sql = "SELECT product_id AS 'Product ID', vendor_id AS 'Vendor ID', product_name AS 'Product Name', product_description AS 'Product Description', inventory_stock AS 'Inventory Stock', price AS 'Price' FROM pgp.products WHERE inventory_stock < 1;"
    return executeQueryAndReturnResult(sql)


def show_current_invoice(invoice_id):
    """
    Retrieves information about all products in a given invoice, including the product name, description, quantity
    ordered, and price.
    :param invoice_id: (int) The ID of the invoice to retrieve product information for
    :return: (tuple) A tuple containing the column headers 'product_name', 'product_description', 'product_quantity',
                     and 'price' as the first element and a list of rows as the second element
    """
    sql = f"SELECT product_name AS 'Product Name', product_description AS 'Product Description', product_quantity AS 'Product Quantity', price AS 'Price' FROM invoice_products ip JOIN products p ON ip.product_id = p.product_id WHERE invoice_id = {invoice_id};"
    return executeQueryAndReturnResult(sql)


def get_current_invoice_total(invoice_id):
    """
    Retrieves total price of the current invoice
    :param invoice_id: (int) The ID of the invoice to retrieve price information for
    :return: (float) sum of the price of all invoice products multiplied by their quantity
    """
    sql = f"SELECT SUM(price * product_quantity) AS 'Total Price' FROM invoice_products ip JOIN products p ON ip.product_id = p.product_id WHERE invoice_id = {invoice_id};"
    return executeQueryAndReturnResultNoColumnName(sql)[0][0]


def get_current_invoice_quantity(invoice_id):
    """
        Retrieves total quantity of the current invoice
        :param invoice_id: (int) The ID of the invoice to retrieve price information for
        :return: (int) sum of the quantity of all invoice products
        """
    sql = f"SELECT SUM(product_quantity) AS 'Total Quantity' FROM invoice_products ip JOIN products p ON ip.product_id = p.product_id WHERE invoice_id = {invoice_id};"
    return executeQueryAndReturnResultNoColumnName(sql)[0][0]


def search_invoice_by_customer_id(customer_id):
    """
    Searches for invoices based on the given customer ID
    :param customer_id: (int) The customer ID to search invoices for
    :return: (tuple) A tuple containing the column headers 'Invoice ID' and 'Total Cost' as the first element and a
                     list of rows as the second element
    """
    sql = f"SELECT ip.invoice_id AS 'Invoice ID', SUM(ip.product_quantity * p.price) AS 'Total Cost' FROM invoice_products AS ip JOIN products AS p ON ip.product_id = p.product_id JOIN invoices AS i ON ip.invoice_id = i.invoice_id WHERE i.customer_id = {customer_id} GROUP BY ip.invoice_id;"
    return executeQueryAndReturnResult(sql)


def check_if_invoice_product_exists(invoice_id, product_id):
    """
    Checks if a product exists in a given invoice
    :param invoice_id: (int) The ID of the invoice to check
    :param product_id: (int) The ID of the product to check
    :return: (bool) True if the product exists in the given invoice, False otherwise
    """
    sql = f"SELECT * FROM pgp.invoice_products WHERE invoice_id = {invoice_id} AND product_id = {product_id}"
    res = executeQueryAndReturnResultNoColumnName(sql)
    if len(res) >= 1:
        return True
    else:
        return False


def total_cost_breakdown_and_products_per_invoice():
    """
    Retrieves the total cost breakdown and product information for each invoice
    :return: (tuple) A tuple containing the column headers 'Invoice ID', 'Total Cost', 'Cost Per Product',
                     'ID Numbers of Products Included' and 'Quantity of Products' as the first element and a
                     list of rows as the second element
    """
    sql = f"SELECT ip.invoice_id AS 'Invoice ID',SUM(ip.product_quantity * p.price) AS 'Total Cost', GROUP_CONCAT(ip.product_quantity * p.price) AS 'Cost Per Product', GROUP_CONCAT(p.product_id) AS 'ID Numbers of Products Included', GROUP_CONCAT(ip.product_quantity) AS 'Quantity of Products' FROM invoice_products AS ip JOIN products AS p ON ip.product_id = p.product_id JOIN invoices AS i ON ip.invoice_id = i.customer_id GROUP BY ip.invoice_id;"
    return executeQueryAndReturnResult(sql)


"""Functions that commit changes to the database. Numbering lines 53-70"""


def add_invoice(customer_id, invoice_date):
    """
    Adds a new invoice to the database
    :param customer_id: (int) The ID of the customer who made the purchase
    :param invoice_date: (date) The date of the purchase
    :return: (int) Count of affected rows
    """
    sql = f"INSERT INTO pgp.invoices VALUES (DEFAULT, {customer_id}, {invoice_date});"
    return executeQueryAndCommit(sql)


def add_customer(customer_first_name, customer_last_name, customer_phone, customer_email, customer_address):
    """
    Adds a new customer to the database
    :param customer_first_name: (str) The first name of the customer
    :param customer_last_name: (str) The last name of the customer
    :param customer_phone: (str) The phone number of the customer
    :param customer_email: (str) The email address of the customer
    :param customer_address: (str) The address of the customer
    :return: (int) Count of affected rows
    """
    sql = f"INSERT INTO pgp.customers VALUES (DEFAULT, '{customer_first_name}', '{customer_last_name}', '{customer_phone}', '{customer_email}', '{customer_address}');"
    return executeQueryAndCommit(sql)


def add_customer_id_to_invoices(customer_id):
    """
    Adds a customer based on an id to the invoices table
    :param customer_id: (int) The ID of the customer to add to the invoice
    :return: (int) Count of affected rows
    """
    sql = f"INSERT INTO invoices(customer_id, invoice_date) VALUES ({customer_id}, now());"
    return executeQueryAndCommit(sql)


def add_product_to_invoice_products(invoice_id, product_choice, quantity):
    """
    Adds a product and its quantity to an invoice in the database
    :param invoice_id: (int) The ID of the invoice to add the product to
    :param product_choice: (int) The ID of the product being added
    :param quantity: (int) The quantity of the product being added
    :return: (int) Count of affected rows
    """
    sql = f"INSERT INTO invoice_products(invoice_id,product_id,product_quantity) VALUES ({invoice_id},{product_choice}, {quantity});"
    return executeQueryAndCommit(sql)


def increase_inventory(intake_amount, product_id):
    """
    Increases the inventory stock of a product in the database
    :param intake_amount: (int) The amount to increase the inventory stock by
    :param product_id: (int) The ID of the product to increase the inventory stock of
    :return: (int) Count of affected rows
    """
    sql = f"UPDATE pgp.products SET inventory_stock = inventory_stock + {intake_amount} WHERE product_id = {product_id};"
    return executeQueryAndCommit(sql)


def increase_invoice_product_inventory(intake_amount, invoice_id, product_id):
    """
    Increases the inventory stock of a product in an invoice in the database
    :param intake_amount: (int) The amount to increase the inventory stock by
    :param invoice_id: (int) The ID of the invoice containing the product to increase the inventory stock of
    :param product_id: (int) The ID of the product to increase the inventory stock of
    :return: (int) Count of affected rows
    """
    sql = f"UPDATE pgp.invoice_products SET product_quantity = product_quantity + {intake_amount} WHERE invoice_id = {invoice_id} AND product_id = {product_id};"
    return executeQueryAndCommit(sql)


def decrease_inventory(purchase_amount, product_id):
    """
    Decreases the inventory stock of a product in the database
    :param purchase_amount: (int) The amount to decrease the inventory stock by
    :param product_id: (int) The ID of the product to decrease the inventory stock of
    :return: (int) Count of affected rows
    """
    sql = f"UPDATE pgp.products SET inventory_stock = inventory_stock - {purchase_amount} WHERE product_id = {product_id};"
    return executeQueryAndCommit(sql)
