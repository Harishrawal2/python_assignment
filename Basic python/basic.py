#  Write a program to print your name. 

print("Harish")

#  Write a program for a Single line comment and multi-line comments 
print("# This is Comment Program")

# Define variables for different Data Types int, Boolean, 
# , float, double and print on the Console 

# Thisis int data Type
a = 5
print(a, "is of type", type(a))

# This is float data type
a = 2.0
print(a, "is of type", type(a))

# This is Complext data type
a = 1+2j
print(a, "is complex number?", isinstance(1+2j,complex))

# This is Bolean data type
x = (1 == True)
y = (1 == False)
a = True + 4
b = False + 10

print("x is", x)
print("y is", y)
print("a:", a)
print("b:", b)



# Define the local and Global variables with the same name and print both variables and 
# understand the scope of the variables 

# Create a Global Variable
x = "global"

def foo():
    print("x inside:", x)


foo()
print("x outside:", x)


# Accessing local variable outside the scope
def foo():
    y = "local"
    print(y)


foo()











