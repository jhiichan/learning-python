# Sets

num1 = {1, 2, 3, 4, 5, 5}

# adding
num1.add(100)
num1.add(2)
print(num1)

# convert to set
my_list = ['water', 'water', (1, 2), (1, 2), 1000, 1000]
list_to_set = set(my_list)
print(my_list)
print(list_to_set)

# comparison
yorha_2b = {'YoRHa', 'YoRHa Android', 'Female', 'Silvery White Hair', 'Gray Blue Eye', 168, 148.8}
yorha_9s = {'YoRHa Scanning Unit', 'YoRHa Android', 'Male', 'Silvery White Hair', 'Light Blue Eye', 160, 129.9}

print(yorha_2b.difference(yorha_9s))
print(yorha_2b.intersection(yorha_9s))
print(yorha_2b.union(yorha_9s))