'''Jonathan Amir
I pledge my honor that I have abided by the Stevens Honor System
'''
from cs115 import *

L = [1,5,10,25,50]

def giveChange(amount, coins):
    '''Returns a number of the minimum amount of coins needed for change, and a list of the coins
'''
    if amount == 0:
        ''' if the amount is zero, then it takes zero coins to get to it '''
        return [0, []]
    elif coins == []:
        ''' if there are no coins, it will never reach the amount '''
        return [float("inf"), []]
    else:
        if coins[0] > amount:
            ''' If the coin is more than the amount, remove the coin '''
            return giveChange(amount, coins[1:])
        else:
            use = giveChange(amount-coins[0], coins)
            ''' use = the initial amount, minus the first coin '''
            uselist = [1+use[0], use[1] + [coins[0]]]
            ''' add 1 for every coin being used, and add that coin to the used coins list '''
            lose = giveChange(amount, coins[1:])
            ''' lose is dropping one coin to not use it ''' 
            if uselist[0] > lose[0]:
                return lose
            return uselist
