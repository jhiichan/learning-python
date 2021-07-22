# Strings

# single quotes
word1 = 'Hello'

# double quotes
word2 = "World"

print(type(word1))
print(type(word2))

# escape characters
print('doesn\'t')

# using double quotes
print("doesn't")

# raw strings
print(r'C:\users\name')

# multiline
print("""
Hello!
World!
""")

print('''
Hello!
World!
''')

# using operators
print(word1 + word2) #will display HelloWorld
print(word1 * 4) #will repeat Hello 4x

# index
print(word1[1]) #prints second letter `e`
print(word1[-1]) #prints letter starting from the right `o`