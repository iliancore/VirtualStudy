# 1.
def fibonacci(array_size):
    """
    Recursive calculation of the n-th number of the Fibonacci series.
    :param array_size:
    :return: array
    """
    array = [0, 1]
    if array_size <= 0:
        array = []
    elif array_size < 2:
        array = [0]
    else:
        stage = 0
        while stage != array_size - 2:
            new_digit = array[-1] + array[-2]
            array.append(new_digit)
            stage += 1
    return array


numbers_in_array = int(input('1. Enter the number of Fibonacci digits - '))
print('1. Your Fibonacci series from {} numbers - {}\n'.format(numbers_in_array, fibonacci(numbers_in_array)))

# 2.
sort_list = []

for i in range(1, 101):
    None if (i % 3) != 0 else sort_list.append(i)

print('2. List of multiples of three \n   {}\n'.format(sort_list))

# 3.
sum_list = []
print('3. Enter 10 numbers:')
for i in range(10):
    number_in_list = int(input('3. {} new number in list {} is - '.format(i+1, sum_list)))
    sum_list.append(number_in_list)

print('3. The sum of the entered numbers is - {}\n'.format(sum(sum_list)))

# 4.
choice = int
while choice != 0:
    choice = int(input('4. Enter any number to continue.\n   Enter "0" to stop input.\n\t'))

# 5.
a = int(input('\n5. Enter First Variable '))
b = int(input('5. Enter Second Variable '))
formula = (4 * a) ** b
print('5. (4 * a) ** b = {}'.format(formula))

c = a
a = b
b = c
new_formula = (4 * a) ** b
print('5. (4 * a) ** b = {}'.format(new_formula))
