# Define a list
my_list = [1, 2, 3, [4, 5, 6], 7, 8, 9]

# Nested List
print("Nested List:", my_list)

# Length of List
print("Length of List:", len(my_list))

# Concatenation of Lists
new_list = [10, 11, 12]
result = my_list + new_list
print("Concatenated List:", result)

# Membership Test
print("Is 4 in my_list?", 4 in my_list)

# Iteration through List
print("Elements of my_list:")
for item in my_list:
    print(item)

# Indexing
print("First element of my_list:", my_list[0])

# Slicing
print("Sliced List:", my_list[2:5])
