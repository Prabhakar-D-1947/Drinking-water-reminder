# tuples do not change 
tup = (34,76,87,"prabhakar",True)
print(tup)
if "prabhakar" in tup: 
    print("yes it is present")
tup2 = tup[0:4]
print(tup2)
print(len(tup))

#------------ method of tuples----------

countries = ("spain","India","Italy","England","Germany")
temp = list(countries)
temp.append("Russia")
temp.pop(2)
temp[3] = "Finland"
countries = tuple(temp)
print(countries)

# we can concatenate tuples directly by adding them
temp2 = ("france","polland")
Nation = countries + temp2
print(Nation)

# count() method is use to count the number of occrance of element
tup3= (0,9,7,9,8,3,0,9,9,8,9,9,)
print(tup3.count(9))

# index() method return the index of first occurance of given element also we can use in particular portion of tuples
print(tup3.index(9))
print(tup3.index(9,2,7))
print(len(tup3))
