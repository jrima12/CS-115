from cs115 import *

'''
For truth table, focus on cases it is true
and write combination of ands combined by ors
(like in discrete)
example format
(x and not y and not z) or (not x and y and z) or (x and y and z)
'''

'''
assert format: assert f(x,y,z) == output
EAMPLE:
'''
assert sum([1,2]) == 3


'''
2's compliment!!!
put number in standard binary, then invert 1s to 0s and 0s to 1s
add 1 to bit at the end
if number starts with 1, it is negative
if number starts with 0 it is positive

for standard binary, highest number is 2^n - 1
for 3 bits, highest number is 7 (0,1,2,3,4,5,6,7)
for 2s compliment, highest positive number = 2^(n-1) - 1
                  lowest (negative) number = 2^(n-1)

find negative 27:
in standard binary with 8 bits, positive 27 = 00011011
in 2's compliment:                            11100100 + 1 = 11100101
'''

'''
MEMOIZATION
initialize dictionary 
check if values are in dictionary, if yes, give result
if no, continue with code
plug in the result to the dictionary

Example:
#initialize
D = {}

#check for values
if (parameter1,parameter2,...) in D:
    return D[(parameter1, parameter2,...)]
.
. code goes here
.
D[(paramter1, parameter2,...)] = result

return result
'''











