from sql_functions import executeQueryAndCommit, executeQueryAndReturnResult, executeQueryAndReturnResultNOCOLUMNNAME


def add_invoice(customer_id, invoice_date):
    sql = f"INSERT INTO pgp.invoices VALUES (DEFAULT, {customer_id}, {invoice_date});"

    return executeQueryAndCommit(sql)


def add_to_invoices_with_customer_name(customer_name, product_name):
    sql = f"INSERT INTO programming_group_project.invoices VALUES (default, {vendor_id}, '{invoice_number}', {invoice_date}, {invoice_total}, {payment_total}, {invoice_due_date}, {payment_date});"
    return executeQueryAndCommit(sql)


def add_customer(customer_first_name, customer_last_name, customer_phone, customer_email, customer_address):
    sql = f"INSERT INTO pgp.customers VALUES (DEFAULT, '{customer_first_name}', '{customer_last_name}', '{customer_phone}', '{customer_email}', '{customer_address}');"
    return executeQueryAndCommit(sql)


def get_customer_by_name(customer_full_name):
    sql = f"SELECT * FROM customers WHERE CONCAT(customer_first_name, ' ', customer_last_name) = '{customer_full_name}';"
    return executeQueryAndReturnResult(sql)


def get_customer_id_by_customer_name(customer_first_name, customer_last_name):
    sql = f"SELECT customer_id FROM pgp.customers WHERE customer_first_name = '{customer_first_name}' and customer_last_name = '{customer_last_name}';"
    query = str(executeQueryAndReturnResultNOCOLUMNNAME(sql)[0])
    return query[1]


def get_customer_names():
    sql = f"SELECT concat(customer_first_name,' ', customer_last_name) as customer_full_name FROM pgp.customers;"
    return executeQueryAndReturnResult(sql)


def get_product_names():
    sql = f"SELECT product_name FROM pgp.products;"
    return executeQueryAndReturnResult(sql)


def get_price_with_product_name(product_name):
    sql = f"SELECT price FROM pgp.products WHERE product_name = '{product_name}';"
    query = str(executeQueryAndReturnResultNOCOLUMNNAME(sql))
    # print(query[11:16])
    return query


def add_customer_id_to_invoices(customer_id):
    sql = f"INSERT INTO invoices(customer_id, invoice_date) VALUES ({customer_id}, now());"
    return executeQueryAndCommit(sql)


def get_most_recent_invoice_id_by_date():
    sql = f"SELECT invoice_id FROM invoices ORDER BY invoice_date DESC LIMIT 1;"
    return executeQueryAndReturnResultNOCOLUMNNAME(sql)[0][0]


def add_product_to_invoice_products(invoice_id, product_choice, quantity):
    sql = f"INSERT INTO invoice_products(invoice_id,product_id,product_quantity) VALUES ({invoice_id},{product_choice}, {quantity});"
    return executeQueryAndCommit(sql)


def get_product_id(product_choice):
    sql = f"SELECT product_id FROM pgp.products WHERE product_name = '{product_choice}';"
    query = executeQueryAndReturnResultNOCOLUMNNAME(sql)[0][0]
    return query


# print(get_product_id("Risk"))


def increase_inventory(intake_amount, product_id):
    sql = f"UPDATE pgp.products SET inventory_stock = inventory_stock + {intake_amount} WHERE product_id = {product_id};"
    return executeQueryAndCommit(sql)

def increase_invoice_product_inventory(intake_amount,invoice_id, product_id):
    sql = f"UPDATE pgp.invoice_products SET product_quantity = product_quantity + {intake_amount} WHERE invoice_id = {invoice_id} AND product_id = {product_id};"
    return executeQueryAndCommit(sql)


def decrease_inventory(purchase_amount, product_id):
    sql = f"UPDATE programming_group_project.products SET inventory_stock = inventory_stock - {purchase_amount} WHERE product_id = {product_id};"
    return executeQueryAndCommit(sql)


def get_product_by_id(product_id):
    sql = f"SELECT product_name, product_description, inventory_stock, price FROM products WHERE product_id = {product_id};"
    return executeQueryAndReturnResult(sql)


def show_products():
    sql = "SELECT * FROM products"
    return executeQueryAndReturnResult(sql)


def get_customer_by_name(customer_full_name):
    sql = f"SELECT * FROM customers WHERE CONCAT(customer_first_name, ' ', customer_last_name) = '{customer_full_name}';"
    return executeQueryAndReturnResult(sql)


# def get_most_recent_invoice_id_by_date():
#   sql = f"SELECT invoice_id FROM invoices ORDER BY invoice_date DESC LIMIT 1;"
#   return executeQueryAndReturnResult(sql)

def check_if_invoice_product_exists(invoice_id, product_id):
    sql = f"SELECT * FROM pgp.invoice_products WHERE invoice_id = {invoice_id} AND product_id = {product_id}"
    res = executeQueryAndReturnResultNOCOLUMNNAME(sql)
    if len(res) >= 1:
        return True
    else:
        return False

def get_invoice_by_customer_id(customer_id):
    sql = f"SELECT ip.invoice_id AS 'Invoice ID', SUM(ip.product_quantity * p.price) AS 'Total Cost' FROM invoice_products AS ip JOIN products AS p ON ip.product_id = p.product_id JOIN invoices AS i ON ip.invoice_id = i.invoice_id WHERE i.customer_id = {customer_id} GROUP BY ip.invoice_id;"
    return executeQueryAndReturnResult(sql)


def total_cost_breakdown_and_products_per_invoice():
    sql = f"SELECT ip.invoice_id AS 'Invoice ID',SUM(ip.product_quantity * p.price) AS 'Total Cost', GROUP_CONCAT(ip.product_quantity * p.price) AS 'Cost Per Product', GROUP_CONCAT(p.product_id) AS 'ID Numbers of Products Included', GROUP_CONCAT(ip.product_quantity) AS 'Quantity of Products' FROM invoice_products AS ip JOIN products AS p ON ip.product_id = p.product_id JOIN invoices AS i ON ip.invoice_id = i.customer_id GROUP BY ip.invoice_id;"
    return executeQueryAndReturnResult(sql)
