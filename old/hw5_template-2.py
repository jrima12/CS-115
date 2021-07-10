'''
Created on 03/12/2021
@author:   Jonathan Amir
Pledge:    I pledge my honor that I have abided by the Stevens Honor System

CS115 - Hw 5 (Rev. Oct 2020 by D.N.)
'''
import turtle  # Needed for graphics
from turtle import *

def sv_tree(trunk_length, levels):
    '''creates a series of branches of length trunk_length. there are "levels" level
    of branches per chain'''
    if levels == 0:
        return None
    forward(trunk_length)
    left(10)
    sv_tree(trunk_length*0.7, levels-1)
    right(20)
    sv_tree(trunk_length*0.7, levels-1)
    left(10)
    backward(trunk_length)

def fast_lucas(n):
    '''Returns the nth Lucas number using the memoization technique
    shown in class and lab. The Lucas numbers are as follows:
    [2, 1, 3, 4, 7, 11, ...]'''
    def helper(n, memo):
        if n in memo:
            return memo[n]
        if n == 0:
            num = 2
        elif n == 1:
            num = 1
        else:
            num = helper(n-1,memo) + helper(n-2,memo)
        memo[n] = num
        return num
    return helper(n, {})
def fast_change(amount, coins):
    '''Takes an amount and a list of coin denominations as input.
    Returns the number of coins required to total the given amount.
    Use memoization to improve performance.'''
    def fast_change_helper(amount, coins, memo):
        '''Does the job of fast_change, assuming coins is a tuple.'''
        if(amount, coins) in memo:
            return memo[(amount, coins)]
        if amount == 0:
            ch = 0
        elif amount < 0:
            ch = float("inf")
        elif coins == ():
            ch = float("inf")
        else:
            lose = fast_change_helper(amount, coins[1:], memo)
            use = 1 + fast_change_helper(amount-coins[0], coins, memo)
            ch = min(use, lose)
        memo[(amount,coins)] = ch
        return ch

    # Call the helper. Note we converted the list to a tuple.
    return fast_change_helper(amount, tuple(coins), {})

# If you did this correctly, the results should be nearly instantaneous.
print(fast_lucas(3))  # 4
print(fast_lucas(5))  # 11
print(fast_lucas(9))  # 76
print(fast_lucas(24))  # 103682
print(fast_lucas(40))  # 228826127
print(fast_lucas(50))  # 28143753123

print(fast_change(131, [1, 5, 10, 20, 50, 100]))
print(fast_change(292, [1, 5, 10, 20, 50, 100]))
print(fast_change(673, [1, 5, 10, 20, 50, 100]))
print(fast_change(724, [1, 5, 10, 20, 50, 100]))
print(fast_change(888, [1, 5, 10, 20, 50, 100]))

# Should take a few seconds to draw a tree.
sv_tree(100, 4)
