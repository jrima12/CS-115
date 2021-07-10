# nim template DNaumann (2018), for assignment nim_hw11.txt 

# Global variables used by several functions
'''
Jonathan Amir
I pledge my honor that I have abided by the Stevens Honor System
'''
piles = []         # list containing the current pile amounts
num_piles = 0      # number of piles, which should equal len(pile)


def play_nim():
    """ plays game of nim between user and computer; computer plays optimally """
    
    init_piles()
    display_piles()
    while True:
        user_plays()
        display_piles()
        if sum(piles) == 0:

            print("You Win")

            break
        computer_plays()
        display_piles()
        if sum(piles) == 0:

            print("I WIN")

            break


def init_piles():
    """ Assign initial values to the global variables 'num_piles' and
        'piles'
        User chooses number of piles and initial size of each pile.
        Keep prompting until they enter valid values."""
    global piles
    global num_piles
    
    while True:
        piles = []
        num_piles = int(input("How many piles do you want to play with? "))
        try:
            val = int(num_piles)
        except ValueError:
            print("Please input an integer")
            
        for i in range(val):
                num = int(input("how many in pile " + str(i) + "? "))
                piles += [num]
        break
     
def display_piles():
    """ display current amount in each pile """
    global piles
    global num_piles

    for i in range(num_piles):
        print("pile "+str(i)+" :"+str(piles[i]))


def user_plays():
    """ get user's choices and update chosen pile """
    global piles
    
    print("Your turn ...")
    p = get_pile()
    amt = get_number(p)
    piles[p] = piles[p] - amt


def get_pile():
    """ return user's choice of pile
        Keep prompting until the choice is valid, i.e.,
        in the range 0 to num_piles - 1. """
    global piles
    global num_piles

    while True:
        p = int(input("which pile would you like to take from? "))
        if p in range(num_piles):
            return p
        else:
            print("number not in range")


def get_number(pnum):
    """ return user's choice of how many to remove from pile 'pnum'
        Keep prompting until the amount is valid, i.e., at least 1
        and at most the amount in the pile."""
    global piles
    
    while True:
        takeout = int(input("How many would you like to remove? "))
        if takeout in range(1, piles[pnum]+1):
            return takeout
        else:
            print("not in range")


def game_nim_sum():
    """ return the nim-sum of the piles """
    global piles
    global num_piles
    nimsum = 0 
    for i in range(num_piles):
        nimsum = nimsum ^ piles[i]
    return nimsum


def opt_play():
    """ Return (p,n) where p is the pile number and n is the amt to
        remove, if there is an optimal play.  Otherwise, (p,1) where
        is the pile number of a non-zero pile.

        Implement this using game_nim_sum() and following instructions
        in the homework text."""
    global piles
    global num_piles 
    nimsum = game_nim_sum()
    for i in range(num_piles):
        pilesum = nimsum ^ piles[i]
        if pilesum < piles[i]:
            return [i,piles[i]-pilesum]
    for i in range(num_piles):
        if piles[i] != 0:
            return[i,1]
        


def computer_plays():
    """ compute optimal play, update chosen pile, and tell user what was played

        Implement this using opt_play(). """
    global piles
    global num_piles

    play = opt_play()
    piles[play[0]] = piles[play[0]] - play[1]

    print(str(play[1]) + " was removed from pile " + str(play[0]))


#   start playing automatically
if __name__ == "__main__" : play_nim()
