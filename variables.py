# Variables are like a bucket which stores something. In our case variables store values 
# Rules of variables :
# 1) A variable name must start with a letter or the underscore character
# 2) A variable name cannot start with a number
# 3) A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# 4) Variable names are case-sensitive (age, Age and AGE are three different variables)
# 5) A variable name cannot be any of the Python keywords.
# 6) Variable should not contain space in between

# Legal variable names:

# myvar = "John"
# my_var = "John"
# _my_var = "John"
# myVar = "John"
# MYVAR = "John"
# myvar2 = "John"

# Illegal variable names:

# 2myvar = "John"
# my-var = "John"
# my var = "John"


# MOST IMPORTANT VARIABLES IN PYTHON CAN BE REDECLARED It means you can assign a new value to 
# an existing variable name at any time, even if it's a different type (like number, string, list, etc.).

# For example - 
# x = 10        # Initially, x is an integer
# print(x)      # Output: 10

# x = "Hello"   # Now x is reassigned to a string
# print(x)      # Output: Hello

# x = [1, 2, 3] # Now x is reassigned to a list
# print(x)      # Output: [1, 2, 3]


y = 5
y = "Jack"
print(y)
