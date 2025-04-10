# Highest Priority operators :-
# 1) ** (Exponent)
# 2) + (Unary Addition),  - (Unary Subtraction)
# 3) * (Multiplication), / (Division), // (Floor Division (it means it rounds of to smallest integer value)), % (modulus)
# 4) + (Binary(there must be some number in both sides of the operand) Addition),  - (Binary Subtraction)


# NOTE SUB EXPRESSIONS LIKE 2*(2+5) the values inside the bracket is calculated first
#Example 

# print(+5 + -5** - 4* 13 + 4 - 10)

#First it will focus on -5**-4 
# This is evaluated as:

# -(5 ** - 4)
# = - (1 / (5 ** 4))
# = - (1 / 625)
# = -0.0016

# So, now the expression becomes:
# +5 + -0.0016 * 13 + 4 - 10

# Now next priority is of multiplication
# -0.0016 * 13 = -0.0208 

# So now the expression becomes:
# +5 + (-0.0208) + 4 - 10 

# Left to Right: Addition and Subtraction
# +5 + (-0.0208) = 4.9792
# 4.9792 + 4 = 8.9792
# 8.9792 - 10 = -1.0208

# So the output will be:
# -1.0208

# print(6. // 4)

# x = 10 / 4
# y = 5 / 2.0
# print (x + y)

# print(100 / 50 )

print(2 ** 3.)