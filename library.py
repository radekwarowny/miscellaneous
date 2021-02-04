
#!/usr/bin/env python

import os
import time

__author__      = "Radek Warowny and Connor Heckley"
__version__   = "1.0"
__status__ = "Education demo"

""" Newcast Library Demo Project """


details = [] # cookie stores username for current session


library_db = [ #  Our mock library database
                {'type': 'book','title': 'Harry Potter', 'author': 'J.K.Rawling', 'date': 2004},
                {'type': 'book','title': 'Bible', 'author': 'J.Christ', 'date': 32},
                {'type': 'book','title': 'PhD for Dummies', 'author': 'Andrew Dockerty', 'date': 2015},

                {'type': 'cd','title': 'The Joshua Tree', 'author': 'U2', 'date': 1987},
                {'type': 'cd','title': 'Greatest Hits', 'author': 'Now', 'date': 2010},
                {'type': 'cd','title': 'Physical Graffiti', 'author': 'Led Zeppelin', 'date': 1975}
            ]


""" Application """

def login_screen():

    os.system('clear||cls') # clears the terminal

    global details 

    print("\t=================")
    print("\tNewcastle Library")
    print("\t=================\n")

    username = input("\tUsername? ")
    password = input("\tPassword? ")

    details = [username, password]
    login_validation(details)


def login_validation(details):
 
    username = details[0]
    password = details[1]
    
    try: # find and open db file
        f = open("database.txt", "r")
        logins = f.read()
        logins = logins.split('\n')
    
    except FileNotFoundError: # if not found create db file
        f = open("database.txt", "a")
        f.write(username + "\n")
        f.write(password + "\n")
        f.close()

        print("\t\tYou have signed up!\n")
        print("\t\tNow Please Login")

        time.sleep(2)
        login_screen()
            
    if username in logins:
        if password in logins:
            menu()
    else:
        login_screen()


def menu():
    os.system('clear||cls')
    
    print()
    print("********************\n")
    print(" 1. Rent a book")
    print(" 2. Rent a CD")
    print()
    print(" 3. Return a book")
    print(" 4. Return a CD")
    print()
    print(" 5. Show Library Content")
    print(" 6. Logout")
    print(" 7. Exit Application")
    print("\n********************")

    option = input()

    if option == '1':

        search_title = input("RENT BOOK - Title: ")
        os.system('clear||cls')
        for i in library_db:
            if (search_title.upper() == i.get('title').upper()) and i.get('present') != False:
                print("\n//////////////////////////////////////////////////////")
                print(f"\nYou have borrowed {i.get('title')} for 30 days.")
                print("\n//////////////////////////////////////////////////////")
                time.sleep(3)
                take_out_item(search_title)
        print("Book not in library.")
        time.sleep(2)
        menu()

    elif option == '2':
        os.system('clear||cls')
        search_title = input("RENT CD - Title: ")
        for i in library_db:
            if (search_title.upper() == i.get('title').upper()) and i.get('present') != False:
                print("\n//////////////////////////////////////////////////////")
                print(f"\nYou have borrowed {i.get('title')} for 30 days.")
                print("\n//////////////////////////////////////////////////////")
                time.sleep(3)
                take_out_item(search_title)
                
        print("CD not in library.")
        time.sleep(3)
        menu()

    elif option == '3':
        title = input("RETURN BOOK - Title:  ")
        os.system('clear||cls')
        return_item(title)
        menu()

    elif option == '4':
        title = input("RETURN CD - Title:  ")
        os.system('clear||cls')
        return_item(title)
        menu()

    elif option == '5':
        os.system('clear||cls')

        for i in library_db:
            if i.get('present') == False:
                print('*',i)
            print(i)
        
        time.sleep(5)
        menu()
    
    elif option == '6':
        logout()
    
    elif option == '7':
        os.system('clear||cls')

        print("\t=================")
        print("\tNewcastle Library")
        print("\t=================\n")

        print("---   ---   ---   ---   ---   ---")
        print("\tApplication Shutdown")
        print("---   ---   ---   ---   ---   ---\n")
        
        quit()
        
    else:
        print("Input Error")
        menu()

def take_out_item(title):
    global details
    os.system('clear||cls')
    for i in library_db:
        if title.upper() == i.get('title').upper():
            i['present'] = False 
            i['username_of_borrower'] = details[0]
    menu()

def return_item(title):
    os.system('clear||cls')
    global details 
    for i in library_db:
        if title.upper() == i.get('title').upper():
             i['present'] = True
             i['username_of_borrower'] = details[0] 
    menu()

       
def logout():
    os.system('clear||cls')
    print("\n///////////////////////////////")
    print("\nUser Logged Out\n")
    print("///////////////////////////////\n")
    time.sleep(2)
    login_screen()


if __name__ == "__main__":
    login_screen()













