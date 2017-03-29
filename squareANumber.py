# Define a procedure, square, that takes one number
# as its input, and returns the square of that
# number (result of multiplying
# the number by itself).
# To help you out, the code for sum(a,b) is below.

def sum(a,b):
    c = a + b
    return c


# To test your procedure, uncomment the print
# statement below, by removing the hash mark (#)
# at the beginning of the line.

# Do not remove the # from in front of the line
# with the arrows (>>>). Lines which begin like
# this (#>>>) are included to show the results
# you should see when run your procedure


def square(num):
    return num * num

print square(9)


# The code below is an example of procedure composition.
# Use the output from one procedure (function) as the
# input for a different procedure (function).

def square(num):
    return num * num

x = 37
print square(square(x))