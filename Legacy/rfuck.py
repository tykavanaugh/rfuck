#legacy skelton idea
#not for release
import sys

def main():
    file = sys.argv[1]
    memory = {0:0}
    index = 0

def movePointerRight(index,memory):
    try:
        memory[index+1]
    except KeyError:
        memory[index+1] = 0
        return index+1

def movePointerLeft(index,memory):
    try:
        memory[index-1]
    except KeyError:
        memory[index-1] = 0
        return index-1

def increment(index,memory):
    memory[index] += 1
    return index

def decrement(index,memory):
    memory[index] -= 1
    return index

def rstdout(index,memory):
    print(chr(memory[index]),end="")
    return index

def rstdin(index,memory):
    input_var = input()
    if type(input_var)==type(" "):
        memory[index] = ord(input_var)
    if type(input_var) == int:
        memory[index] = input_var
    return index

def start_loop(index,memory):
    pass
def end_loop(index,memory):
    pass

    

def parse(text,index,memory):
    code = []
    for count,char in enumerate(text):
        if char == ">":
            code.append(movePointerRight(index,memory))
        if char == "<":
            code.append(movePointerLeft(index,memory))
        if char == "+":
            code.append(increment(index,memory))
        if char == "-":
            code.append(decrement(index,memory))
        if char == ".":
            code.append(rstdout(index,memory))
        if char == ",":
            code.append(rstdin(index,memory))
        if char == "[":
            pass
        if char == "]":
            pass