from prettytable import PrettyTable
from controller import *

# Placeholder view
products_table = PrettyTable()
current_product_ids = []


def initialize_tables():
    current_products_table = PrettyTable()
    current_products_table.field_names = show_products()[0]
    current_products_table.add_rows(show_products()[1])
    return current_products_table


def display_options():
    print('=' * 50)
    print('0. Exit')
    print('1. Start Transaction ')
    print('2. Show Products')
    print('3. Show Out Of Stock Products')
    print('4. Show Last Month Customer History')
    print('=' * 50)


def transaction_options():
    print('=' * 50)
    print('1. Show Current Transaction Items')
    print('2. Add Item')
    print('3. Remove Item')
    print('0. Exit')
    print('=' * 50)


if __name__ == '__main__':
    products_table = initialize_tables()
    while True:
        display_options()
        user_choice = input('Enter a choice: ')
        match user_choice:
            case '0':
                break
            case '1':
                while True:
                    transaction_options()
                    user_choice = input('Enter a choice: ')
                    match user_choice:
                        case '0':
                            #Create Customer
                            customer_fname = input('Enter your first name: ')
                            customer_lname = input('Enter your last name: ')
                            customer_phone = input('Enter your phone number: ')
                            customer_email = input('Enter your email: ')
                            customer_address = input('Enter your address: ')
                            #add_customer(customer_fname, customer_lname, customer_phone, customer_email, customer_address)
                            #Need a get_customer_by_name(fullname) function
                            #get_customer_by_name(customer_fname+customer_lname)
                            # add new invoice in database here with add_invoice
                            #add_invoice(customer_id, 'NOW()')
                            break
                        case '1':
                            print(products_table)
                        case '2':
                            print(products_table)
                            user_product_choice = input('Choose product: ')
                        case '3':
                            pass

            case '2':
                print(products_table)
            case '3':
                pass
            case '4':
                pass
            case '5':
                pass
