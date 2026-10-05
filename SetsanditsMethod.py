# Sets are unchangeable meaning you can not change items othe 
# the set once you created,set do not contain duplicate items.

s = {2,4,6,2}
print(s)

info = {"Carla",19,False,2.5,19}
print(info)
#Empty set
name = set()
print(type(name))


for value in info:
    print(value)
# -----------------just for practice-------------------
# i =0
# while(i<5):
#  j=0
#  while(j<=i):
#   print("*",end=" ")
#   j = j+1
#  print()
#  i = i+1


#------------------ MethodS of Sets -------------------------
s1 ={1,2,5,6}
s2 ={3,6,7}
# it does not change the s1
print(s1.union(s2))
# it changes the s1 add all the element of s2 in s1
s1.update(s2)
print(s1,s2)


cities ={"Tokyo","Madrid","Berlin","Delhi"}
cities2 ={"Tokyo","Seoul","Kabul","Madrid"}
cities3 = cities.intersection(cities2)
print(cities3)

# it updates the the set cities
cities.intersection_update(cities2)
print(cities)

#symetric difference or union of (A-B)U(B-A)
cities3 = cities.symmetric_difference(cities2)
print(cities3)

#difference method is (A-b)......Similarly there is method name difference_update()
cities3 =cities.difference(cities2)
print(cities3)

#check sets have some common element or not
print(cities.isdisjoint(cities2))


#check sets is superset of a set.......Similarly there is issubset()method 
print(cities3.issuperset(cities2))

# add() method add a single item in the set
cities.add("Singapore")
print(cities)

# remove() method and discard() method both use to delete any item from set 
# but remove raise a error ... discard() not raise any error 

cities.discard("Singapore") 
print(cities)

# cities.remove("Singapore")
# print(cities)

# pop() method delete last item of the set.... means a random item will pop as set always in random order
item = cities.pop()
print(cities)

# del is a keyword that use to delete a entire set
del cities

# if you don't want to delete the set but you want delete all the item of the set then 
# use clear() method

cities2.clear()
print(cities2)