while True:
    try:
        age = int(input('Age: '))
        print(age)
    except ValueError as error:
        print(f'Please enter a number. {error}')
    else:
        print('Thank you!')
        break
