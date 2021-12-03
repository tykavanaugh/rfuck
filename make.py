import sys
import re
import helpers
import os
import PyInstaller.__main__

def main():
    args_dict = arg_parser()
    execute_on_compile = args_dict['execute_on_compile']
    binary_compile = args_dict['binary_compile']
    #Store all variables in this hashtable Legacy
    helper = helpers.Helper()
    if len(sys.argv) < 2:
        print("No file supplied, quitting")
        print("Please specifiy source code")
        return
    #read in file
    in_file = open(args_dict['in_file'],'r')
    raw_input_code = in_file.readlines()
    in_file.close()

    #input_code is an array where each item is a statement
    input_code = helper.format_statements(raw_input_code)


    #check for invalid lines
    print("checking statements")
    for i,line in enumerate(input_code): 
        errors_found = False
        line_type = helper.identify_line_type(line)
        if "invalid type cannot be both" in line_type:
            print(f'Error line {i}: {line_type}')
            errors_found = True
        else:
            #for debugging
            print(f'{i}:{line_type}')
            pass
    if errors_found:
        print("Compilation Error")
        sys.exit()


    output_code = []
    for line in input_code:
        result =  helper.identify_and_return(line)
        if result:
            output_code.append(result)



    #Set outfile filename based on args
    if args_dict['out_file'] != '':
        out_file = open(args_dict['out_file'],'w')
    else:
        out_file_name = str(args_dict['in_file'])[:str(args_dict['in_file']).rfind('.')]+".py"
    
    #write file
    with open(out_file_name,'w') as out_file:
        for line in output_code:
            out_file.write((f'{line}\n'))
    
    #execute script
    print(f"File src generated at: {out_file_name}")
    
    if execute_on_compile:
        os.system(f'python3 {out_file_name}')

    #compile to binary

    if binary_compile:
        PyInstaller.__main__.run([
            f'{out_file_name}',
            '--onefile',
        ])


def arg_parser():
    out_dict = {
        "in_file":"",
        "out_file":"",
        "execute_on_compile":False,
        "binary_compile":False,

    }
    for arg in sys.argv[1:]:
        if "-" in arg:
            if arg == "-b" or arg == "--binary":
                out_dict["binary_compile"] = True
            if arg == "-e" or arg == "--execute":
                out_dict["execute_on_compile"] = True
        else:
            if out_dict["in_file"] == "":
                out_dict["in_file"] = arg
            else:
                out_dict["out_file"] = arg
    return(out_dict)

#Old notes

#Pronouns or "some" or "someone" at the start declare some statements

#define variables- standard variables are arrays of python ints
    #default to zero
    #"My/a/the [values], lets call them/him/her/it variable_name"
    # Must contain "call them/him/her/it/that "

#special variables- 
#   "best for the family/country/group" is True
#   "worse/not good for the family/country/group" is False




#compare variables start with "Pronoun argued"
    # var0 > var1 "Pronoun argued that var0 was better than var2 with var3"
    # var0 < var1 "Pronoun argued that var0 was worse than var2 with var3"
    # var0 == var1 "Pronoun argued that var0 was the same as var2 with var3"
    # var0 != var1 "Pronoun argued that var0 was nothing like var2 with var3"
    # var0 >= var1 "Pronoun argued that var0 was better or the same as var2 with var3"
    # var0 <= var1 "Pronoun argued that var0 was worse or the same as var2 with var3"

#operators start with "So then"
    # var0 + var1 "var0 gave x to var1"
    # var0 - var1 "var1 took/got x to/from var0"
    # var0 % var1 "var0 had x leftover after/left to do after x with var1"
    # var0 // var1 "var0 was torn on x when it came to var1"
    # var0 * var1  "var0 repeated x to var1"
    # assignment to var3 "{statement} and said/called/considered it var3"

#while "Pronoun calmly explained that"
    # while {}"Pronoun calmly explained that variable *" 
    # ends alls loops "stormed off" "left the party/room/dinner/meal" 
    # end specific loop "didn't want to talk about variable"

#if-then "Pronoun believed/that x"
    # for range(0,x,1)

#Reddit
    # special "output" variable

#stdout
    # x declared/told/proclaimed 
    # "AITA?" or "WIBTA?" on the last line should output Reddit to stdout



main()

