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
    
    input_string = sys.stdin.readline()
    input_string = eval(input_string)
    
    return states, sigma, dlt, qs, F, input_string 

# global variables
states, sigma, dlt, qs, F, input_string = read_from_stdin()

# create empty matrix given rows + columns 
def create_matrix_of_zeros(rows, cols):
    M = []
    for s in range(rows):
        M.append([])
        for r in range(cols):
            M[s].append(0.0)
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
             
def create_matrix_of_transitions_over_a_symbol(target):    
    # figure out rows/columns by taking the length of the states list 
    n = len(states)
    
    # initialize our matrix
    M = create_matrix_of_zeros(n, n)
    
    # actually fill in the matrix 
    for j in range(len(states)):
        s = states[j]
        if (s, target) in dlt:
            for next in dlt[(s, target)]:
                i = states.index(next)   # row index for target state
                M[i][j] = 1.0
                
    return M

# start of code for Task 2 -> 

# function to print column matrix/identity matrix corresponding to start state
def print_start_state(states, qs):
    n = len(states)
    M = create_matrix_of_zeros(n, 1)
    M[states.index(qs)][0] = 1.0 
    return M

# function to write for Task 2
def find_state_and_matrix(input_string):
    # turn string into lsit of characters 
    char_list = list(input_string)
    
    # intialize a list to hold matrices produced by input string
    M_list = []
    
    # for loop to create a matrix that corresponds to every character in the string
    for c in char_list:
        M_list.append(create_matrix_of_transitions_over_a_symbol(c))    

    # create matrix for start state
    column = print_start_state(states, qs)
    
    # create final matrix to be displayed
    final_matrix = mult_matrix_list(M_list[::-1])
    
    # multiple that matrix with the start state identity matrix to find the landing state 
    final_vector = mult_matrices(final_matrix, column)
    
    # compute the final state 
    final_state = final_vector.index([1.0])
    
    # do the printing of matrix + final state 
    print(final_state)
    #print(final_vector)
    print_matrix(final_matrix, 4)

find_state_and_matrix(input_string)

