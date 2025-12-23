import sys 

def read_from_stdin():
    productions = sys.stdin.readline()
    productions = eval(productions)
    return productions
    
productions = read_from_stdin()

def generate_options_dictionary(productions):
    new_dict = {}
    for key, values in productions.items():
        val = len(values)
        new_dict[key] = val
    print(new_dict)
    
generate_options_dictionary(productions)