#import pandas
#import tensorflow
import hashlib
# print("hello world")
# print("hey",120,8, sep="~", end="\n")
# print("Prabhakar")
# print(15+6)
# print(15-6)
# print(15*6)
# print(15/6)
# print(15//6)
# print(15%6)
# print(5**3)

# str ="hello"
# name = """hey my name is : Prabhakar 
#     here i am practicing python or 
#     you can say that i am learning python."""
# print(name)

# for char in str:
#  print(char)

# for alph in name:
#  print(alph)

x= int(input("Enter a number: "))

match x:
 case 0:
  print("hello this is me ")

 case 5:
  print("hey ... i am here only")

 case _:
  print("default case")
  
#----------------- Recursion ---------------
def fibonacci(n):
    if(n==0):
     return 0
    if(n==1):
       return 1
    else:
       return (fibonacci(n-1)+fibonacci(n-2))
    

print(fibonacci(8))


# we can use Else block with for loop , while loop, if etc.