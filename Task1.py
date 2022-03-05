# Revision Number 1 4Mar22
## Begin Derek Ruggirello (4Mar22)

def makeDictionary():
    names = ['joe','tom','barb','sue','sally']
    scores = [10,23,13,18,12]
    global scoreDict
    scoreDict = {}
    for key in names:
        for value in scores:
            scoreDict[key] = value
            scores.remove(value)
            break 

makeDictionary()
print(scoreDict)

# Revision Number 1 4Mar22
## End Derek Ruggirello
# Zion Worship Cult / Ram Vuduku / Rich Eissen / the Zion Project