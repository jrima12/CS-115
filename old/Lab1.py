'''Jonathan Amir
I pledge my honor that I have abided by the Stevens Honor System
'''

from cs115 import map, reduce
import math

'''The sum function takes in 2 inputs and adds them together'''
def sum(x,y):
    return x+y

'''inverse function returns the reciprocal of the single input'''
def inverse(n):
    return 1/n

'''approximates the value of e based of its taylor series'''
def e(n):
    '''maps the numbers from 1 to n to the factorial, then maps those numbers
    into the inverse function to get the reciprocal, then adds them all up and
    adds 1 to complete the taylor series'''
    return 1 + reduce(sum, map(inverse, map(math.factorial, range(1, n+1))))

def error(n):
    '''error function uses built in function absolute value to determine the
    difference (error) in the calculated value of e based of the previous function,
    to the actual value of e found in the math library'''
    return abs(math.e - e(n))
