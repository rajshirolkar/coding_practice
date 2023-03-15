my_list = [1, 2, 3, 4]
# Append an element to the end of the list
my_list.append(5)
print(my_list)  # [1, 2, 3, 4, 5]

# Insert an element at a specific position
my_list.insert(1, 6)
print(my_list)  # [1, 6, 2, 3, 4, 5]

# Remove an element from the list
my_list.remove(6)
print(my_list)  # [1, 2, 3, 4 ,5]

# Pop an element from a specific position
my_list.pop(0)
print(my_list)  # [2 ,3 ,4 ,5]

# Reverse a list
my_list.reverse()
print(my_list)  # [5 ,4 ,3 ,2]

# Sort a list
my_list.sort()
print(my_list)  # [2 ,3 ,4 ,5]

my_list = [1, 2, 3, 4, 5]

# Slicing a list
print(my_list[1:4])  # [2 ,3 ,4]
print(my_list[:3])  # [1 ,2 ,3]
print(my_list[2:])  # [3 ,4 ,5]

# List comprehension
squared_list = [x**2 for x in my_list]
print(squared_list)  # [1 ,4 ,9 ,16 ,25]

# Nested lists
nested_list = [[1, 2], [3, 4]]
flattened_list = [item for sublist in nested_list for item in sublist]
print(flattened_list)  # [1 ,2 ,3 ,4]

my_list = [1, 2, 3, 4, 5]

# Extract every third element starting from the first element
print(my_list[::3])  # [1 ,4]

# Extract every third element starting from the second element
print(my_list[1::3])  # [2 ,5]

# Extract a portion of the list in reverse order
print(my_list[3:0:-1])  # [4 ,3 ,2]
