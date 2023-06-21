# 1.
def last_lines(file_path, num_lines):
    """
    Calls a function specifying 'file_path' and the number of last lines 'num_lines' to be output.
    :param file_path: File name
    :param num_lines: Number of lines from the end
    :return: The last lines
    """
    with open(file_path, 'r') as file:
        lines = file.readlines()
        last_line = lines[-num_lines:]
        for line in last_line:
            print(line.strip())


file_path = r'C:\Users\IlIaN\Desktop\example.txt'
num_lines = 5

print("\n 1. Last 5 lines in this file:")
last_lines(file_path, num_lines)


# 2
def multiples_numbers_to_list(numbers, multiple_num):
    """
    The function defines a range from 0 to 'numbers' and marks all numbers divisible by 'multiple_num'.
    A list of multiples is saved in the file 'num100.txt'.
    :param numbers: [int]
    :param multiple_num: [int]
    :return: list
    """
    multiples_of_num_list = [num for num in range(0, numbers + 1) if num % multiple_num == 0]
    with open('num100.txt', 'w') as file:
        file.write("{}".format(multiples_of_num_list))
    return multiples_of_num_list


print("\n 2. Numbers multiple of 5 from 0 to 100 \n{}".format(multiples_numbers_to_list(100, 5)))


# 3
def number_of_lines(count=0):
    """

    :param count:
    :return:
    """
    with open(file_path, 'r') as file:
        return sum(1 for line in file if line.strip())


file_path = 'num100.txt'
print("\n 3. Number of lines in the file - {}".format(number_of_lines()))


# 4
def file_reader(file_path):
    """

    :param file_path:
    :return: [list]
    """
    with open(file_path, 'r') as file:
        text_input = file.read()
        return list(text_input)


# print(file_reader(r'C:\Users\IlIaN\Desktop\example.txt'))
print(file_reader(input("\n 4. Enter your File Path - ")))
