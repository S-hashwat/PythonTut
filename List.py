#LIST :- 
List1 = ["India", "America", "Russia", "England", "Australia"]
# print(List1) This will print the list

# print(List1[::3]) In this the index mentioned(1) after the dots means that the string will print till that index

# print(List1[0::2]) 
# List1[ start : stop : step ] start = 0: Start from index 0 (i.e., the first element). 
# #stop = omitted: So it goes till the end of the list.
# #step = 2: It picks every 2nd element, i.e., it skips one element in between
# #It will print every alternate element starting from index 0.

# print(List1[-1]) It will reverse the string

# del List1[2] It will delete the element
# print(List1)


# List Methods
# 1. Append Method - we can append the item at the end of the list
# List1.append("Pakistan")  
# print(List1)

# 2.Insert Method - we can insert the item at any place in the list
# List1.insert(3, "Ukraine") 
# print(List1)

#3 Swap the values method 1
# temp = List1[3]
# List1[3] = List1[0]
# List1[0] = temp
# print(List1)

# Method 2 for swapping the values 
# List1[0], List1[3] = List1[3], List1[0]
# print(List1)

#4 Sort Method
# numbers = [90, 20, 50, 79, 19, 34, 235, 73, 12, 57, 124]
# numbers.sort()
# print(numbers)

#5 Reverse Method - 
# numbers = [90, 20, 50, 79, 19, 34, 235, 73, 12, 57, 124]
# numbers.reverse()
# print(numbers)

#6 Extend Method - Adds elements of an iterable (list, tuple, etc.) to the end.
# lst = [1, 2, 4, 5, 6, 8, 2,3,4,4,1]
# lst.extend([10, 7,8,9,10,11,12,13,14,15,10,10,10,10,10]) #extend the list 
# print(lst)


#7 Remove Method - remove the 2nd index element
# lst.remove(2) 
# print(lst)

#8 Pop Method - Remove the last item by default
# lst.pop()
# print(lst)

#9 Count Method - Count the items 
# lst3 = [1, 2, 2, 3]
# print(lst3.count(2))
