# examples shallow and deep copy

from cs115 import *

class Cat(object):
    '''simple example class with a mutable field'''
    def __init__(self, nam, ag):
        '''Represents a cat with name nam and age ag.'''
        self.__name = nam 
        self.__age = ag
    def __str__(self): return self.__name + " " + str(self.__age)
    def getName(self): return self.__name
    def getAge(self): return self.__age
    def setAge(self, a):
        self.__age = a
    def copy(self):
        return Cat(self.__name, self.__age)

fluffy = Cat("Fluffy", 5)
x = fluffy
y = fluffy.copy()
x.setAge(6)
print(fluffy.getAge()) # prints 6
print(y.getAge()) # prints 5

A = [x, y] 
B = A
C = list(A) # shallow copy

D = [] # make a new list, for deep copy
for cat in A:
    D.append(cat.copy()) 
    
y.setAge(7)
B[0] = Cat("tigger", 1) 
D[0].setAge(8)

print("A ", map(str, A))
print("B ", map(str, B))
print("C ", map(str, C))
print("D ", map(str, D))

    





