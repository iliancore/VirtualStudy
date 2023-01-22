# 1.
import math

radius = r = 4
circle_length = 2*math.pi*r

print('1. Circle length is {}!'.format(circle_length))

# 2.
some_string = "My name is Python"

print('2. String length is {}!'.format(len(some_string)))

# 3.
list_numbers = [1, 8, 5, 4, 12]

print('3. Average of the list is {}!'.format((sum(list_numbers) / len(list_numbers))))

# 4.
dict_movies = {'The Shawshank Redemption': 9.3, 'The Godfather': 9.2,
               'The Dark Knight': 9.0, 'The Godfather Part II': 9.0, '12 Angry Men': 9.0}

print('4. Top 5 IMDB ratings is {}!'.format(dict_movies.items()))

# 5.
some_list = ('A', 1, "3D")

print('5. The first element from list is {}!'.format(some_list[0]))

# 6.
py_str = 'python'

print('6. Upper string is {}!'.format(py_str.upper()))

# 7.
kilobyte = 1
byte = 1024 * kilobyte
bit = byte * 8

print('7. Kilobyte is {} bits!'.format(bit))

# 8.
py_str_up = 'P Y T H O N'
print('8. Crop space in string. String after format is {}!'.format(py_str_up.replace(" ", "")))
