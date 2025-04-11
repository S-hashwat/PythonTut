# Operators - 
# AND , OR Operators

# AND Operator Chart 
# TRUE + TRUE = True
# FALSE + TRUE = False
# FALSE + FALSE = False
# True + False = False

# OR OPERATOR CHART
# TRUE + FALSE = True
# FALSE + TRUE = True
# TRUE + TRUE = True
# FALSE + FALSE = FALSE

Age1 = 19
Age2 = 25

if(Age1 and Age2 >= 18):
    print("The person is adult")
elif(Age1 or Age2 <= 18 ):
    print("The person is not adult ")