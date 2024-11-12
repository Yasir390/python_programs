name = "yasir"
nameShort = name[3] #specific index
nameLen = len(name) # string length calculate
nameRange = name[0:3] # start from 0 index and less than index 3 . So, index 0-2 will print
nameRangeNegativeSlice = name[-5:-2]  # last index -1
firstPosEmpty = name[:3]  # it means start from 0 to <3 index
lastPosEmpty = name[1:]  # it means start from 1 to  last index
a ='123456789'
skipValue = a[1:8:2] # 1 index to <8 index. and value gap will be 2

print(nameShort)
print(nameLen)
print(nameRange)
print(nameRangeNegativeSlice)
print(firstPosEmpty)
print(lastPosEmpty)
print(skipValue)