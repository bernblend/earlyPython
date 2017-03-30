# A small change will fix the crashing bug in printInches.

def printExample(a, b):
    print a + b

def printInches(n):
    print str(n) + " inches"

    # BUG: The bug was above because we didn't have str() with 'n' as
    # a parameter to concatenate the 'int' and 'string.'
    # str() converts 'int' into a 'string'.

# Don't change the function calls on lines 10 - 12.
printExample(17, 23)
printExample('long', 'word')
printInches(42)
