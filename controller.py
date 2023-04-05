from sql_functions import executeQueryAndCommit, executeQueryAndReturnResult


def add_invoice(invoice_number, customer_id, invoice_date):
    sql = f"INSERT INTO programming_group_project.invoices VALUES ('{invoice_number}', {customer_id}, {invoice_date});"
    return executeQueryAndCommit(sql)


def add_customer(customer_first_name, customer_last_name, customer_phone, customer_email, customer_address):
    sql = f"INSERT INTO programming_group_project.customers VALUES (default, '{customer_first_name}', '{customer_last_name}', '{customer_phone}', '{customer_email}', '{customer_address}');"
    executeQueryAndCommit(sql)

def increase_inventory(intake_amount):
    sql = f"UPDATE programming_group_project.products SET inventory_stock = inventory_stock + {intake_amount};"
    executeQueryAndCommit(sql)

def decrease_inventory(purchase_amount):
    sql = f"UPDATE programming_group_project.products SET inventory_stock = inventory_stock - {purchase_amount};"
    executeQueryAndCommit(sql)

def get_product_by_id(product_id):
    sql = f"SELECT product_name, product_description, inventory_stock, price FROM programming_group_project WHERE product_id = {product_id};"
    executeQueryAndReturnResult(sql)

def show_products():
    sql = "SELECT * FROM products"
    return executeQueryAndReturnResult(sql)

def search_invoice_by_customer_id(customer_id):
    sql = f"SELECT ip.invoice_id AS 'Invoice ID', SUM(ip.product_quantity * p.price) AS 'Total Cost' FROM invoice_products AS ip JOIN products AS p ON ip.product_id = p.product_id JOIN invoices AS i ON ip.invoice_id = i.invoice_id WHERE i.customer_id = {customer_id} GROUP BY ip.invoice_id;"
    return executeQueryAndReturnResult(sql)

def total_cost_breakdown_and_products_per_invoice():
    sql = f"SELECT ip.invoice_id AS 'Invoice ID',SUM(ip.product_quantity * p.price) AS 'Total Cost', GROUP_CONCAT(ip.product_quantity * p.price) AS 'Cost Per Product', GROUP_CONCAT(p.product_id) AS 'ID Numbers of Products Included', GROUP_CONCAT(ip.product_quantity) AS 'Quantity of Products' FROM invoice_products AS ip JOIN products AS p ON ip.product_id = p.product_id JOIN invoices AS i ON ip.invoice_id = i.customer_id GROUP BY ip.invoice_id;"
    return executeQueryAndReturnResult(sql)

# add_invoice(69,'aaa111', 'NOW()', 299.99, 299.99, 'NOW()', 'NOW()')