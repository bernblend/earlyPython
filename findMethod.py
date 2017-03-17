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
print danton.find('audace', 0)  # now goes to next audace in string
print danton[6:]
print danton.find('audace', 25)
print danton.find('audace', 26)
print danton[47:]
print danton.find('audace', 48)



# This segment is just a chance for you to play around with
# finding strings within strings. Read through the code and
# press Test Run to see what it does. Is there anything
# interesting or unexpected?

print "Example 1: using find to print the second occurrence of a sub-string"
print "test".find("t")
print "test".find("t", 1)

print "Example 2: using a variable to store first location"
first_location = "test".find("t") # here we store the first location of "t"
print "test".find("t", first_location+1) # then we use that location to find the second occurrence.

print "Example 3: using find to get rid of exclamation marks!!"
example = "Wow! Python is great! Don't you think?"
first = example.find('!')
second = example.find('!', first + 1)
new_string = example[:first] + example[first+1:second] + example[second+1:]
print new_string # oops, I should probably replace the !s with periods
new_string = example[:first] +'.'+ example[first+1:second] +'.'+ example[second+1:]
print new_string




print "***************************"
print "***************************"

# Assume text is a variable that
# holds a string. Write Python code
# that prints out the position
# of the second occurrence of 'zip'
# in text, or -1 if it does not occur
# at least twice.

# The Python code should be general enough
# to pass every possible case where 'zip'
# can occur in a string

# Here are two example test cases:
#text = 'all zip files are zipped'
# >>> 18
# text = 'all zip files are compressed'
# >>> -1

text = "all zip files are zipped"

# ENTER CODE BELOW HERE
first_zip = text.find('zip')
print text.find('zip', first_zip + 1)
# Other way
print text.find('zip',text.find('zip')+ 1)

# IMPORTANT BEFORE SUBMITTING:
# You should only have one print command in your function




print "***************************"
print "***************************"
