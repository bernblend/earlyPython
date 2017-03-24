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
