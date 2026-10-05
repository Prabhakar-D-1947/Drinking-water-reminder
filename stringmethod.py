# --------------String slicing ------------

names = "Prabhakar,Aarsha,Aditya,Nishant,Arshal,"
#print from starting index (0) but not (9) instead upto index (8) 
print(names[0:9])

print(len(names))
print(names[10:16])
#python automatic start indexing from (0)
print(names[:9])
# negative index means len(str)-(index)
print(names[0:-1])
print(names[0:len(names)-1])
print(names[17:len(names)])

# ---------- String Method -------------------
# Strings are immutable 

a = "Prabhakar!!!!!!!!!!"
# change the case of the string
print(a.upper())
print(a.lower())

# remove the instructed string 
print(a.rstrip("!"))

# replace the string with new string 
print(a.replace("Prabhakar","Aarsha"))

# split the string with instructed delimiter
b = "Prabhakar Aarsha Aditya Arshal"
print(b.split(" "))

# if the first letter of the whole string is in lower case convert into upper case
# and also change the any upper case letter into lower case if is in between the string
blogHeading ="introduction to PyTHon"
print(blogHeading.capitalize())

# add the space from left margin as total length of string become as instructed 
str1 ="Welcome to the Console!!!"
print(str1.center(50))
print(len(str1))
print(len(str1.center(50)))

# count the number of occurance of the string 
print(str1.count("o"))

# check the string whether string ends with particular string or not  and the return boolean answer 
# there is similar method for checking string from the starting startswith()method .
print(str1.endswith("!!!"))
# print(a.endswith("!!!"))

print(str1.endswith("to",4,10))

# return the index of  first occurance of given string 
str2 = "He's name is Dan. He is an honest man."
print(str2.find("is"))

# raise a exception if it is not found the string otherwise it is very similar with find()
# print(str2.find("ishh"))
# print(str2.index("ishh"))
 
c = "hello123"
#return true if string contains only A-Z a-z and 0-9 no special character not even space
print(c.isalnum())
# return true if string contains only A-z and a-z  no special character not even space 
print(c.isalpha())
# check wether given string character is lower case or not 
# similarly there is method for upper case name isupper()
print(c.islower())
print(c.isupper())

# return false because \n is not a printable character like if we print oue=r string \n will not print 
str1 = "We wish you a merry christmas \n" 
print(str1.isprintable())

# isspace()  method return true only and only if the string contains white spaces ,else return false

str1 ="     " #using spacebar
print(str1.isspace())
str2="          " #using tab bar 
print(str2.isspace())

# return true only if the first lettr of the each word of the string is capitalized,else return false.
str1 ="World Health Organisatiion"
print(str1.istitle())
# change the the case of the sting 
print(str1.swapcase())

# title() method ..title the string if it is not 
text ="my name is prabhakar dwivedi"
print(text.title())
 