name = 'Hector'
print 'Hello ' + name + '!' * 3

print name[-1]


s = "some string"

print s[3],s[1+1+1]

print s[0],(s+s)[0]

print s[0] + s[1],s[0 + 1]

print s[1],(s + 'ity')[1]  #trick question - NOT same value all the time.

print s[-1],(s + s)[-1]


name = 'Hector'
print name[0:3]


word = 'assume'

print word[3]
print word[3:5]  #print index 3 and 4 only
print word[:2]
print word[2:]
print word[:]



s = 'audacity'

print 'U' + s[2:]




s = 'any string'

print s[:]

print s + s[0:-1+1]

print s[0:]

print s[:-1]

print s[:3] + s[3:]
