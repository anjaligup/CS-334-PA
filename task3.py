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
                
# multiply two matrices (from prof)
def mult_matrices(A, B):
    if len(A[0]) != len(B):
        raise Exception("The matrices are not compatible")
    C = create_matrix_of_zeros(len(A), len(B[0]))
    for i in range(len(A)):
        for j in range(len(B[0])):
            a_ij = 0
            for s in range(len(A[0])):
                a_ij += A[i][s]*B[s][j]
                C[i][j]=a_ij
    return C

# multiply a list of matrices (from prof)
def mult_matrix_list(matrices: list):
    num_matrices = len(matrices)
    C = matrices[0]
    for s in range(1, num_matrices):
        C = mult_matrices(C, matrices[s])
    return C


# begin code for Task 3:
def create_matrix_of_transitions_over_a_symbol():
    states, sigma, dlt, qs, F, symbol = read_from_stdin()
    
    # figure out rows/columns by taking the length of the states list 
    n = len(states)
    
    # initialize our matrix
    M = create_matrix_of_zeros(n, n)
    
    # actually fill in the matrix 
    for j in range(len(states)):
        s = states[j]
        transitions = dlt.get((s, symbol), [])
        for target in transitions:
            i = states.index(target)   # row index for target state
            M[i][j] += 1.0
                
    # do the normalization part
    for j in range(n):
        col_sum = 0
        for i in range(n):
            col_sum += M[i][j]
        if col_sum != 0:
            for i in range(n):
                M[i][j] = M[i][j] / col_sum
               
    # turn float 0.0 into integer 0
    for i in range(n):
        for j in range(n):
            if M[i][j] == 0.0:
                M[i][j] = int(M[i][j])
                
    print_matrix(M, 4)
    
create_matrix_of_transitions_over_a_symbol()