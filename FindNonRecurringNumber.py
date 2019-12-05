# Python code to demonstrate the working of 
# array(), append(), insert() 

# importing "array" for array operations 
import array 

# initializing array with array values 
# initializes array with signed integers 
arr = array.array('i', [1, 3, 3, 3,9,9,9]) 

# printing original array 
print ("The new created array is : ") 
for i in range (0, 7): 
	print (arr[i]) 

print("\r") 

# using append() to insert new value at end 
arr.append(4); 

# printing appended array 
print("The appended array is : ") 
for i in range (0, 8): 
	print (arr[i]) 
	
# using insert() to insert value at specific position 
# inserts 5 at 2nd position 
arr.insert(2, 5) 

print("\r") 

# printing array after insertion 
print ("The array after insertion is : ") 
for i in range (0, 9): 
	print (arr[i]) 
