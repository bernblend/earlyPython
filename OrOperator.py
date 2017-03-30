



def is_friend(name):
    return name[0] == 'D' or name[0] == 'N'



print is_friend('Doug')
#>>> True

print is_friend('Nicole')
#>>> True

print is_friend('Fred')
#>>> False






print True or False
print False or True
print True or True
print False or False

print "print True or this_is_an_error: "

print True or this_is_an_error   # No need to evaluate the 2nd expression.


#   print False or this_is_an_error         This will give error because 2nd
                                          # expression is NOT defined.
    #NOTE: If first expression is 'false' then the value of the 'or'
    # construct is the value of the 2nd expression.
