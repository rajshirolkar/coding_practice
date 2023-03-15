my_dict = {'a': 1, 'b': 2, 'c': 3}

# Accessing a value by key
print(my_dict['a'])  # 1

# Adding a new key-value pair
my_dict['d'] = 4
print(my_dict)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Updating a value by key
my_dict['a'] = 5
print(my_dict)  # {'a': 5, 'b': 2, 'c': 3, 'd': 4}

# Removing a key-value pair
del my_dict['b']
print(my_dict)  # {'a': 5, 'c': 3 , 'd' :4}

# Checking if a key exists in the dictionary
print('c' in my_dict)  # True

# Iterating over keys and values in a dictionary
for key, value in my_dict.items():
    print(key, value)

# Counting the frequency of elements in a list using a dictionary
my_list = [1, 2, 3, 1, 2, 3, 4]
freq_dict = {}

for item in my_list:
    if item in freq_dict:
        freq_dict[item] += 1
    else:
        freq_dict[item] = 1

print(freq_dict)  # {1: 2 ,2: 2 ,3: 2 ,4: 1}
