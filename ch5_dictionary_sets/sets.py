
# sets , doesn't print duplicate value (repetition not allowed)
a = {1,45,34,5,7,3,6,7,8,7,7,"hello"}
print(a)

# this is empty set, interview question
b = set()
print(type(b))
print(len(a)) # length 

a.remove(7)
print(a)


b = {} # now this is dictionary . 
c = set() # this is set
d = {1,45,34,5,7,3,6,7,8,7,7,"hello"} # this is set.
# when set is empty and { }, then it represent as dictionary. so , empty set will be, k= set()