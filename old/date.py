'''
Created on 05/05/2021
@author:   Jonathan Amir
Pledge:    I pledge my honor that I have abided by the Stevens Honor System

CS115 - Hw 12 - Date class
'''
DAYS_IN_MONTH = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

class Date(object):
    '''A user-defined data structure that stores and manipulates dates.'''

    # The constructor is always named __init__.
    def __init__(self, month, day, year):
        '''The constructor for objects of type Date.'''
        self.month = month
        self.day = day
        self.year = year

    # The 'printing' function is always named __str__.
    def __str__(self):
        '''This method returns a string representation for the
           object of type Date that calls it (named self).

             ** Note that this _can_ be called explicitly, but
                it more often is used implicitly via the print
                statement or simply by expressing self's value.'''
        return '%02d/%02d/%04d' % (self.month, self.day, self.year)

    def __repr__(self):
        '''This method also returns a string representation for the object.'''
        return self.__str__()

    # Here is an example of a 'method' of the Date class.
    def isLeapYear(self):
        '''Returns True if the calling object is in a leap year; False
        otherwise.'''
        if self.year % 400 == 0:
            return True
        if self.year % 100 == 0:
            return False
        if self.year % 4 == 0:
            return True
        return False

    def copy(self):
        '''Returns a new object with the same month, day, yearas the calling object (self).'''
        dnew = Date(self.month, self.day, self.year)
        return dnew

    def equals(self, d2):
        '''decides if self and d2 represent the same calendar date, whether or not they are in thesame place in memory'''
        return self.year == d2.year and self.month == d2.month and self.day == d2.day

    def tomorrow(self):
        '''changes calling object so that it represents one calendar
        day after the date it originally represented'''
        #DAYS_IN_MONTH = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self.isLeapYear() == True:
            DAYS_IN_MONTH[2] = 29
        else:
            DAYS_IN_MONTH[2] = 28
        if self.day == DAYS_IN_MONTH[self.month]:
            if self.month == 12:
                self.day = 1
                self.month = 1
                self.year += 1
            else:
                self.day = 1
                self.month += 1
        else:
            self.day += 1

    def yesterday(self):
        '''changes calling object so that it represents one calendar
        day before the date it originally represented'''
        #DAYS_IN_MONTH = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self.isLeapYear() == True:
            DAYS_IN_MONTH[2] = 29
        else:
            DAYS_IN_MONTH[2] = 28
        if self.day == 1:
            if self.month == 1:
                self.day = 31
                self.month = 12
                self.year -= 1
            else:
                self.month -= 1
                self.day = DAYS_IN_MONTH[self.month]
        else:
            self.day -= 1

    def addNDays(self, N):
        '''changes calling object so that it represents N calendar
        days after the original date'''
        print(self)
        for i in range(N):
            self.tomorrow()
            print(self)

    def subNDays(self, N):
        '''changes calling object so that it represents N calendar
        days before the original date'''
        DAYS_IN_MONTH = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self.isLeapYear() == True:
            DAYS_IN_MONTH[2] = 29
        else:
            DAYS_IN_MONTH[2] = 28
        print(self)
        for i in range(N):
            self.yesterday()
            print(self)

    def isBefore(self, d2):
        ''' returns True if the calling object is before the input date
        and false otherwise'''
        if self.year < d2.year:
            return True
        if self.year > d2.year:
            return False
        if self.month < d2.month:
            return True
        if self.month > d2.month:
            return False
        if self.day < d2.day:
            return True
        if self.day > d2.day:
            return False
        return False

    def isAfter(self, d2):
        ''' returns True if the calling object is after the input date
        and false otherwise'''
        if self.year < d2.year:
            return False
        if self.year > d2.year:
            return True
        if self.month < d2.month:
            return False
        if self.month > d2.month:
            return True
        if self.day < d2.day:
            return False
        if self.day > d2.day:
            return True
        return False
        
    def diff(self, d2):
        '''Calculates how many days apart the calling object is from the
        input date. returns negative if calling object is before input date.'''
        D1 = self.copy()
        D2 = d2.copy()
        c = 0
        if D1.isBefore(D2) == True:
            while D1.isBefore(D2) == True:
                D1.tomorrow()
                c += 1
            return c*(-1)
        if D1.isBefore(D2) == False:
            while D1.isAfter(D2) == True:
                D1.tomorrow()
                c += 1
            return c
        return c

    def dow(self):
        '''returns the day of the week the calling object falls on'''
        DOW = ['Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'Monday', 'Tuesday']
        d = Date(11, 9, 2011)
        listin = abs(d.diff(self)) % 7
        return DOW[listin]
        
