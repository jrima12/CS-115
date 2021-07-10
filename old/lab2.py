'''
Jonathan Amir
I pledge my honor that I have abided by the Stevens Honor System
'''

from cs115 import *

def dot(L,K):
    #dot function will take 2 inputs and compute the dot product
    #If different lengths will return "try again"
    #if empty, will return 0.0
    #otherwise, will return L1*K1 + L2*K2 + L3*k3..."
    if len(L) != len(K):
        return "try again"
    elif len(L) == 0 or len(K) == 0:
        return 0.0
    else:
        return L[0]*K[0] + dot(L[1:], K[1:])

def explode(S):
    #explode will take a string input and return characters in a list
    if len(S) == 0:
        return []
    else:
        return [S[0]] + explode(S[1:])

def ind(e, L):
    #takes element e and sequence L (list or string)
    #will return where in L, e exists (first)
    #if not in L, then return the length of L
    if L == []:
        return 0
    if L == "":
        return 0
    if L[0] == e:
        return 0
    else:
        return 1 + ind(e,L[1:])
    
def removeAll(e,L):
    #element e and list L
    #return list identical to L but without e
    if L == []:
        return []
    if L[0] == e:
        return removeAll(e, L[1:])
    else:
        return [L[0]]+removeAll(e,L[1:])

def myFilter(f, L):
    if L == []:
        return []
    if f(L[0]):
        return  [L[0]] + myFilter(f, L[1:])
    if not f(L[0]):
        return  [] + myFilter(f, L[1:])

def deepReverse(L):
    #returns a reversal of a list
    if L == []:
        return []
    if type(L[0]) == type([]):
        return deepReverse(L[1:]) + [deepReverse(L[0])]
    else:
        return deepReverse(L[1:]) + [L[0]]
