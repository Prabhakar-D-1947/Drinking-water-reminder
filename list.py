# list do all the operation on the same list 
l = [1,3,24,5,8,24]
print(l)
#add the at last
l.append(90)
# ascending order sorting
l.sort()
print(l)
# decreasing order sortging
l.sort(reverse=True)
print(l)
# reverse() method reverse the list
l.reverse()
print(l)
# return the index of the given value at first occrance
print(l.index(24))
# count the number of occurance of the element
print(l.count(24))
# if you want to copy of the list then use copy method 
m = l.copy()
m[0]=199
print(m)
# use for insert a new value at particular index 
m.insert(1,200)
print(m)
# extend() method use to add or extend or concatenate a list 
n = [800,324,111]
m.extend(n)
print(m)
k = m+n
print(k)

