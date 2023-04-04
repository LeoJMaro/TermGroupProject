from sql_functions import executeQueryAndCommit, executeQueryAndReturnResult


def add_invoice(vendor_id, invoice_number, invoice_date, invoice_total, payment_total, invoice_due_date, payment_date):
    sql = f"INSERT INTO programming_group_project.invoices VALUES (default, {vendor_id}, '{invoice_number}', {invoice_date}, {invoice_total}, {payment_total}, {invoice_due_date}, {payment_date});"
    return executeQueryAndCommit(sql)


def add_customer(customer_first_name, customer_last_name, customer_phone, customer_email, customer_address):
    sql = f"INSERT INTO programming_group_project.customers VALUES (default, '{customer_first_name}', '{customer_last_name}', '{customer_phone}', '{customer_email}', '{customer_address}');"
    executeQueryAndCommit(sql)

def increase_inventory(inventory_stock):
    sql = f"UPDATE programming_group_project.products SET inventory_stock = {inventory_stock};"
    executeQueryAndCommit(sql)


def decrease_inventory():
    pass

def get_product_by_id():
    pass


def show_products():
    sql = "SELECT * FROM products"
    return executeQueryAndReturnResult(sql)

# add_invoice(69,'aaa111', 'NOW()', 299.99, 299.99, 'NOW()', 'NOW()')
