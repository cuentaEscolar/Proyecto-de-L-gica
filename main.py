import pandas as pd
from binaryFunctions import binOr,binAnd,binThen
from expressionHandling import expressionReader
import proposiciones

def trueFalseFill(len,total):
    tFS = ["T"]*len + ["F"]*len
    tFS = tFS * int(total/(2*len))
    return tFS

def GetTablesFromExpression(expression):
    pass
    return [table1,table2,operator]

def getTableBin(table1,table2,operation):
    binBuffer = []
    for index in range(len(table1)):
        binBuffer.append([genValueBin(table1[index], table2[index], operation)])


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
    expLen = len(expressionList)
    rowNo = (2**len(variableList))
    indexG = [x+1 for x in range(rowNo)]

    trueFalseDictionary = {}
    for x in list(range(varLen)):
        trueFalseDictionary[variableList[x]] = trueFalseFill( 2**x ,rowNo)
    


    #TODO generate the actual rows for the expressions
    #plz do use the functions from the expression handling page thank you very much.
    # for x in list(range(expLen)):



    #     trueFalseDictionary[expressionList[x]] = getTableBin(table1, table2, operation)

    table = pd.DataFrame(trueFalseDictionary,columns=variableList, index=indexG)


    
    

    print(table)
    pass

if __name__ =="__main__":
    # printTable(["a","b"],[])


    

    varTable = proposiciones.getVariables()
    expressionTable = proposiciones.generateExpresions(varTable)
    printTable(varTable, [])
    print(expressionTable)

    