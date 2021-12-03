# rfuck

Parses code that looks like the average reddit relationships question and transpiles into python and then executes the script

Simply run 
```
python main.py filename.redditlang
```

There will likely be issues if you try this on a non-unix system because of carriage returns. 

~~All documentation right now is just comments in the source code fuck you~~

Some documentation added

## Implemented

Variable assignment to int or bool

While loops

Comparison operators

Stdout 

## Todo/Partial

Basic operators (add, subtract, modulo, divide, multiply, etc)

For loops

Compile to golang/c binary instead of python

Handle assignment with integers that have zeros in base 10 better

Explain or document how r/relationshitsLang works like at all. probably not

# Hello.redditlang

This overly complicated program prints "HELLO" using a while loop that iterates one time may god have mercy on me for making this


```
Backstory: my family has lots of political drama
so dad, for clarity lets call him d, is generly it
more backstory by that I mean the source the drama
so trump, for ease lets call him t, is kindaa important
the thing, who for simplicity lets call it l, is superly online
kinda guy, you know just for more backstory
my family, for clarity lets call f, is a f a
mily that likes to argue about politics and history stuff
our cat, for clarity lets call it dad, is a cuddly guy

I calmly explained to dad I was poly

he yelled that d would never have a vegan son
i proclaimed that t was a bad president
i told him that l my bro is also poly
he told us that l was a bad son as well
and for more backstory my mom was around
my mom, for ease lets call her m, is against aborition
she declared to us that m jepordized the beans
for some more backstory, m is my mom and she buried the beans 

my room, for clarity lets call it room, is too sm
all for me I think, just adding more backstory
our house, for clarity lets call it house, is a b i
t too big if you ask me while we continue to add relevant history

our family, for simplicity lets call it fam, is a not no
bit of a mess

our dad, for clarity lets call him dad

has some anger issues, just to add more backstory

dad refused to discuss and stormed off before we could talk about them giving me their house

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

f"{first person pronoun} calmly explained to " declares while and the word following must be an already declared variable that is the condition of the loop. As it's python, python truthy or falsy values will work for the loop

You cannot nest while loops in this version.

For example:

```We calmly explained to my_car```

All text after that in the statement is just comments.

To end the while loop a statement with 'refused to discuss','stormed off','refused to talk' will exit the loop and return to the main scope

#### Logic


f"{first person pronoun} argued that" followed by a variable, followed by an operator, followed by another variable, followed by "with" followed by the new assigned variable.

Operators
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

#### Operators

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

