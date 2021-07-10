'''
Created on 03/23/21
@author:   Jonathan Amir
Pledge:    I pledge my honor that I have abided by the Stevens Honor System

CS115 - Hw 6
'''
# Number of bits for data in the run-length encoding format.
# The assignment refers to this as k.
COMPRESSED_BLOCK_SIZE = 7

# Number of bits for data in the original format.
#If compressed block size is 7, max run length is 127
MAX_RUN_LENGTH = 2 ** COMPRESSED_BLOCK_SIZE - 1 

# Do not change the variables above.
# Write your functions here. You may use those variables in your code.
def isOdd(n):
    '''Returns whether or not the integer argument is odd.'''
    return n%2 != 0

def numToBinary(n):
    '''make decimal number into binary number'''
    if n == 0:
        return ''
    if n >= 1:
        numToBinary(n//2)
    x = numToBinary(n//2) + str(n%2)
    return x

def convertLength(s):
    '''make binary number to standard length of bits'''
    return (COMPRESSED_BLOCK_SIZE - len(s))*"0" + s

def binaryToNum(s):
    '''converts binary number to decimal number'''
    if s == "":
        return 0
    if isOdd(int(s[len(s)-1])):
        return binaryToNum(s[:(len(s)-1)])*2+1
    return binaryToNum(s[:(len(s)-1)]) * 2

def CountZero(S):
    '''counts the number of consecutive zeros'''
    if S == "":
        return 0
    if S[0] == "0":
        return 1 + CountZero(S[1:])
    else:
        return 0
    
def CountOne(S):
    '''counts the numbers of consecutive ones'''
    if S == "":
        return 0
    if S[0] == "1":
        return 1 + CountOne(S[1:])
    else:
        return 0

def compress(S):
    '''returns a binary number in which each bits shows how many zeros or ones there are in input string S (alternating in that order)'''
    '''
    The largest number of bits I would need to use is for 64 bits of S in the
    checkerboard pattern. That would be a total of 58 compressed sequences. If the COMPRESSED_BLOCK_SIZE
    is 7 bits (which I changed it to, then there would be 7*58 compressed sequences. So
    a total of 406 bits
    '''
    if S == '':
        return ''
    numz = CountZero(S[:MAX_RUN_LENGTH])
    numo = CountOne(S[numz:numz+MAX_RUN_LENGTH])
    return convertLength(numToBinary(numz)) + convertLength(numToBinary(numo)) + compress(S[numz+numo:]) 
        

def uncompress(C):
    """takes a compressed string as input and returns the binary number decompressed"""
    if C == "":
        return ""
    zero = "0" * binaryToNum(C[:7])
    one = "1" * binaryToNum(C[7:14])
    return zero+one+uncompress(C[14:])

def compression(S):
    """returns the ratio of compressed and uncompressed sizes of a string of binary"""
    return len(compress(S))/len(S)


"""
Proof by contradiction for Professor Lai:
suppose S == chess board = 101010101010101010101010101010101010101010101010101010101010101010 (64 bits)
eve using the shortest possible length for compression (one bit) do describe how many ones and zeroes there are
(in this case starting with one), you still get a string of 64 1's (1111111111111111111111111111111111111111111111111111111111111111)
therefore the compression is not shorter (it is the same length)
"""
