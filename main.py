import pandas as pd
from binaryFunctions import binOr


def trueFalseFill(len,total):
    tFS = ["T"]*len + ["F"]*len
    tFS = tFS * int(total/(2*len))
    return tFS


def genValueBin( valueFromTable1,valueFromTable2,operation ):
    #This function takes a decorator an 
    return operation(valueFromTable1,valueFromTable2)


def printTable(variableList,expressionList):
    #the variableArray is a list of all variables
    # 

    # the expressionList is a list. There is no need for it to be a numpy array yet
    # It is a list of all expressions. 
    

    # The array to be printed ought to have at least a column per variable
    # 2^n rows, and a column per expression
    varLen = len(variableList)
    rowNo = (2**len(variableList))
    indexG = [x+1 for x in range(rowNo)]

    trueFalseDictionary = {}
    for x in list(range(varLen)):
        trueFalseDictionary[variableList[x]] = trueFalseFill( 2**x ,rowNo)

    
    table = pd.DataFrame(trueFalseDictionary,columns=variableList, index=indexG)


    
    

    print(table)
    pass

if __name__ =="__main__":
    printTable(["a","b"],[])

