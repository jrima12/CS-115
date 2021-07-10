# Example showing how to trace a for-loop

def squareSums(n):
    '''list of the first n sums of squares'''
    L = []
    s = 0
    for i in range(1,n+1):
        s += i*i
        L.append(s)
    return L

# The loop changes L, s, and i, so we make a table
# of their values.  For the call squareSumsTrace(5)
# it looks like this:

#  s  i  L 
#  ----------------------
#  0 1 []
#  1 2 [1]
#  5 3 [1, 5]
#  14 4 [1, 5, 14]
#  30 5 [1, 5, 14, 30]
#  55 5 [1, 5, 14, 30, 55]


# Below is code that automatically prints the trace.
# In binsearchExSol there is a self-tracing loop
# where the first line of the table is from a print
# statement that precedes the loop.  For a for-loop,
# the for-variable doesn't have a value until the loop
# starts, so we put the print statement at the top
# of the loop body.  And then we need an extra print
# statement for the values after the last iteration.

def squareSumsTrace(n):
    '''self-tracing version of squareSums'''
    L = []
    s = 0
    print("s  i  L \n -----------------")
    for i in range(1,n+1):
        print(s,i,L)
        s += i*i
        L.append(s)
    print(s,i,L,"\n") 
    return L
