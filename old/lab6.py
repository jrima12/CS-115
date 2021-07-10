'''
Created on 03/18/2021
@author:  Jonathan Amir
Pledge:  I pledge my honor that I have abided by the Stevens Honor System

CS115 - Lab 6
'''
def isOdd(n):
    '''Returns whether or not the integer argument is odd.'''
    return n%2 != 0

def numToBinary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned.'''
    if n == 0:
        return ""
    if isOdd(n):
        return numToBinary(n//2) + "1"
    else:
        return numToBinary(n//2) + "0"

def binaryToNum(s):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    if s == "":
        return 0
    if isOdd(int(s[len(s)-1])):
        return binaryToNum(s[:(len(s)-1)])*2+1
    return binaryToNum(s[:(len(s)-1)]) * 2

def increment(s):
    '''Precondition: s is a string of 8 bits.
    Returns the binary representation of binaryToNum(s) + 1.'''
    if s == "11111111":
        return "00000000"
    else:
        ntb = numToBinary((binaryToNum(s) +1))
        return("0"*(8-len(ntb))) + ntb

def count(s, n):
    '''Precondition: s is an 8-bit string and n >= 0.
    Prints s and its n successors.'''
    if n<0:
        return None
    print(s)
    count(increment(s), n-1)

def numToTernary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the ternary representation of non-negative integer
    n. If n is 0, the empty string is returned.'''
    if n == 0:
        return ""
    if n%3 == 0:
        return numToTernary(n//3) + "0"
    if n%3 == 1:
        return numToTernary(n//3)+"1"
    else:
        return numToTernary(n//3)+"2"

def ternaryToNum(s):
    '''Precondition: s is a string of 0s, 1s, and 2s.
    Returns the integer corresponding to the ternary representation in s.
    Note: the empty string represents 0.'''
    if s == "":
        return 0
    if int(s[int(len(s))-1]) == 2:
        return ternaryToNum(s[:(len(s)-1)])*3+2
    if int(s[int(len(s))-1]) == 1:
        return ternaryToNum(s[:(len(s)-1)])*3+1
    else:
        return ternaryToNum(s[:(len(s)-1)])*3
                               
