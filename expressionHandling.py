
def operatorStringGenerator(operatorValue):
    # print("\t1) Conjuncion ^\n"
    #         "\t2) Disyuncion V\n"
    #         "\t3) Implicacion ->\n"
    #         "\t4) Dole Implicacion <->\n"
    #         "\t5) Negacion ~\n"
    #         "\t6) Salir \n")
    if operatorValue == 1:
        return "∧"
    elif operatorValue == 2:
        return "v"
    elif operatorValue == 3:
        return "→"
    elif operatorValue == 4:
        return "↔"
    elif operatorValue == 5:
        return "~"
    else:
        pass
def parenthesisGiver(expression):
    return "("+expression+")"
def expressionGenerator(value1,value2,operator):
    #the operator was obtained from a operatorValueOperation
    
    return ""+len(value1)*parenthesisGiver(value1)+operator+parenthesisGiver(value2)






def parenthesiStartEnd(string):
    startEnd = []
    for index in range(len(string)):
        if string[index] == "(":
            startEnd.append(index+1)
        if string[index] == ")":
            startEnd.append(index)
    # print(startEnd)
    return startEnd

def readInsideParenthesis(string,parLoc):
    #parloc has the property that (parloc%2==0)
    columns = []
    for x in range(0,len(parLoc)-1,2):
        columns.append(string[parLoc[x]:parLoc[x+1]])
    return columns



def expressionReader(expression):

    #TODO!

    # this should return the name of the first column, the second and the operator
    #   like this [table1,table2,operator]
    #   so that we may abuse our functions later
         # Find the operator
    if "∧" in expression:
        operator = binAnd
    elif "v" in expression:
        operator = binOr
    else:
        operator = binThen

    # Find the table names
    parLoc = parenthesisStartEnd(expression)
    columns = readInsideParenthesis(expression, parLoc)
    table1 = columns[0]
    table2 = columns[1]

    # Generate the final expression string
    operatorString = operatorStringGenerator(operator.__name__[3:])
    value1 = parenthesisGiver(table1)
    value2 = parenthesisGiver(table2)
    finalExpression = expressionGenerator(value1, value2, operatorString)

    return [table1, table2, operator] 

if __name__=="__main__":
    print(readInsideParenthesis("21211(banana),awertgfhtr(tree)", parenthesiStartEnd("21211(banana),awertgfhtr(tree)")))
