# Revision Number 1 4Mar22
## Begin Derek Ruggirello (4Mar22)

import Task1, Task2, Task3, Task4

def DeleteItem(dict):
    
    inputValue = input("Enter name to delete: ")
    del dict[inputValue]
    print(dict)
    return dict

def Print(dict):
    print(dict)

def Program():
    tempDict = Task1.makeDictionary
    UserInput = ''
    while UserInput != 'q' and UserInput != 'Q':
        UserInput = input("Please enter command. Ex. Add, Delete, Query, Print, or Q for quit: ")
        if UserInput == 'add' or UserInput == 'Add':
            Task3.AddItem(tempDict)
        elif UserInput == 'delete' or UserInput == 'Delete':
            tempDict = DeleteItem(tempDict)
        elif UserInput == 'query' or UserInput == 'Query':
            Task2.QueryDict(tempDict)
        elif UserInput == 'print' or UserInput == 'Print':
            Print(tempDict)
        elif UserInput == 'q' or UserInput == 'Q':
            break
        else:
            print("Invalid input. Please type either Add, Delete, Query, Print, or Q for quit: ")
          
Program()

# Revision Number 1 4Mar22
## End Derek Ruggirello
# Zion Worship Cult / Ram Vuduku / Rich Eissen / the Zion Project