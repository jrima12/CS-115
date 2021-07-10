'''
Created on 05/12/2021
@author:   Jonathan Amir
Pledge:    I pledge my honor that I have abided by the Stevens Honor System

CS115 - Hw 13 - connect 4
'''

class Board(object):
    def __init__(self, width = 7, height = 6):
        '''constructor for the Board objects that sets the
        width height and board properties'''
        self.__width = width
        self.__height = height
        board = []
        for i in range(self.__height):
            row = []
            for j in range(self.__width):
                row += [' ']
            board += [row]
        self.__board = board


    def __str__(self):
        '''returns a string which represents how the board currently
        looks'''
        b = ""
        for i in range(self.__width-1):
            for j in self.__board[i]:
                b += "|"
                b += str(j)
            b += "|"
            b += "\n"
        for l in range(self.__width):
            b += "--"
        b += "-" + "\n"
        for n in range(self.__width):
            b += " " + str(n)
        return b

    def allowsMove(self, col):
        '''function that determines if moving to the input column is a propper
        move'''
        if col < self.__width and col >= 0 :
            for i in range(self.__height):
                if self.__board[i][col] == " ":
                    return True
        return False

    def addMove(self, col, ox):
        '''If it is a proper move, this function adds that move and updates
        how the board is'''
        if self.allowsMove(col):
            p = -1
            while True:
                if self.__board[p][col] == " ":
                    self.__board[p][col] = ox
                    break
                else:
                    p -= 1

    def setBoard( self, moveString ):
        """ takes in a string of columns and places
             alternating checkers in those columns,
             starting with 'X'
            
             For example, call b.setBoard('012345')
             to see 'X's and 'O's alternate on the
             bottom row, or b.setBoard('000000') to
             see them alternate in the left column.
             moveString must be a string of integers
         """
        nextCh = 'X' # start by playing 'X'
        for colString in moveString:
            col = int(colString)
            if 0 <= col <= self.width:
                self.addMove(col, nextCh)
            if nextCh == 'X':
                nextCh = 'O'
            else:
                nextCh = 'X'

    def winsFor(self, ox):
        '''checks the board for wins in the horizontal, vertical,
        bottom left to top right, and bottom right to top left, in that order'''
        for i in range(self.__height):
            for j in range(self.__width-3):
                if self.__board[i][j] == self.__board[i][j+1] == self.__board[i][j+2] == self.__board[i][j+3] == ox:
                    return True
        for i in range(self.__width):
            for j in range(self.__height-3):
                if self.__board[j][i] == self.__board[j+1][i] == self.__board[j+2][i] == self.__board[j+3][i] == ox:
                    return True
        for i in range(self.__height-3):
            for j in range(self.__width-3):
                if self.__board[i][j] == self.__board[i+1][j+1] == self.__board[i+2][j+2] == self.__board[i+3][j+3] == ox:
                    return True
        for i in range(self.__height-1, 2):
            for j in range(self.__width-3):
                if self.__board[i][j] == self.__board[i-1][j+1] == self.__board[i-2][j+2] == self.__board[i-3][j+3] == ox:
                    return True
            i -= 1

    def hostGame(self):
        '''gives a good gameplay, and allows the user to make moves'''
        print("Welcome to Connect Four")
        ox = "X"
        while True:
            print(self)
            if self.winsFor(ox):
                print(ox + " Wins!!")
                print(self)
                break
            col = int(input("player " + ox + " choose your column:"+"\n"))
            if self.allowsMove(col) == True:
                self.addMove(col, ox)
                if self.winsFor(ox):
                    print(ox + " Wins!!")
                    print(self)
                    break
                else:
                    if ox == "X":
                        ox = "O"
                    else:
                        ox = "X"
            else:
                print("Not a valid option, try again")
if __name__ == "__main__":
    '''runs the code'''
    b = Board()
    b.hostGame()
