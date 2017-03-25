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
print "Imutable Objects: string, int, float (not containers)"
print "*************************************************************"
print "Mutable Objects: Lists, Dictionaries"
print "*************************************************************"



# IMUTABLE OBJECT

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
print "********************************************"
