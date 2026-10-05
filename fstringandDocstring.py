#-------------- fString -----------------

letter = "hey my name is {1} and I am from {0}"
country ="India"
name ="Prabhakar"


print(letter.format(country,name))
print(f"hey my name is {name} and I am from {country}")
print(f"we want to print fstring as it is....hey my name is {{name}} and I am from {{country}}")


# txt = "for only {price:.2f} dollors!"
# print(txt.format(price = 49.099999))
price = 49.09999
txt = f"for only {price:.2f} dollors!"
print(txt)

#---------------------- DocString -----------------
#doc string always write just above the function definition otherwise it will not be docstring 
def square(n):
    """Takes in a number n, returns the square of n"""
    print(n**2)

square(5)
print(square.__doc__)



