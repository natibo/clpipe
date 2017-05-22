#!/usr/bin/env python3

import shelve


Yes = ['Y', 'Yes', 'yes', 'y']
No = ['N', 'No', 'no', 'n']
Q = ['Q', 'q', 'Quit', 'quit', 'exit', 'Exit']

"""
Create a Database for storing one's smoking pipes
"""

# Create a Pipe Class in Python


class Pipe:

    def __init__(self, name='', maker='', shape='', store='', buyyear=0):
        Pipe.name = name
        Pipe.maker = maker
        Pipe.shape = shape
        Pipe.store = store
        Pipe.buyyear = buyyear

    def printpipe(Pipe):

            print('\n', '-' * 50, '\n')
            print("Pipe's name is:\t\t\t\t %s" % Pipe.name)
            print("Pipe's maker is:\t\t\t %s" % Pipe.maker)
            print("Pipe's shape is:\t\t\t %s" % Pipe.shape)
            print("You bought this pipe at:\t\t %s" % Pipe.store)
            print("You bought your pipe in:\t\t %s" % Pipe.buyyear)
            print('\n', '-' * 50, '\n')


def addpipe():

    # First, gather information on the new pipe

    db = shelve.open('pipedb')
    while True:
        newname = input('\nEnter your name for the pipe '
                        '(Enter Q to go back to homepage): ')
        if newname in db:
            print("\nA Pipe having that name already exists"
                  " in the database, try again")
            continue
        elif newname in Q:
            break
        else:
            NewPipe = Pipe()
            NewPipe.name = newname
            NewPipe.maker = input(
                'Enter the carver or manufacturer of the pipe: ')
            NewPipe.shape = input('Enter your shape of the pipe: ')
            NewPipe.store = input('Enter where you bought the pipe: ')
            NewPipe.buyyear = input('Enter the year you bought the pipe: ')

    # Print Pipe's information

            NewPipe.printpipe()

    # Store Pipe in the Shelve

        db[newname] = NewPipe
        db.close()
        break


def displaypipe():

    # Display pipes in the user's connection

    print('These are the Pipes in your Database')
    db = shelve.open('pipedb')                 # Reopen the shelve
    print('There are  ', len(db), ' pipes in database \n')

    for k in db:
        dpipe = db[k]
        dpipe.printpipe()

    db.close()


def searchpipe():

    # Search for a Pipe in the collection

    db = shelve.open('pipedb')                 # Reopen the shelve
    while True:
        key = input('\nEnter the Name of Pipe you are searching for? => ')
        if key in db:

            db[key].printpipe()

        else:
            print('No such Pipe "%s"!' % key)
            again = input("\n Do you to search again? Y or N ==>")
            if again in No:
                break
            elif again in Yes:
                continue
            else:
                print("\n I didn't quite get that, try again. \n")
                continue
    db.close()


def editpipe():
    db = shelve.open('pipedb')

    def change():
        setattr(pedit, value, pnew)
        db[pname] = pedit
        db[pname].printpipe()

    while True:
        pname = input('\nEnter your name for the pipe you want to edit '
                      '(Enter Q to go back to homepage): ')
        if pname in Q:
            break

        elif pname not in db:
            print("\ No such Pipe exists"
                  " in the database, try again")
            continue

        else:
            pedit = db[pname]
            print("What would you like to edit\n")
            print("-" * 50, "\n")
            print("1. Name?\t Enter '1'\n")
            print("2. Maker?\t Enter '2'\n")
            print("3. Shape?\t Enter '3'\n")
            print("4. Store?\t Enter '4'\n")
            print("5. Buy Year?\t Enter '5'\n")
            print("Quit?\t Enter 'Q' \n")
            q = input("Enter your selection =>")

            if q == "1":
                value = 'name'
                pnew = input("Enter new name for this Pipe => ")
                change()
                db[pnew] = db.pop(pname)
                break

            elif q == "2":
                value = 'maker'
                pnew = input("Enter new maker for this Pipe => ")
                change()
                break

            elif q == "3":
                value = 'shape'
                pnew = input("Enter new shape for this Pipe => ")
                change()
                break

            elif q == "4":
                value = 'store'
                pnew = input("Enter new store for this Pipe => ")
                change()
            elif q == "5":
                value = 'buyyear'
                pnew = input("Enter new buy year for this Pipe => ")
                change()
            elif q in Q:
                break
            else:
                print("\n I didn't quite get that, try again. \n")
                continue
    db.close()


def delpipe():

    # Delets a Pipe in the collection

    db = shelve.open('pipedb')                 # Reopen the shelve
    while True:
        key = input('\nEnter the Name of Pipe you want to remove? => ')
        if key in db:

            db[key].printpipe()
            delquestion = input('Is this the Pipe you want to delete? => ')
            if delquestion in Yes:
                oldname = str(key)
                db.pop(key)
                print(oldname, " Has been removed from your collection")
            else:
                break

        else:
            print('No such Pipe "%s"!' % key)
            again = input("\n Do you to search again? Y or N ==>")
            if again in No:
                break
            elif again in Yes:
                continue
            else:
                print("\n I didn't quite get that, try again. \n")
                continue
    db.close()


print("WELCOME TO BO\'S PIPE DATABASE \n")

while True:

    # Ask the user what he wants to do?

    print("What would you like to do?\n")
    print("-" * 50, "\n")
    print("1. Display all the Pipes in your collection?\t\t\t Enter '1'\n")
    print("2. Add a new Pipe to your collection?\t\t\t\t Enter '2'\n")
    print("3. Search for a paticular Pipe in your"
          " collection by name?\t Enter '3'\n")
    print("4. Edit a paticular Pipe in your collection?\t\t\t Enter '4'\n")
    print("5. Remove a paticular Pipe in your collection?\t\t\t Enter '5'\n")
    print("Quit?\t Enter 'Q' \n")
    q = input("Enter your selection =>")

    if q == "1":
        displaypipe()
    elif q == "2":
        addpipe()
    elif q == "3":
        searchpipe()
    elif q == "4":
        editpipe()
    elif q == "5":
        delpipe()
    elif q in Q:
        break
    else:
        print("\n I didn't quite get that, try again. \n")
        continue

end = input('GOODBYE')
quit()
