from sql_functions import executeQueryAndCommit, executeQueryAndReturnResult


def add_invoice(vendor_id, invoice_number, invoice_date, invoice_total, payment_total, invoice_due_date, payment_date):
    sql = f"INSERT INTO programming_group_project.invoices VALUES (default, {vendor_id}, '{invoice_number}', {invoice_date}, {invoice_total}, {payment_total}, {invoice_due_date}, {payment_date});"
    executeQueryAndCommit(sql)



