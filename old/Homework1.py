'''
Jonathan Amir
I pledge my honor that I have abided by the Stevens Honor System.
'''

from cs115 import *

'''multiplication function'''
def mult(x, y):
    return x * y

'''addition function'''
def add(x, y):
    return x + y

'''division function'''
def divides(n, k):
    def div(k):
        return n % k == 0 '''returns True or False'''
    return map(div, k)    '''puts the value k into div to see if divisible'''

'''Factorial function'''
def factorial(n):
    return reduce(mult, range(1, n+1)) '''multiply all the values from one to n inclusively'''

'''Mean function'''
def mean(L):
    return (reduce(add, L))/len(L) '''add all the values in L and then divide by the length of L'''

'''Prime Number Function'''
def prime(n):
    return sum(divides(n, range(2, n))) == 0
'''The line above does a few things. 1, it passes in all the values between 2 and n into division and then to div, to test if it is divisible at all
then it sums up all the True's and Falses, in the returned list, and counts the trues as 1 and the falses as 0
then it checks if the sum is equal to zero (all falses) or if it is not (some amount of true) and returns true or false accordingly
'''

'''I am not sure what else to include in docstrings, but I have a label for each of the functions and other lines of code'''
