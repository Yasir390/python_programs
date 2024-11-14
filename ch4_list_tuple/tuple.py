#tuple is list but immutable(not changeable)

a =(1,45.5,45.5,'jkdc',True)
print(a)
b = a.count(45.5) # how many items find
print(b)

c = a.index('jkdc') # index find
print(c)