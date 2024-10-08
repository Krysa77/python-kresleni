from kresleni import spirala, random_shape, jedna, zprava

def main_menu():

    operation = input('''
Select operation:
[1] - Spiral
[2] - Random
[3] - Jednicka
[4] - Zprava
[0] - Exit

''')
    mylist = []

    if operation == '1':
        print("Program vykresli spiralu: ")
        spirala()

    elif operation == '2':
        print("Program vykresli neco nahodneho: ")
        random_shape()
    elif operation == '3':
        print("Program vykresli jednicku: ")
        jedna()
    elif operation == '4':
        print("Program vypise zpravu: ")
        zprava()
    elif operation == '0':
        print("Program se vypne: ")
        exit()
    else:
        print('---:')

    again()

def again():
    list_again = input('''
Turtle screen will close after 2 seconds.
Would you like to see main menu again? (Y/N)
''')

    if list_again.upper() == 'Y':
        main_menu()
    elif list_again.upper() == 'N':
        print('OK. Bye bye. :)')
    else:
        again()

main_menu()