# Enter your code here. Read input from STDIN. Print output to STDOUT

import random 
import sys 

#read code from STDIN
def read_from_stdin():
    states = input()
    states = eval(states)

    sigma = sys.stdin.readline()
    sigma = eval(sigma)

    dlt = sys.stdin.readline()
    dlt = eval(dlt)

    qs = sys.stdin.readline()
    qs = eval(qs)

    F = sys.stdin.readline()
    F = eval(F)
    
    symbol = sys.stdin.readline()
    symbol = eval(symbol)
    
    return states, sigma, dlt, qs, F, symbol


# create empty matrix given rows + columns 
def create_matrix_of_zeros(rows, cols):
    M = []
    for s in range(rows):
        M.append([])
        for r in range(cols):
            M[s].append(0)
    return M

# print the above matrix 
def print_matrix(A, padding):
    rows = len(A)
    cols = len(A[0])
    for i in range(rows):
        for j in range(cols):
            if j < cols-1:
                print (f"{A[i][j]: {padding}}", end = " ")
            else:
                print (f"{A[i][j]: {padding}}")
                
                
# main function 
def create_matrix_of_transitions_over_a_symbol():
    states, sigma, dlt, qs, F, symbol = read_from_stdin()
    
    # figure out rows/columns by taking the length of the states list 
    n = len(states)
    
    # initialize our matrix
    M = create_matrix_of_zeros(n, n)
    
    # actually fill in the matrix 
    for j in range(len(states)):
        s = states[j]
        if (s, symbol) in dlt:
            for target in dlt[(s, symbol)]:
                i = states.index(target)   # row index for target state
                M[i][j] = 1.0
                
    print_matrix(M, 4)
    
create_matrix_of_transitions_over_a_symbol()