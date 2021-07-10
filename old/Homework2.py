'''
Created on February 22, 2021
@author:   Jonathan Amir, Template recieved from class
Pledge:    I pledge my honor that I have abided by the Stevens Honor System

CS115 - Hw 2

WARNING: with the imported dictionary, this code took roughly 7 minutes to run
'''
import sys
from cs115 import map, reduce, filter
#from dict import Dictionary
# Be sure to submit hw2.py.  Remove the '_template' from the file name.

# Allows up to 10000 recursive calls.
# The maximum permitted limit varies from system to system.
sys.setrecursionlimit(10000)

# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']

# Implement your functions here.

'''Takes two values, one string (character) and one list, and will retrieve
the predetermined numerical value for the input letter'''
def letterScore(letter, scorelist):
    if scorelist[0][0] == letter:
        return scorelist[0][1]
    else:
        return letterScore(letter, scorelist[1:])

'''Takes a string (word) and a list, and will give the score of that word
based off the list'''
def wordScore(S, scorelist):
    if S =='':
        return 0
    else:
        return letterScore(S[0], scorelist) + wordScore(S[1:], scorelist)

'''SCRABBLE GAME BELOW'''

def checkLetter(Word, Rack):
    ''' Checks to see if letters in word in Dictionary are in rack'''
    Word = sorted(Word)
    if Word == []:
        return True
    if Rack == []:
        return False
    if Word[0] in Rack:
        ind = Rack.index(Word[0])+1
        return checkLetter(Word[1:], Rack[ind:])
    else:
        return False

def TFList(Dict, Rack):
    Rack.sort()
    '''this function builds a True/False list based on which words in dictionary can be built from rack'''
    if Dict == []:
        return []
    else:
        return [checkLetter(Dict[0], Rack)] + TFList(Dict[1:], Rack)

def filFunc(Dict, Rack):
    '''this will filter the words in the dictionary based off the true and false list in the TFList function'''
    tflist = TFList(Dict, Rack)
    if tflist == []:
        return []
    if tflist[0] == True:
        return [Dict[0]] + filFunc(Dict[1:], Rack)
    if tflist[0] == False:
        return [] + filFunc(Dict[1:], Rack)



def scoreList(Rack):
    '''Will return possible words that can be made, and their score'''
    wordlist = filFunc(Dictionary, Rack)
    def listOfWords(L, score):
        ''' this will return the list of words plus the scores'''
        if L == []:
            return []
        else:
            return [L[0] + ", " + str(wordScore(L[0], score))] + listOfWords(L[1:], score)
    return listOfWords(wordlist, scrabbleScores)



def bestWord(Rack):
    '''Will get all the words that can be made and then return the one with the highest value'''
    wordlist = filFunc(Dictionary, Rack)
    print("Possible words: ")
    print(scoreList(Rack))
    def getScore(L, scorelist):
        '''gets the scores of each of the words based on the wordScore function'''
        if L == []:
            return []
        else:
            return [wordScore(L[0], scrabbleScores)] + getScore(L[1:], scrabbleScores)
    totalscorelist = getScore(wordlist, scrabbleScores)
    print("best word:")
    return [str(max(totalscorelist))]+ [(wordlist[totalscorelist.index(max(totalscorelist))])]


    
