# mandelbrot.py
# Lab 9
#
# Name:Jonathan Amir
# I pledge my honor that I have abided by the Stevens Honor System

# keep this import line...
from cs5png import PNGImage

# start your Lab 9 functions here:
def mult(c,n):
    '''multiplies c and n, by using a for loop
    to add c to result (initially at 0) n times.
    '''
    result = 0
    for i in range(n):
        result = result + c
    return result
        
def update(c,n):
    '''
    Returns the nth value of z by the equation z = z^2 + c,
    starting at z = 0 and repeating the equation n times
    '''
    z = 0
    for i in range(n):
        z = z**2 + c
    return z

def inMSet(c,n):
    '''
    using the same meathod and equation as update function
    this time, both c and z are complex numbers, and it will
    return weather the function is in the Mandelbrot set.
    It is in the Mandelbrot set if it converges, and not if it goes to infinity
    we can check this by using the proof that if it ever goes past 2
    it will diverge to infinity.
    '''
    z = 0 + 0j
    for i in range(n):
        z = z**2 + c
        if abs(z) > 2:
            return False
    return True
