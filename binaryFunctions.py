def binOr(a,b):
# both a and b are bool variables
    # 1 1 - 1
    # 1 0 - 1
    # 0 1 - 1
    # 0 0 - 0
    if (a or b ):
        return True
    else :
        return False

def binAnd(a,b):
    if (a and b):
        return True
    else:
        return False

def binThen(a,b):
    # both a and b are bool variables
    # 1 1 - 1
    # 1 0 - 0
    # 0 1 - 1
    # 0 0 - 1
    if (a and (not b)):
        return False
    else: return True
    
def binBicond(a, b):
    # both a and b are bool variables
    if (a == b):
        return True
    else:
        return False

def binNeg(a):
    # a is a bool variable
    if (not a):
        return True
    else:
        return False
