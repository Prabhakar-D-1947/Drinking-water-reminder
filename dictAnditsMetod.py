# Dictionaries are ordered (after python 3.7 onwards) collection of data items.

dic={
    344:"Prabhakar",
    56:"Shubham",
    678:"Zakir",
    567:"Neha"
}
print(dic[567])

info = {'name':'Karan','age':19,'eligble':True}
print(info)
# Raise a error if key not found
print(info['name'])
# return none if key is not found 
print(info.get('name'))
# access  all the keys 
print(info.keys())

#Access  all the value of keys
print(info.values())


# for i in info.keys():
#     print(f"The value corresponding to the key {i} is {info[i]}")


print(info.items())
for key, value in info.items():
    print(f"The value corresponding to the key {key} is {value}")


#--------------------------Methods of dictonary---------------------------

ep1 ={122:45, 123:89, 567:69,
      670:69}

ep2 ={222:67, 566:90}
# update() method udate the dict(ep1) with dict(ep2)
ep1.update(ep2)
print(ep1)

# clear() method use for clear all the item from the dict and update with empty dict
ep2.clear()
print(ep2) 
# pop() method remove the given key value
ep1.pop(122)
print(ep1)

# popitem() methos remove last item from the dict
ep1.popitem()
print(ep1)

# del is a keyword which delete the dictonary or we can use it to delete particular entry from
# the dict
del ep2
del ep1[123]
print(ep1)
