from binaryFunctions import *
def operatorStringGenerator(operatorValue):
    # print("\t1) Conjuncion ∧\n"
    #         "\t2) Disyuncion V\n"
    #         "\t3) Implicacion →\n"
    #         "\t4) Dole Implicacion ↔\n"
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
        return "e" #error
def parenthesisGiver(expression):
    return "("+expression+")"
def expressionGenerator(value1,value2,operator):
    #the operator was obtained from a operatorValueOperation
    
    return ""+len(value1)*parenthesisGiver(value1)+operator+parenthesisGiver(value2)






def parenthesisStartEnd(string):
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

def parStarEndIdentifier(string):

    #this will not only append the position, but its indentation too

    start = []
    end = []
    for index in range(len(string)):
        if string[index] == "(":
            start.append(index)
        if string[index] == ")":
            end.append(index)
    # print(startEnd)
    # print(start,end)
    return [start,end]

    return #this returns an array with a start array and an end array
def genStartEndParenthesis(doubleArray):
    startEndParenthesis = []
    
    start = doubleArray[0]
    end = doubleArray[1]
    mixedUp = start+end
    mixedUp.sort()
    indentUpdater = {}
    for element in mixedUp:
        if element in start:
            indentUpdater[element] = 1
        else:
            indentUpdater[element] = -1

    expecting0 = False
    getOut = False
    c = 0
    # print(indentUpdater)
    # print(indentUpdater.keys())
    accumulator = 0
    for position in indentUpdater.keys():
        accumulator += indentUpdater.get(position)
        # print(accumulator)
        if expecting0 == True and accumulator==0:

            
            startEndParenthesis.append(position+1) #the +1 just makes sure that they are printed in full 
            expecting0 = False
        elif accumulator == 1 and expecting0 == False:
            # print(accumulator,expecting0,position)
            expecting0 = True
            # print(accumulator,expecting0,position)

            startEndParenthesis.append(position)




    # so we are going to create a stack.

    return startEndParenthesis



def expressionReader(expression):

    #TODO!
    if False:

        # this should return the name of the first column, the second and the operator
        #   like this [table1,table2,operator]
        #   so that we may abuse our functions later
            # Find the operator
        # if "∧" in expression:
        #     operator = binAnd
        # elif "v" in expression:
        #     operator = binOr
        # elif "→" in expression:
        #     operator = binThen
        # elif "↔" in expression:
        #     operator = binBicond
        # elif "~" in expression:
        #     operator = binNeg
        # else:
        #     return ["error"]
        # Find the table names
        pass
    
    # we cannot get the operator like we used to. Fortunately, we know where it is thanks to the parenthesis
    # we just need to get rid of the nors cuz they are asy and mess stuff up.
    parLoc = genStartEndParenthesis(parStarEndIdentifier(expression))
    print(parLoc,"parloc")
    columns = readInsideParenthesis(expression, parLoc)
    table1 = columns[0]
    table2 = columns[1]

    # Generate the final expression string
    # operatorString = operatorStringGenerator(operator.__name__[3:])
    # operatorString = operatorStringGenerator(operator.__name__[3:])
    value1 = parenthesisGiver(table1)
    value2 = parenthesisGiver(table2)
    operator = 0
    if expression[0] =="~" :
        operator = binNeg(a)
    if "∧" == expression[parLoc[1]]:
        operator = binAnd
    elif "v" == expression[parLoc[1]]:
        operator = binOr
    elif "→" == expression[parLoc[1]]:
        operator = binThen
    elif "↔" == expression[parLoc[1]]:
        operator = binBicond

    #the only thing left is to strip those ugly parenthesis from each table    
    return [table1[1:-1], table2[1:-1], operator] 

if __name__=="__main__":
    parStarEndIdentifier(string="((AB)V(OP))V(RQ)")
    genStartEndParenthesis(parStarEndIdentifier("((AB)V(OP))V(RQ)"))
    a = expressionGenerator("", expressionGenerator("a", "b", operatorStringGenerator(3)),operatorStringGenerator(5))
    print(a)
    # print(expressionReader((a)))

    a  = "((A↔B)∧(OvP))∧(R→Q)"

    print(expressionReader((a)))