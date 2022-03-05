# Revision Number 1 4Mar22
## Begin Derek Ruggirello (4Mar22)

# Imports makeDictionary from the last task
from Task1 import makeDictionary

def AddItem(dict):

    scoreDict = dict

    # Variables to store user inputs
    name = input("Enter the name of the person to add: ")
    value = input("Enter the value added to the name: ")

    # Loop in order to request a new name and value to add to the dictionary.
    while name != 'quit':
        scoreDict[name] = value
        name = input("Enter the name of the person to add: ")
        # Conditional to end the loop when quit is input
        if name == 'quit':
            break
        value = input("Enter the value added to the name: ")

# Revision Number 1 4Mar22
## End Derek Ruggirello
# Zion Worship Cult / Ram Vuduku / Rich Eissen / the Zion Project