# Function

def buy_things(my_list):
    for item in my_list:
        print(f'Buy {item}')

my_list = ['Apple', 'Oil', 'Ham', 'Ketchup']
buy_things(my_list)

# default parameters
def should_drink_coffee(is_sleepy = False):
    if(is_sleepy):
        print('Drink Coffee!')
    else:
        print('Continue what you are doing...')

should_drink_coffee()
should_drink_coffee(True)