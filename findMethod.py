pythagoras = 'There is geometry in the humming of the strings, there is music in the spacing of the spheres.'

print pythagoras.find('string') #string starts at index 40
print pythagoras[40:]
print pythagoras.find('T')
print pythagoras.find('sphere')
print pythagoras[86:]
print pythagoras.find('algebra')


s = 'any string'

print s.find(s)   # always 0, finds itself

print s.find('s')    # only 0 is string starts with s

print 's'.find('s')   # always 0, finds itself

print s.find('')    # always 0, space is thher

print s.find(s + '!!!') + 1   # always 0, because 1st part is always -1, "!!!" is not found in the string


# This segment is just a chance for you to play around with
# finding strings within strings. Read through the code and
# press Test Run to see what it does. Is there anything
# interesting or unexpected?

print "Example 1: Finding substrings in a string"
print "test".find("te")
print "test".find("st")
print "test"[2:]

print "Example 2: Finding substrings in a string which is stored as a variable"
my_string = "test"
print my_string.find("te")
print my_string.find("st")
print my_string[2:]

print "Example 3: Printing out everything after a certain substring"
my_string = "My favorite color: blue"
color_start_location = my_string.find("color:")
print color_start_location
favorite_color = my_string[color_start_location:]
print favorite_color # oops, this line prints out 'color: ' as well...
print favorite_color[7:] # this fixes it! favorite_color has new index


print "Example 4: Other interesting things about string.find()..."
print "text".find("text") # prints 0
print "text".find("Text") # prints -1
print "text".find("")     # prints 0
print "text".find(" ")    # prints -1


print '********** MORE of .find() ***************'

print "text".find("t", 1)  # starts from index 1 to find letter



print '********** more on 2nd parameter ***************'

danton = "De l'audace, encore de l'audace, toujours de l'audace"
print danton.find('audace')
print danton.find('audace', 0)   # same, as it starts at index 0
print danton.find('audace', 5)  # still finds first audace at index 5
print danton.find('audace', 6)  # now goes to next audace in string
