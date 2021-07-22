# Boolean and Conditional

# Uppercase letters are smaller than lowercase letters
print('M' < 'm') #True

# digits are smaller than letters
print('1' < 'a') #True

# True has a value of 1
print(True == 1) #true
print(True + True) #2
print(True + 3) #4

# False has a value of 0
print(False == 0) #true
print(False + False) #0
print(False + True) #1

# if statement
sleepy = True
if sleepy:
    print('Get Coffee!')

# if else statement
sleepy = False
if sleepy:
    print('Get Coffee!')
else:
    print('Continue what you are doing...')

# else if Statement
day = 'Sunday'
if day == 'Saturday':
    print('Freedom!')
elif day == 'Sunday':
    print('Shopping!')
else:
    print ('Work!')
