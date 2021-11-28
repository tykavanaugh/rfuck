class Helper:
    def __init__(self):
        self.variable_table = {'reddit':'yta'}
        self.pronouns = ['i','he','she','we','they','someone','something','it','ze']
        self.second_person_pronouns = ['them','you','her','him','zem','those','it']

    def assign_variable(self,var_name,value=0):
        var_name = var_name.lower()
        self.variable_table[var_name] = value
    
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
        return False

    #Check comparison statement
    def is_comparison_statement(self,line):
        for pronoun in self.pronouns:
            match_statement = f'{pronoun} argued'
            if match_statement == line[:len(match_statement)]:
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
            ]
            for match_statement in match_statements:
                if match_statement == line[:len(match_statement)]:
                    return True
        return False



