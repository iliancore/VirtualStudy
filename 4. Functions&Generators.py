import math


# 1.
def check_string(*args):
    """
    The function checks all function arguments for compliance with the String type.
    :param args: One or more values of the same or different type
    :return: bool
    """
    for arg in args:
        if not isinstance(arg, str):
            return False
    return True


print("1. Check all arguments for compliance with the String type:")

result = check_string("hello", "world", "123")
print('Example 1: "hello", "world", "123" is {}'.format(result))

result = check_string("hello", "world", 123)
print('Example 2: "hello", "world", 123 is {}'.format(result))


# 2.
def calculate_square(side):
    area = side ** 2
    perimeter = 4 * side
    diagonal = math.sqrt(2 * side ** 2)
    return area, perimeter, diagonal


square_side = 10
square_area, square_perimeter, square_diagonal = calculate_square(square_side)
print("\n2. Side - {} \n Area- {} \n Perimeter- {} \n Diagonal- {}"
      .format(square_side, square_area, square_perimeter, square_diagonal))






