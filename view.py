from prettytable import PrettyTable
from controller import *

# Placeholder view
transaction_items = []
products_table = PrettyTable()
def initialize_tables():
    products_table = PrettyTable()
    products_table.field_names = show_products()[0]
    products_table.add_rows(show_products()[1])
    return products_table
def display_options():
    print('=' * 50)
    print('0. Exit')
    print('1. Start Transaction ')
    print('=' * 50)


def transaction_options():
    print('=' * 50)
    print('0. Exit')
    print('1. Show Items')
    print('2. Add Item')
    print('3. Remove Item')
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
                            break
                        case '1':
                            print(products_table)
                        case '2':
                            print(products_table)
                            user_product_choice = input('Choose product: ')


                        case '3':
                            pass
            case '2':
                pass
