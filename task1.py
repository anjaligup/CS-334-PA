import sys

def read_from_stdin():
    terminals = sys.stdin.readline()
    terminals = eval(terminals)

    variables = sys.stdin.readline()
    variables = eval(variables)

    productions = sys.stdin.readline()
    productions = eval(productions)

    string = sys.stdin.readline()
    string = eval(string)
    
    index = sys.stdin.readline()
    index = eval(index)
    
    return terminals, variables, productions, string, index

#read variables from stdin
terminals, variables, productions, string, index = read_from_stdin()

def apply_single_production_left(string, index):    
    # find leftmost variable in the string (aka the first variable in string)
    var = None 
    for character in string:
        if character in variables:
            var = character
            break
            
    if var is None:
        print(string)
    else:
        # use index to find the production that needs to be used
        prod = productions[var][index]

        # replace the variable in the string with the production
        new_string = string.replace(var, prod, 1)

        print(new_string)
    
apply_single_production_left(string, index)