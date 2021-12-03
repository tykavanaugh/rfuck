# rfuck

Parses code that looks like the average reddit relationships question and transpiles into python and then executes the script

Simply run 
```
python make.py filename.redditlang
```

There will likely be issues if you try this on a non-unix system because of carriage returns. 

~~All documentation right now is just comments in the source code fuck you~~

Some documentation added

## Implemented

Variable assignment to int or bool

While loops

Comparison operators

Stdout 

Basic operators (add, subtract, modulo, divide, multiply, etc) - Done!

*Some* documentation!

If statements!

## Todo/Partial


For loops

Compile to golang/c binary instead of python

Handle assignment with integers that have zeros in base 10 better

# Fizzbuzz.redditlang
```
History about my family- we count down from 50 to 0
Backstory about us, we print fizz if the integer is divisible by 3
Our family history is that we print buzz if divisible by 5
And our last bit of history is that we print fizzbuzz if divisible by 3 AND 5
My program, for ease lets call it fizzbuzzloop, is quite empty
My f, for clarity lets call it letterF, is mostlly empty
Our i, for clarity lets call it letterI, is almostt two
So z, for simplicity lets call it letterZ, is qwertyuio empty
The b, for ease lets call it letterB, is grosly grosss
My u, for clarity lets call it letterU, is blahblah words
Our zero, for clarity lets call it zero, is empty
Our three, for clarity lets call it three, is qwe
Our five, for clarity lets call it five, is qwert
My one, for ease lets call it one, is a
My space, for simplicity lets call it newline, is qwe ty

I calmly explained to fizzbuzzloop that stuff
So then fizzbuzzloop left three and went to modulo3
So then fizzbuzzloop left five and went to modulo5
I argued that modulo3 was the same as zero with modulo3
I argued that modulo5 was the same as zero with modulo5
I thought that modulo3 was something
I thought that modulo5 was something else
I declared that letterf was a letter
I told that letteri was a letter
I declared that letterz was a letter
I yelled that letterz was a letter
I screamed that letterb was a letter
We declared that letteru was a letter
I declared that letterz was a letter
I declared that letterz was a letter
I stormed off and whatever
I declared that letterf was something
I declared that letteri was something
I declared that letterz was something
I declared that letterz was something
We refused to discuss further
I thought that modulo5 was something else
I screamed that letterb was a letter
We declared that letteru was a letter
I declared that letterz was a letter
I declared that letterz was a letter
We refused to discuss further
I declared that newline was a new line
So then fizzbuzzloop took one and called itself fizzbuzzloop
```





## "Documentation"

### General Syntax

I will use python fstring notation for strings with variables

The basic structure is the `sentence`. Each "line" indicated by a carriage return or a period is considered a `sentence`, like ";" in C or a carriage return in python. Unlike good or useful languages, a `sentence` must either be a specific type of statement or it's considered a comment. If it can be typed ambigously the program will not compile and you will get an error telling you which lines were ambigious. Because of the difficulty of knowing exactly what type of statement you are making, the compiler script will by default tell you what it thinks each line is.

Mispellings and bizarre syntax/formatting/variable names is strongly encouraged! Remember to channel someone who thinks asking reddit for advice on their intimate parter issues is a good idea.

Case is irrelvant. 

First and second person pronouns are also part of certain statements

I understand I am using "first and second person" incorrectly I don't care

First person: 'i','he','she','we','they','someone','something','it','ze'

Second person: 'them','you','her','him','zem','those','it','our'

### Implemented Features

#### Comments

Any sentence with "backstory" or "history" will evaluate to a comment without an error, regardless of everything else.

Any sentence that doesn't match any other kind will still become a comment (though the compiler will call it a "no type" for clarity)

#### Variable Assignment

Variable assignment can be to an integer or a bool.

Assignment sentences must start with "my" "so" "our" or "the", then contain the word "clarity" "for ease" or "simplicity," then contain f"lets call {first person pronoun}" followed by a space and the name of the variable you wish to create. If you stop here the value of the variable will be 0

```My car, for ease lets call it my_car```

my_car = 0

To declare and assign a value, follow the variable name with a comma, and then either the word "is" for a positive, "is not" for a negative, or "is nothing" for explict 0. The length of the words correspond to the value of length of the word times 10 ^ position of the word from the right. "A real clunker" evaluates to 147. 

```My car, for ease lets call it my_car, is a real clunker```

my_car = 147

In progress of figuring out how I will assign 0 values, probably with a keyword. 

"empty" should evaluate to 1 * 10 ^ position of the word but this is currently untested.

#### While loop

f"{first person pronoun} calmly explained to " declares while and the word following must be an already declared variable that is the condition of the loop. As it's evaluated by a python interpreter in this version, python truthy or falsy values will work for the loop condition


For example:

```We calmly explained to my_car```

All text after that in the statement is just comments.

To end the while loop a statement with 'refused to discuss','stormed off','refused to talk' will exit the current loop

#### If

```
f'{first person pronoun} believed that ',
f'{first person pronoun} thought that',
```

```
I thought that bob was stupid
```
Evaluates to 
```
if bob:
  {next sentence}
```
You can break out the if loop just like the while loop- 'refused to discuss','stormed off','refused to talk'

#### Logic


f"{first person pronoun} argued that" followed by a variable, followed by an operator, followed by another variable, followed by "with" followed by the new assigned variable.

logic operators
```
'was better than' >
'was worse than' <
'was the same as' == 
'was nothing like' !=
'was better or the same as' >=
'was worse or the same as' <=
```

Assuming cats = 1 and dogs = -1

```
We argued that cats was better than dogs with dad.
```
dad = True

#### Primitive Operators

```
                'gave ' +
                'took ' -
                'left ' %
                'split ' // 
                'repeated ' *
```
You start with "so then" followed by a variable, followed by an operator word, followed by the second variable, followed by the variable to be assigned.

Ie 

```
So then alex gave bob and called it green
```
Evaluates to:
```
green = alex + bob
```

#### Stdout

```
f'{pronoun} told',
f'{pronoun} declared',
f'{pronoun} proclaimed',
f'{pronoun} yelled',
f'{pronoun} screamed',

```
followed by a "that " then a variable to output as ascii

```
i proclaimed that t was a bad president
```
Will output the value of t
