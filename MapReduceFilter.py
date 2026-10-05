#-----------------------Map--------------------------
# def cube(x):
#     return x*x*x

# -------------------lambda function ---------------------
# cube = lambda x: x*x*x

# l = [1,2,3,4,5,6,4,3]
# newl = []
# for item in l:
#     newl.append(cube(item))
# print(newl)


# newl = list(map(cube,l))
# print(newl)

#---------------Filter--------------------------


# def filter_function(a):
#     return a>4

#OR------
# filter_function = lambda a:a>4

# newnewl = list(filter(filter_function,l))
# print(newnewl)


from functools import reduce

numbers = [1,2,3,4,5]

sum = reduce(lambda x,y: x+y,numbers)

print(sum)

# ---------------------is opertor vs == operator------------------
# is compares the exact location or identity of the variable and == compares the value of variable 

a = [1,2,43]
b= [1,2,43]

print(a is b)
print(a==b)