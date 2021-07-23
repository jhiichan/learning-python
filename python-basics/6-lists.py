# Lists

nums = [1, 2, 3, 4, 5]
shopping_cart = ['shirts', 'pants', 'pencil', 'phone']

# nested
nested_list = [1, 2, 3, 'a', 'b', 'c', True, False]

# one item
num = [1,]

# accessing lists
print(nested_list[0])
print(nested_list[3])
print(nested_list[6])

# slicing
print(nested_list[0:3])
print(nested_list[3:6])
print(nested_list[6:8])

# adding
shopping_cart.append('shampoo')
print(shopping_cart)

nested_list.insert(6, 'd')
print(nested_list)

# removing
nums.pop() #removes the last item
nums.pop(0) #removes the item in the given index
print(nums)

nested_list.remove('d') #removes the item 'd'
print(nested_list)