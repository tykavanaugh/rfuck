import sys
import re
import helpers
# import PyInstaller.__main__

# PyInstaller.__main__.run([
#     'my_script.py',
#     '--onefile',
#     '--windowed'
# ])



def main():
    #Store all variables in this hashtable
    helper = helpers.Helper()
    if len(sys.argv) < 2:
        print("No file supplied, quitting")
        print("Please specifiy source code")
        return
    #read in file
    in_file = open(sys.argv[1],'r')
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
        return

    helper.parse_assignment("my buddy, for clarity lets call it green, is very okay")
    helper.parse_assignment("my buddy, for ease lets call him bob, is not super okay")
    helper.parse_compare("I argued that green wasn't enough and was better than bob with gusto")
    print(helper.variable_table)



    #Set outfile filename based on args- future addition
    # if len(sys.argv) > 2:
    #     out_file = open(sys.argv[2],'w')
    # else:
    #     out_file_name = str(sys.argv[1])[:str(sys.argv[1]).rfind('.')] + '.redditlang'
    
    #write file- future addition
    # with open(out_file_name,'w') as out_file:
    #     for line in input_code:
    #         out_file.write((f'{line}\n'))

#features

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

