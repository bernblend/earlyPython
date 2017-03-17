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
