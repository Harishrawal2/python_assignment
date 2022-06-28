# 1. Define a static variable and access that through a class  
# 2. Define a static variable and access that through a instance 
# 3. Define a static variable and change within the instance 
# 4. Define a static variable and change within the class 


# Define a static variable and access that through a class.

class Python:
# Access through class    
 staticVariable = 9 
print(Python.staticVariable)

#Change within an class
Python.staticVariable = 12
print(Python.staticVariable) # Gives 12

#Access through an instance
instance = Python()
print(instance.staticVariable) # Gives 12

#Change within an instance
instance.staticVariable = 15
print(instance.staticVariable) # Gives 15
print(Python.staticVariable) #Gives 12