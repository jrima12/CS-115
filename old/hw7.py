'''
Jonathan Amir
I pledge my honor that I have abided by the Stevens Honor System
'''

from cs115 import *

def numToBaseB(N, B):
    '''Will take in an input of non negative integer and so
    base of counting system (between 2 and 10) and returns a string
    of number N in base B)
    Assum integer N is in base 10
    '''
    def helper(N,B):
        if N == 0:
            return ''
        return (helper(N//B, B) + str(N%B))
    if N == 0:
        return '0'
    return helper(N,B)

def baseBToNum(S,B):
    '''take a string S and a base B (between 2 and 10) and
    convert the integer represented in string S of base B
    to an integer in base 10
    '''
    if S == "":
        return 0
    return baseBToNum(S[1:], B) + int(B**(len(S)-1)*int(S[0]))

def baseToBase(B1,B2,SinB1):
    ''' takes 2 bases between 2 and 10, and string of a number in
    base B1. will output same number in B2 as a string
    '''
    x = baseBToNum(SinB1, B1)
    return numToBaseB(x, B2)

def add(S,T):
    '''takes 2 binary strings, returns their sum in binary'''
    x = baseBToNum(S, 2) + baseBToNum(T,2)
    return numToBaseB(x, 2)

def addB(S,T):
    '''returns the sum of 2 binary strings without converting to decimal (only using bunday addition)'''
    if len(T) > len(S):
        S = "0"*(len(T)-len(S))+S
        
    elif len(S) > len(T):
        T = "0"*(len(S)-len(T))+T
    FullAdder = {
        ('0', '0', '0'): ('0', '0'),
        ('0', '0', '1'): ('1', '0'),
        ('0', '1', '0'): ('1', '0'),
        ('0', '1', '1'): ('0', '1'),
        ('1', '0', '0'): ('1', '0'),
        ('1', '0', '1'): ('0', '1'),
        ('1', '1', '0'): ('0', '1'),
        ('1', '1', '1'): ('1', '1')
    }
    def helper(a,b,c):
        if a == '' and b == '':
            if c == "0":
                return ""
            else:
                return c
        sumB, carry = FullAdder[(a[-1],b[-1], c)]
        return helper(a[:-1], b[:-1], carry) + sumB


    return helper(S,T,"0")
