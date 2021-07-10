''' Jonathan Amir
I pledge my honor that I have abided by the Stevens Honor System
'''

from cs115 import *

def calculate_list(L):
    ''' a helper function to calculate the next row after row L'''
    if not L[1:]:
        return [1]
    return [L[0] + L[1]] + calculate_list(L[1:])

def pascal_row(R):
    ''' will return the list/row number of the integer input'''
    def calculate(i, l=[1], r=0):
        '''will call the calculate_list function to help fetch the list at row R'''
        if i == 0:
            return l
        if i == r:
            return l
        else:
            return calculate(i, [1]+calculate_list(l), r+1)
    return calculate(R)

def pascal_triangle(n):
    ''' Shows all the lists up to and inclusing row R'''
    def showRows(t, l=[[1]], c = 0):
        ''' will make use of calculate_list function to actually generate the lists'''
        if t == 0:
            return 
        if t == c:
            return l
        return showRows(t, l+[[1]+calculate_list(l[len(l)-1])], c+1)
    return showRows(n)

def test_pascal_row():
    ''' tests to make sure the pascal_row function works'''
    assert pascal_row(0) == [1]
    assert pascal_row(1) == [1,1]
    assert pascal_row(2) == [1,2,1]
    assert pascal_row(3) == [1,3,3,1]

def test_pascal_triangle():
    ''' tests to see if the pascal triangle function works'''
    assert pascal_triangle(0) == [[1]]
    assert pascal_triangle(1) == [[1],[1,1]]
    assert pascal_triangle(2) == [[1],[1,1],[1,2,1]]
    assert pascal_triangle(3) == [[1],[1,1],[1,2,1],[1,3,3,1]]
