class Helper:
    def __init__(self):
        self.variable_table = {
            'reddit':'yta',
            }
        self.pronouns = ['i','he','she','we','they','someone','something','it','ze']
        self.second_person_pronouns = ['them','you','her','him','zem','those','it']
        self.current_indent = 0

    def identify_and_return(self,line):
        tab = f'\t'
        if self.identify_line_type(line) == "assignment":
            return f"{tab*self.current_indent}{self.parse_assignment(line)}"
        if self.identify_line_type(line) == "comparison":
            return f"{tab*self.current_indent}{self.parse_compare(line)}"
        if self.identify_line_type(line) == "while":
            return self.parse_while(line)
        if self.identify_line_type(line) == "whilebreak":
            return self.parse_endwhile(line)
        if self.identify_line_type(line) == "stdout":
            return f"{tab*self.current_indent}{self.parse_stdout(line)}"


    def sum_words(self, str_slice):
        out_val = 0
        if " " not in str_slice:
            return len(str_slice)
        words_list = str_slice.split()
        words_list.reverse()
        for i,word in enumerate(words_list):
            if word != "nothing" or word != "none" or word != 'no' or word != 'not':
                out_val += len(word) * 10**i
        return out_val

    def assign_variable(self,var_name,value=0):
        var_name = var_name.lower()
        self.variable_table[var_name] = value
        return f'variable_{var_name} = {value}'

    #Parser functions
    def parse_assignment(self,line):
        for pronoun in self.second_person_pronouns:
            if f'lets call {pronoun}' in line:
                item_len = len(f'lets call {pronoun}')
                start_loc = line.rfind(f'lets call {pronoun}')+item_len
                end_loc = start_loc + line[start_loc+1:].find(" ")
                if end_loc < start_loc:
                    var_name = line[start_loc:]
                    var_name = var_name.strip()
                else:
                    var_name = line[start_loc+1:end_loc+1]
                    var_name = var_name.strip()
                    if var_name[-1] == ",":
                        var_name = var_name[:-1]
                        var_name = var_name.strip()
        #check for boolean assignment
        special_list = ['family','country','group']
        for item in special_list:
            if f'best for the {item}' in line:
                return self.assign_variable(var_name,True)
            if f'worse for the {item}' in line:
                return self.assign_variable(var_name,False)
        #int assignment
        if f'{var_name}, is nothing' in line:
            return self.assign_variable(var_name,0)
        if f'{var_name}, is not' in line:
            start_loc = line.rfind(f'{var_name}, is not') + len(f'{var_name}, is not')
            value = self.sum_words(line[start_loc:])
            return self.assign_variable(var_name,value*-1)
        if f'{var_name}, is' in line:
            start_loc = line.rfind(f'{var_name}, is') + len(f'{var_name}, is')
            value = self.sum_words(line[start_loc:])
            return self.assign_variable(var_name,value)
        return self.assign_variable(var_name)

    def parse_compare(self,line):
        current_operator = ''
        operators_list = [
            ('was better than ',lambda x,y:x>y,'>'),
            ('was worse than ',lambda x,y:x<y,'<'),
            ('was the same as ',lambda x,y:x==y,'=='),
            ('was nothing like ',lambda x,y:x!=y,'!='),
            ('was better or the same as ',lambda x,y:x>=y,'>='),
            ('was worse or the same as ',lambda x,y:x<=y,'<='),
        ]
        for operator in operators_list:
            if operator[0] in line:
                current_operator = operator
        start0 = line.rfind('argued that ') + len('argued that ')
        end0 = start0 + line[start0+1:].find(" ") + 1
        start1 = line.rfind(current_operator[0]) + len(current_operator[0])
        end1 = start1 + line[start1+1:].find(" ") + 1
        start2 = line.rfind("with ") + len("with ")
        end2 = start2 + line[start2+1:].find(" ") + 1
        var0 = line[start0:end0]
        var1 = line[start1:end1]
        if end2 >= start2:
            var2 = line[start2:]
        else:
            var2 = line[start2:end2]
        return f'variable_{var2} = variable_{var0} {current_operator[2]} variable_{var1}'
        #self.assign_variable(var2,(current_operator[1](var0,var1)))
    
    def parse_while(self,line):
        for pronoun in self.pronouns:
            match_statement = f'{pronoun} calmly explained to '
            if match_statement == line[:len(match_statement)]:
                start = line.rfind(match_statement) + len(match_statement)
                end = start + line[start+1:].find(" ") + 1
                var_name = line[start:end+1]
                self.current_indent = 1
                return f'while variable_{var_name}:'

    def parse_endwhile(self,line):
        self.current_indent = 0

    def parse_stdout(self,line):
        for pronoun in self.pronouns:
            match_statements = [
                f'{pronoun} told',
                f'{pronoun} declared',
                f'{pronoun} proclaimed',
                f'{pronoun} yelled',
                f'{pronoun} screamed',
            ]
            for match_statement in match_statements:
                if match_statement == line[:len(match_statement)]:
                    start = line.rfind('that ') + len('that ')
                    end = start + line[start+1:].find(" ") + 1
                    var_name = line[start:end+1]
                    return f'print(chr(variable_{var_name}),end="")'

    def format_statements(self,raw_lines_array):
        #break sentences and paragraphs into statements
        output_array = []
        for line in raw_lines_array:
            tmp = str(line)
            tmp = tmp.lower()
            while (tmp.find('.') != -1):
                output_array.append(tmp[0:(tmp.find('.'))])
                tmp = tmp[tmp.find('.')+1:]
            if (tmp[len(tmp)-1] == "\n"):
                output_array.append(tmp[:-1])
            else:
                output_array.append(tmp)
        #drop empty lines
        clean_output_array = []
        for line in output_array:
            if line:
                clean_output_array.append(line)
        return clean_output_array

    def identify_line_type(self,line):
        line_type = []
        if self.is_comment_statement(line):
            return "comment"
        #Check comparison statement
        if self.is_comparison_statement(line):
            line_type.append('comparison')
        #Check operator statement
        if self.is_operator_statement(line):
            line_type.append('operator')
        #Check for while loop
        if self.is_while_statement(line):
            line_type.append('while')
        #Check for while loop break
        if self.is_whilebreak_statement(line):
            line_type.append('whilebreak')
        #Check for if-then
        if self.is_ifthen_statement(line):
            line_type.append('ifthen')
        #Check assignment
        if self.is_assignment_statement(line):
            line_type.append('assignment')
        #Check stout
        if self.is_stdout_statement(line):
            line_type.append('stdout')
        if len(line_type) > 1:
            return f"invalid type cannot be both {line_type}"
        if len(line_type) == 0:
            return "no type"
        else:
            return line_type[0]

    #matching helper functions - check and return boolean
    #Check comment statement
    def is_comment_statement(self,line):
        if "backstory" in line:
            return True
        if "history" in line:
            return True
        return False

    #Check comparison statement
    def is_comparison_statement(self,line):
        for pronoun in self.pronouns:
            match_statement = f'{pronoun} argued'
            if match_statement == line[:len(match_statement)]:
                if "with" in line:
                    return True
        return False

    #Check operator statement
    def is_operator_statement(self,line):
        if 'so then' == line[:7]:
            return True
        return False

    #Check for while loop start
    def is_while_statement(self,line):
        for pronoun in self.pronouns:
            match_statement = f'{pronoun} calmly explained '
            if match_statement == line[:len(match_statement)]:
                return True
        return False

    #Check for while loop end
    def is_whilebreak_statement(self,line):
        break_statements = ['refused to discuss','stormed off','refused to talk']
        for statement in break_statements:
            if statement in line:
                return True
        return False
        
    #Check for if-then
    def is_ifthen_statement(self,line):
        for pronoun in self.pronouns:
            match_statements = [
                f'{pronoun} believed ',
                f'{pronoun} thought ',
                f'{pronoun} said I thought ',
                f'{pronoun} said they thought ',
                f'{pronoun} said everybody thought ',
                ]
            for match_statement in match_statements:
                if match_statement == line[:len(match_statement)]:
                    return True
        return False
    #Check variable assignment
    def is_assignment_statement(self,line):
        if line[:2] == "so" or line[:2] == "my" or line[:3] == "our" or line[:3] == "the":
            if 'clarity' in line or 'simplicity' in line or 'for ease' in line:
                for pronoun in self.second_person_pronouns:
                    if f'lets call {pronoun}' in line:
                        return True
        return False
        #standard or boolean todo
    #Check stdout statement
    def is_stdout_statement(self,line):
        for pronoun in self.pronouns:
            match_statements = [
                f'{pronoun} told',
                f'{pronoun} declared',
                f'{pronoun} proclaimed',
                f'{pronoun} yelled',
                f'{pronoun} screamed',
                f'{pronoun} sobbed',
            ]
            for match_statement in match_statements:
                if match_statement == line[:len(match_statement)]:
                    return True
        return False



