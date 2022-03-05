# Revision Number 1 4Mar22
## Begin Derek Ruggirello (4Mar22)

def makeDictionary():

    # Create lists from customer
    names = ['joe','tom','barb','sue','sally']
    scores = [10,23,13,18,12]
    # Make scoreDict global for use outside fuction
    global scoreDict
    scoreDict = {}

    # Iteration loop goes through the lists and adds values to them in dictionary
    for key in names:
        for value in scores:
            scoreDict[key] = value
            # Removes value from list2 in order to go onto the next value
            scores.remove(value)
            # Breaks for loop in order to go to the next name
            break 
    return scoreDict

# Call make dictionary function
makeDictionary()

# Revision Number 1 4Mar22
## End Derek Ruggirello
# Zion Worship Cult / Ram Vuduku / Rich Eissen / the Zion Project