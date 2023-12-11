import sys
from vectortoolkit import vector_tools

def help_function():
    """A helper function that prints out all of the command line functions avaliable to the user.
    """
    print("Usage:")
    print(" vectortoolkit <command> [arguments]")
    print("\n")
    print("Commands:")
    print(" -d          Calculate dot product of two vectors")
    print(" -c          Calculate cross product of two vectors")
    print(" -di         Calculate distance between two points")
    print(" -a          Caclulate the angle between two vectors")
    print(" -p          Calculate the projection of one vector onto another")
    print(" -n          Calculate the unit vector of a given vector ")
    print(" -help       Show help for commands")
    print("\n")
    print("Example usages:")
    print("python -m vectortoolkit -d [1, 5, 7] [8, -24, 2]")
    print("python -m vectortoolkit -a [0.6, 532, -7] [7, 4, -43]")


# dictionary to convert between arg flag and the functionality of that arg flag
function_lookup = {
    "-d": {"func": vector_tools.VectorTools.dot_product, "n_args":2},
    "-c": {"func": vector_tools.VectorTools.cross_product, "n_args":2},
    "-di": {"func": vector_tools.VectorTools.calculate_distance, "n_args":2},
    "-a": {"func": vector_tools.VectorTools.calculate_angle, "n_args":2},
    "-p": {"func": vector_tools.VectorTools.calulate_vector_projection, "n_args":2},
    "-u": {"func": vector_tools.Vector3D.get_unit_vector, "n_args":1},
    "-help": {"func": help_function, "n_args":0}
}


if __name__ == "__main__":
    """Called from the command line. Provides command line functionality.
    """
    # gets the functionality flag eg: -d or -help
    selected_function = sys.argv[1]

    # if the flag exists
    if function_lookup.get(selected_function) is not None:
        # check if the functionality requires 0 arguments
        if function_lookup[selected_function]["n_args"] == 0:
            # run the function
            function_lookup[selected_function]["func"]()
            
        # check if the functionality requires 1 argument
        elif function_lookup[selected_function]["n_args"] == 1:
            # get the argument and convert it into a list of floats
            arg = list(map(float, sys.argv[2].strip("[]").split(",")))
            
            # convert the list into a vectortoolkit vector
            vector = vector_tools.Vector3D(arg[0], arg[1], arg[2])
            
            result = function_lookup[selected_function]["func"](vector)
            
            print(result)
        
        # check if the functionality requires 2 arguments
        elif function_lookup[selected_function]["n_args"] == 2:
            
            # get both the arguments and convert them into lists of floats
            arg_1 = list(map(float, sys.argv[2].strip("[]").split(",")))
            arg_2 = list(map(float, sys.argv[3].strip("[]").split(",")))
            
            # convert them into vectortoolkit vectors
            vec_a = vector_tools.Vector3D(arg_1[0], arg_1[1], arg_1[2])
            vec_b = vector_tools.Vector3D(arg_2[0], arg_2[1], arg_2[2])
            
            result = function_lookup[selected_function]["func"](vec_a, vec_b)
            
            print(result)
            
    else:
        # if the flag does not exist print error message
        print("No such option: ", selected_function)
        print("For help use -help")


    
    
    
    