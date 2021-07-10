'''
Created on 03/10/2021
@author:   Jonathan Amir
Pledge:    I pledge my honor that I have abided by the Stevens Honor System

CS115 - Lab
'''

import time
from cs115 import map

words = []
HITS = 10

def ED(first, second):     
    ''' Returns the edit distance between the strings first and second.'''      
    if first == '':          
        return len(second)     
    elif second == '':         
        return len(first)     
    elif first[0] == second[0]:         
        return ED(first[1:], second[1:])     
    else:         
        substitution = 1 + ED(first[1:], second[1:])         
        deletion = 1 + ED(first[1:], second)         
        insertion = 1 + ED(first, second[1:])         
        return min(substitution, deletion, insertion) 

def fastED(first, second):
    '''Returns the edit distance between the strings first and second. Uses
    memoization to speed up the process.'''
    def helper(first, second, memo):
        if (first, second) in memo:
            return memo[(first, second)]
        if first == '':          
            return len(second)     
        elif second == '':         
            return len(first)     
        elif first[0] == second[0]:         
            return helper(first[1:], second[1:],memo)     
        else:         
            substitution = 1 + helper(first[1:], second[1:],memo)         
            deletion = 1 + helper(first[1:], second,memo)         
            insertion = 1 + helper(first, second[1:],memo)
        memo[(first,second)] = min(substitution, deletion, insertion)
        return min(substitution, deletion, insertion)
    return helper(first, second, {})

def getSuggestions(user_input):
    '''For each word in the global words list, determine the edit distance of
    the user_input and the word. Return a list of tuples containing the
    (edit distance, word).
    Hint: Use map and lambda, and it's only one line of code!'''
    return map(lambda w: (fastED(user_input, w), w), words)

def spam():
    '''Main loop for the program that prompts the user for words to check.
    If the spelling is correct, it tells the user so. Otherwise, it provides up
    to HITS suggestions.

    To exit the loop, just hit Enter at the prompt.'''
    while True:
        user_input = input('spell check> ').strip()
        if user_input == '':
            break
        if user_input in words:
            print('Correct')
        else:
            start_time = time.time()
            suggestions = getSuggestions(user_input)
            suggestions.sort()
            endTime = time.time()
            print('Suggested alternatives:')
            for suggestion in suggestions[:HITS]:
                print(' %s' % suggestion[1])
            print('Computation time:', endTime - start_time, 'seconds')
    print('Bye')

if __name__ == '__main__':
    f = open('3esl.txt')
    for word in f:
        words.append(word.strip())
    f.close()
    spam()
