from ast import operator


def add(x,y):
    """It returns addition of two numbers"""
    return x+y

def sub(x,y):
    """It returns subtraction of two numbers"""
    return x-y

def mul(x,y):
    """It returns multiplication of two numbers"""
    return x*y

def div(x,y):
    """It returns division of two numbers"""
    return x/y

operators = {
'+' : add,
'-' : sub,
'*' : mul,
'/' : div
}