# def func1():
#  a =input("Enter the number: ")
#  print(f"Multiplication table of {a} is:")

#  try:
#   for i in range(1,11):
#     print(f"{int(a)}X{i} = {int(a)*i}")

#  except Exception as e:
#   print("Sorry pleas give valid integer",e)
#  finally:
#   print("Some imp lines of code")

# x = func1()


# -------------------Custom Error -------------------------

a = int(input("Enter any value between 5 and 9"))

if(a<5 or a>9):
    raise ValueError("Value should be between 5 and 9")