'''Jonathan Amir
I pledge my honor that I have abided by the Stevens Honor System
'''
from cs115 import *

L = [1,5,10,25,50]

def change(amount, coins):
    '''
    Change function will take 2 parameters. an amount to make change of, and the coins available
    It will test every possibility and return the lowest amount
    '''
    if amount == 0:
        return 0
    if coins == []:
        return float("inf")
    if coins[0] > amount:
        return change(amount, coins[1:])
    else:
        use = 1 + change(amount - coins[0], coins)
        lose = change(amount, coins[1:])
        return min(use,lose)
