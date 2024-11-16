s = set()
s.add(20)
s.add(20.0)
s.add("20")

print(len(s))
print(s)

# why length is 2? 
#ans: bcz, 20 and 20.0 are the same so, length of these is 1. set count them as 1
#and "20" is another one 