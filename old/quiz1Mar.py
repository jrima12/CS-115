# CS 115A Spring 2021 pop quiz March 1

###########################################################################
# RULES: You can use the following:
# Canvas to download+upload the 
# IDLE to edit this file and check your solutions
# Zoom for the class meeting; use private chat to Dave or TAs if needed.
#
# Hint: If some of your code doesn't work, comment it out and write a note.
# 
# Name and pledge:
#Jonathan Amir
# I pledge my honor that I have abided by the Stevens Honor System
#
#
###########################################################################

###########################################################################
# STEP ZERO:
# Please run this file right now to be sure you downloaded it ok, and have 
# cs115.py in the same folder.  There should be no error.
###########################################################################

from cs115 import *

###########################################################################
# STEP ONE:
# Using the definition of LCS below, show the trace of function calls
# for the expression LCS("hi", "bi").  Use indentation to show which 
# calls result from previous calls.
###########################################################################

def LCS(S1, S2):
    """Length of longest common subsequence of two lists."""
    if S1 == "" or S2 == "": return 0
    elif S1[0] == S2[0]:  
        return 1 + LCS(S1[1:], S2[1:])
    else:
        return max(LCS(S1, S2[1:]), LCS(S1[1:], S2))

"""
LCS looks to see if either of the two inputs are empty strings and returns 0 if they are
otherwise, if the zero'th element of each string are the same, then return 1 plus the string minus the first character
if neither of the cases, it returns the maximum between the same function and itself but where in one case the first string removes the first character, and in the second case, the second letter removes the first character
"""

###########################################################################
# STEP TWO:
# Complete the definition of rev below, so that reverse_alt works correctly.
# Your code should be tail-recursive, using the parameter acc as accumulator.
###########################################################################


def reverse(L):
    '''reverse a list'''
    if L == []: return []
    else: return reverse(L[1:]) + [L[0]]

def reverse_alt(L):
    def rev(acc, L):
        '''.....define this using recursion on L,
        so we can use L==[], L[0], and rev(...,L[1:])'''
        print(acc)
        if L == []:
            return []
        else:
            acc = rev(acc, L[1:])+[L[0]]
            return acc

    return rev([], L)

    # Hint: if you traced the calls, it would look like this:
    #     reverse_alt([1,2,3,4])
    #       rev([], [1,2,3,4])
    #         rev([1], [2,3,4])
    #           rev([2,1],[3,4])
    #             rev([3,2,1],[4])
    #               rev([4,3,2,1],[])
                  

def testReverse():
    assert reverse(['hi','there']) == reverse_alt(['hi','there'])
    assert reverse(range(10)) == reverse_alt(range(10))
    assert reverse([]) == reverse_alt([])


