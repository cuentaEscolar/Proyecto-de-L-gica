
def operatorStringGenerator(operatorValue):
#
#   0---> ∧     for and
#   1---> v     for or
#   and thats it for the time being
    if operatorValue==0:
        return "∧"
    elif operatorValue==1:
        return "v"
    else:
        pass
def parenthesisGiver(expression):
    return "("+expression+")"
def expressionGenerator(value1,value2,operator):
    #the operator was obtained from a operatorValueOperation
    
    return ""+parenthesisGiver(value1)+parenthesisGiver(value2)+operator






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
    pass 

if __name__=="__main__":
    print(readInsideParenthesis("21211(banana),awertgfhtr(tree)", parenthesiStartEnd("21211(banana),awertgfhtr(tree)")))