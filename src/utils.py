import operator as op

def cmp(a, b):
    if op.lt(a,b):
        return -1
    elif op.gt(a,b):
        return 1
    else:
        return 0