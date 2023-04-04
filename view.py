## Placeholder view

def display_options():
    print('=' * 50)
    print('0. Exit')
    print('1. ')
    print('2. ')
    print('3. ')
    print('4. ')
    print('5. ')
    print('=' * 50)


if __name__ == '__main__':
    while True:
        display_options()
        user_choice = input('Enter a choice: ')
        match user_choice:
            case '0':
                break;
            case '1':
                pass
            case '2':
                pass
            case '3':
                pass
            case '4':
                pass
            case '5':
                pass
