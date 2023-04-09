from sql_functions import executeQueryAndCommit, executeQueryAndReturnResult,executeQueryAndReturnResultNOCOLUMNNAME


def add_invoice(vendor_id, invoice_number, invoice_date, invoice_total, payment_total, invoice_due_date, payment_date):
    sql = f"INSERT INTO programming_group_project.invoices VALUES (default, {vendor_id}, '{invoice_number}', {invoice_date}, {invoice_total}, {payment_total}, {invoice_due_date}, {payment_date});"
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
def get_customer_id_by_customer_name(customer_first_name,customer_last_name):
    sql= f"SELECT customer_id FROM pgp.customers WHERE customer_first_name = '{customer_first_name}' and customer_last_name = '{customer_last_name}';"
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
    print(query[11:16])
    return query

def add_customer_id_to_invoices(customer_id):
    sql = f"INSERT INTO invoices(customer_id, invoice_date) VALUES ({customer_id}, now());"
    return executeQueryAndCommit(sql)

def get_most_recent_invoice_id_by_date():
    sql = f"SELECT invoice_id FROM invoices ORDER BY invoice_date DESC LIMIT 1;"
    return executeQueryAndReturnResultNOCOLUMNNAME(sql)[0][0]

def add_product_to_invoice_products(invoice_id,product_choice):
    sql = f"INSERT INTO invoice_products(invoice_id,product_id,product_quantity) VALUES ({invoice_id},{product_choice}, 1);"
    return executeQueryAndCommit(sql)

def get_product_id(product_choice):
    sql = f"SELECT product_id FROM pgp.products WHERE product_name = '{product_choice}';"
    query = executeQueryAndReturnResultNOCOLUMNNAME(sql)[0][0]
    return query


def increase_inventory():
    pass


def decrease_inventory():
    pass

def get_product_by_id():
    pass


def show_products():
    sql = "SELECT * FROM products"
    return executeQueryAndReturnResult(sql)

# add_invoice(69,'aaa111', 'NOW()', 299.99, 299.99, 'NOW()', 'NOW()')
