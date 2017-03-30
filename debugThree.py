# Try adding print statements to look at the values of variables inside
# the remove function.  See if you can find out what's making it give
# silly answers such as remove('ding', 'do') -> 'dining'.

def remove(somestring, sub):
    """Return somestring with sub removed."""
    location = somestring.find(sub)
    if location == -1:     # this means it was not found.
        return somestring     # this line was missing, we were returning -1.

    print "# DEBUG:"
    print "# location", location
    length = len(sub)
    print "# length", length
    part_before = somestring[:location]
    part_after = somestring[location: + length:]

    print "# before and after", part_before, part_after
    return part_before + part_after


#
# Don't change these test cases!
print remove('audacity', 'a')
print remove('pythonic', 'ic')
print remove('substring institution', 'string in')
print remove('ding', 'do')  # "do" isn't in "ding"; should print "ding"
print remove('doomy', 'dooming')  # and this should print "doomy"
