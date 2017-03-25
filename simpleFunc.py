# Once again, say_hello is a function (AKA procedure). But this time, it DOESN'T
# do the same thing every time.
#
# Read through the code and try to predict what the output will be when
# you press "Test Run"

def say_hello(name):
    greeting = "Hello " + name + "!"
    return greeting

print say_hello("Miriam")
print say_hello("Andy")



def say_hello(name):
    greeting = "Hello " + name + '!'
    return greeting
# In the previous example, you saw code that looked like what you see above.
# Look at the first line. In that line, 'name' is a "parameter"
# of the function say_hello

# In the code below, the add_two_numbers function has two parameters.
# What do you think will happen when you press "Test Run"?
# Make a prediction and then press "Test Run"
def add_two_numbers(number_1, number_2):
    return number_1 + number_2

print add_two_numbers(4, 3)
print add_two_numbers(2, 6)
print add_two_numbers(0, 9)

# Once you've pressed Test Run, remove the comment characters from the
# code below and then make ONE modification so that the function does
# what the name says it should do.

#def subtract_two_numbers(number_1, number_2):
#    return number_1 + number_2

#print subtract_two_numbers(4, 3)



# *******************************************************************
# *******************************************************************


# Below are some examples:

#This example shows that the function sum returns no value.
#OUTPUT: None (no value)
def sum(a, b):
    a = a + b

print sum(1, 1)

#Here we add print statements to debug the code.
def sum(a, b):
    print "enter sum!"
    print "a is", a
    a = a + b
    print "a is", a

print sum(1, 1)


#Here we fix the code with a 'return'.
def sum(a, b):
    a = a + b
    return a

print sum(1, 1)



# *******************************************************************
#    VIDEO EXAMPLES WITH COACH:

def some_func():
    print "Hello World!"

some_func()
some_func()




print "***********     AVOID GLOBAL VARIABLES   **********************"
# ******************************************************************
#     Global vs Local Variable

a = 6           #without this 'a', bottom function causes error.

def some_function():
    a = 5
    print "Function: " + str(a)

some_function()
print "Global: " + str(a)       #this 'a' would not run as prior 'a' is
                                #indented and therefore local NOT global.

# *******************************************************************


def some_func(var1, var2):
    print var1
    print var2

some_func("bern", 2)


# SIMILAR

def some_func(var1, var2):
    print var1
    print var2

a = "bern"
b = 2
some_func(a, b)




print "*************************************************************"
print "Immutable Objects: string, int, float (not containers)"
print "*************************************************************"
print "Mutable Objects: Lists, Dictionaries"
print "*************************************************************"



# IMMUTABLE OBJECT

# A variable points to a value that it holds on python.
# int is a type of immutable value

a = 5      # b is a variable that points to the value 5.

print "The address the variable is pointing to is: "
print id(a)


a = 6     # b is now point ing to a new value.

print "The address the variable is pointing to is: "
print id(a)

a = 5

print "The address the variable is pointing to is: "
print id(a)

#NOTE: Above, when '5' was changed to '6', the id changed!
# '5' & '6' are constants, they don't change.
# That means the pointer that 'a' refers to has to change!





print "MUTABLE OBJECT (example: a list):"

a = [1]
print id(a)

a.append(2)
a
print id(a)

#NOTE: The list is still the same list, it's just mutated.

# When we made it a 'list', the ID did NOT change because the 'list'
# itself changed instead of the pointer.






print "********************************************"
print "****  MUTABLE AND IMMUTABLE OBJECTS   **********"
print "********************************************"
print "********************************************"

print "If we pass in a MUTABLE variable to a function:"


def some_func(some_list):
    some_list.append(1)
    print "Local: " + str(some_list)

a = [1,2,3]
some_func(a)
print "Global: " + str(a)

print "The value that comes in the function is changed oustide"
print "of the function, they are the same (think Global)."
print "The local variable in the function is NOT destroyed at the end"
print "of the function."



print "********************************************"
print "********************************************"

print "If we pass in a IMMUTABLE variable to a function:"


def some_func(some_list):
    some_list += 1
    print "Local: " + str(some_list)

a = 5
some_func(a)
print "Global: " + str(a)

print "The value that comes in the function is changed oustide"
print "of the function, they are different (think local)."
print "The local variable in the function is destroyed at the end"
print "of the function."




print "************************************************************"
print "****  GETTING THE VALUE OF AN IMMUTABLE WITH 'return'.  *****"
print "************************************************************"
print "************************************************************"


def some_func(some_value):
    some_value += 1
    print "Local: " + str(some_value)
    return some_value, 1, 2

a = 5
x = some_func(a)
print "Global: " + str(x)





print "************************************************************"
print "****  'Hi' will never be printed, return closes function.   *****"
print "************************************************************"
print "************************************************************"


def some_func(some_value):
    some_value += 1
    print "Local: " + str(some_value)
    return some_value, 1, 2
    print "HI"

a = 5
x = some_func(a)
print "Global: " + str(x)




print "\n\n"
print "****  Using 'return' to print out directly.   *****"
print "\n"



def some_func(some_value):
    some_value += 1
    return some_value, 1, 2


a = 5
print some_func(a)







print "\n\n"
print "****  Possible ways to return 'none'.   *****"
print "\n"


def some_func(some_value):
    some_value += 1
    return


a = 5
print some_func(a)




def some_func(some_value):
    some_value += 1

a = 5
print some_func(a)



print "\n\n"
print "************************************************************"
print " ASIDE: When a function does anything besides input/output"
print "and alters some mutable values, we call that alteration"
print "a side effect of the function   (a side effect may be the"
print "whole point someday)"





print "\n\n\n\n\n"
print " IF STATEMENTS:"
print "\n"
print "In python we don't have to specify a type for our parameter."
print "Here we can return things depending on wether we have an 'int': "
print "\n"


def some_func(some_value):
    if type(some_value) == type(1):
        return 1
    else:
        return "Not an int"

print some_func(25)
print some_func(25.0)    #NOTE: This one is a 'float', NOT an 'int'.




print "\n\n"
print "The 'return' will end a function even in the middle of a loop,"
print "so you have to put the 'return' outside the for loop:"
print "\n"


def some_func(some_value):
    some_list = []
    for e in range(10):
        some_list.append(some_value)
    return some_list

print some_func(25)
print some_func(25.0)







print "\n\n"
print " Recursion: "
print " 'if' statement has a base case, which is the stopping condition."
print "python NOT good for recursion, because it takes too much memory"
print "in python"
print "\n"


def some_func(some_value, count):
    print some_value
    if count == 0:      # base case
        return some_value
    else:
        return some_func(some_value + 1, count - 1)

            # NOTE: Above, count + 1 above, would never end

print some_func(25, 10)


print "\n\n"
print " Aside: "
print " Where recursion can be used, so can loops. However, recursion"
print "may be EASIER to set-up. Loops tend to be faster."
print "Recursion is most useful when you are not sure how many"
print "calculations you may end up processing."
print "\n\n\n\n"



print "CONCLUSION: Functions and procedures are interchangable terms."
print "main point GLOBAL & LOCAL scopes."
