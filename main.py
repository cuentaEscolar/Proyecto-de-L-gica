import pandas as pd
from binaryFunctions import binOr,binAnd,binThen
from expressionHandling import expressionReader
import proposiciones
from  expressionHandling import *

def translateTF(value):
    if value =="T":
        return True
    else : return False


def trueFalseFill(len,total):
    tFS = ["T"]*len + ["F"]*len
    tFS = tFS * int(total/(2*len))
    return tFS

def GetTablesFromExpression(expression):
    return [table1,table2,operator]

def getTableBin(table1,table2,rowNo,operation):
    binBuffer = []
    for index in range(rowNo):
        binBuffer.append(genValueBin(translateTF(table1[index]), translateTF(table2[index]), operation))
    return binBuffer

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
    trueFalseDictionary = {}            #the dictionary where the truth "rows" are to be stored
    for x in list(range(varLen)):
        trueFalseDictionary[variableList[x]] = trueFalseFill( 2**x ,rowNo)
    processedExpressions = []           # a list full of lists that look like [componentA, componentB, operation] # Hay problemas con la negación
    for expression in expressionList:
        processedExpressions.append(expressionReader(expression))
    for exprIndex, expression in enumerate((processedExpressions)):
        if len(expression)==2:
            # this is in the case of the negation. I had to have negation take 2 arguments (though it ignores the first lol) so that I didnt have to refactor everythin
            # SO BASICALLY NEGATION ALWAYS HAS LEN ==2 . ALWAYS
            
            componentA = expression[0]
            operation = expression[1]
            componentB = variableList[0]
        else:
            componentA = expression[0]
            componentB = expression[1]
            operation = expression[2]
        # print(expression)
        
        trueFalseDictionary[expressionList[exprIndex]]  = getTableBin(trueFalseDictionary[componentA], trueFalseDictionary[componentB], rowNo, operation)

        # fill = []
        # for index in range(rowNo):
        #     # fill.append(genValueBin(translateTF(trueFalseDictionary[componentA][index]), translateTF(trueFalseDictionary[componentB][index]), operation))
        
        # print(fill)
        # print(expressionList[exprIndex])
        # print(trueFalseDictionary)

    table = pd.DataFrame(trueFalseDictionary,columns=(variableList.append(expressionList)), index=indexG)

    print(table)

    #TODO generate the actual rows for the expressions
    #plz do use the functions from the expression handling page thank you very much.
    # for x in list(range(expLen)):



    #     trueFalseDictionary[expressionList[x]] = getTableBin(table1, table2, operation)



if __name__ =="__main__":
    # printTable(["a","b"],[])


    

    varTable = proposiciones.getVariables()
    expressionTable = proposiciones.generateExpresions(varTable)
    # expressionTable+=(proposiciones.generateExpresions(varTable+expressionTable))
    print(expressionTable)
    printTable(varTable, expressionTable)
    # print(expressionTable)

    # print(expressionReader((expressionGenerator("(x)v(y)", "b","v"))))

    