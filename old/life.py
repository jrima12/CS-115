#
# life.py - Game of Life lab
#
# Name: Jonathan Amir
# Pledge: I pledge my honor that I have abided by the Stevens Honor System
#

import random
import sys

def createOneRow(width):
    """Returns one row of zeros of width "width"...  
       You should use this in your
       createBoard(width, height) function."""
    row = []
    for col in range(width):
        row += [0]
    return row

def createBoard(width, height):
    '''returns a 2d array with "height" rows and "width" cols'''
    board = []
    for row in range(height):
        board += [[0]*width]
    return board

def printBoard(A):
    '''prints the 2d list of lists "A" without spaces'''
    for row in A:
        for col in row:
            sys.stdout.write(str(col))
        sys.stdout.write('\n')
        
def diagonalize(width, height):
    ''' creates an empty board and then modifies it so that is has a
    diagonal strip of "on" cells'''
    A = createBoard(width, height)
    for row in range(height):
        for col in range(width):
            if row == col:
                A[row][col] = 1
            else:
                A[row][col] = 0
    return A

def innerCells(w,h):
    '''returns a board of all 1's except for the outside edges'''
    board = createBoard(w,h)
    for row in range(h):
        for col in range(w):
            if row == 0 or row == h-1 or col == 0 or col == h-1:
                board[row][col] = 0
            else:
                board[row][col] = 1
    return board

def randomCells(w,h):
    '''returns a list with 0's as outside edges and random arangement
    of 1's and 0's in the middle'''
    board = createBoard(w,h)
    for row in range(h):
        for col in range(w):
            if row == 0 or row == h-1 or col == 0 or col == w-1:
                board[row][col] == 0
            elif random.choice([0,1]) == 1:
                board[row][col] = 1
            else:
                board[row][col] = 0
    return board

def copy(A):
    '''copies list A and returns a list that will not change even when
    list A changes'''
    board = createBoard(len(A), len(A[0]))
    for row in range(len(A)):
        for col in range(len(A[0])):
            board[row][col] = A[row][col]
    return board

def innerReverse(A):
    '''Reverses the values from 1 to 0 or from 0 to 1 of the inside
    of the 2d list'''
    board = copy(A)
    for row in range(len(A)-1):
        for col in range(len(A[0])-1):
            if row != 0 and col != 0:
                board[row][col] = (A[row][col] + 1)%2
    return board

def next_life_generation(A):
    '''makes a copy of A and then advanced one generation of Conway's
    game of life within the inner cells of that copy. The outer edge
    always stays 0 '''
    newA = copy(A)
    for row in range(len(A)):
        for col in range(len(A[0])):
            if row == 0 or row ==len(A)-1 or col == 0 or col == len(A[0])-1:
                newA[row][col] = 0
            elif countNeighbor(row,col,A) < 2 or countNeighbor(row,col,A) > 3:
                newA[row][col] = 0
            elif A[row][col] == 0 and countNeighbor(row,col,A) == 3:
                newA[row][col] = 1
            else:
                newA[row][col] = A[row][col]

    return newA

def countNeighbor(row, col, A):
    '''a helper function for next_life_generation which counts how many
    neighbors each spot in array has'''
    num = 0
    for r in range(row-1, row+2):
        for c in range(col-1, col+2):
            if A[r][c] == 1:
                 num += 1
    if A[row][col] == 1:
        num = num - 1
    return num
