print("don")

# Python program to print list 
# using for loop 
a = [1, 2, 3, 4, 5] 

# printing the list using loop 
for x in range(len(a)): 
	print a[x], 
  
###########################################################

# Python program to print list 
# by Converting a list to a  
# string for display 
a =["Geeks", "for", "Geeks"] 
  
# print the list using join function() 
print(' '.join(a)) 
  
# print the list by converting a list of  
# integers to string  
a = [1, 2, 3, 4, 5]  
print str(a)[1:-1]  

###########################################################

# Python program to print list 
# print the list by converting a list of  
# integers to string using map 
  
a = [1, 2, 3, 4, 5] 
print(' '.join(map(str, a)))  
  
print"in new line"
print('\n'.join(map(str, a))) 
