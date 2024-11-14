# dict.. hosse key,value pair value store. like:dart er map

a = {
    'name': "yasir",
    'age':24,
    'gender':"male",
     "smoking":False,
     'marks':[20,82,36],
     8:"hello"
}

print(a.items()) # each pairs
print(a.keys()) # keys
print(a.values()) # values

a.update({'name':'yasir arafat'}) # update
print(a)

print(a.get('age'))
print(a['age'])

#diff between both
# if given key is not list then it print None. ex: a.get('age3') 
# if given key is not list then it print error. ex: a['age3'] 