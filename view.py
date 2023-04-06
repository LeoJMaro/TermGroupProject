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
    print('0. Exit')
    print('1. Show Products')
    print('2. Add Item')
    print('3. Remove Item')
    print('4. Show Current Transaction Items')
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
                            # Create invoice in database here with add_invoice
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
