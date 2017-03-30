# Define a procedure, biggest, that takes three
# numbers as inputs and returns the largest of
# those three numbers.


# USING max()

print max(56, 33, 78)



def biggest(a, b, c):
    if a > b:
        biggestNum = a
    else:
        biggestNum = b
    if c > biggestNum:
        biggestNum = c
    return biggestNum



print biggest(3, 6, 9)
#>>> 9

print biggest(6, 9, 3)
#>>> 9

print biggest(9, 3, 6)
#>>> 9

print biggest(3, 3, 9)
#>>> 9

print biggest(9, 3, 9)
#>>> 9
