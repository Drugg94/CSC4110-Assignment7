# Revision Number 1 4Mar22
## Begin Derek Ruggirello (4Mar22)

# Imports makeDictionary from the last task
from Task1 import makeDictionary

def QueryDict():
    # Equates scoreDict to the dictionary made in makeDictionary
    scoreDict = makeDictionary()
    # Creates variable to store user inputs
    name = 'barb'
    
    # Iterative loop in order to ask the user for name input and then output the value associated.tom
    while name != 'quit' and name != 'Quit':
        print("The score for", name, "is:", scoreDict[name])
        name = input("Please enter joe, tom, barb, sue, or sally for your next query, or type quit to end:\n")
    
# Revision Number 1 4Mar22
## End Derek Ruggirello
# Zion Worship Cult / Ram Vuduku / Rich Eissen / the Zion Project