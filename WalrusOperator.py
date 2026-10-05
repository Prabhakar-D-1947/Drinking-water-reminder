#a = True
#print(a:=False)

# numbers = [1,2,3,4,5]

# while(n:=len(numbers)>0):
#     print(numbers.pop())



# foods = list()
# while True:
#     food = input("what food do you like ?:")

#     if food == "quit":
#         break

#     foods.append(food)

# ----------------OR with Walrus Operator------------------

foods = list()
while(food:= input("what do you like ?:"))!= "quit":
    foods.append(food)