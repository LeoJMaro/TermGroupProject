from sql_functions import executeQueryAndCommit, executeQueryAndReturnResult


def add_invoice(vendor_id, invoice_number, invoice_date, invoice_total, payment_total, invoice_due_date, payment_date):
    sql = f"INSERT INTO programming_group_project.invoices VALUES (default, {vendor_id}, '{invoice_number}', {invoice_date}, {invoice_total}, {payment_total}, {invoice_due_date}, {payment_date});"
    return executeQueryAndCommit(sql)


def add_customer():
    pass


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
