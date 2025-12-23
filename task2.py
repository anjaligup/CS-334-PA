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
    
    index_list = sys.stdin.readline()
    index_list = eval(index_list)
    
    return terminals, variables, productions, string, index_list

terminals, variables, productions, string, index_list = read_from_stdin()

# function from last task
def apply_single_production_left(string, index):    
    # find leftmost variable in the string (aka the first variable in string)
    var = None 
    for character in string:
        if character in variables:
            var = character
            break
            
    if var is None:
        return string

    # use index to find the production that needs to be used
    prod = productions[var][index]

    # replace the variable in the string with the production
    new_string = string.replace(var, prod, 1)
    return new_string

# function for this task
def apply_productions_left(string, index_list):
    #loop through index list and apply every index to the string
    for index in index_list:
        string = apply_single_production_left(string, index)
    print(string)
    
apply_productions_left(string, index_list)
        
    