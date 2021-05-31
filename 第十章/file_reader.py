filename = 'pi_digits.txt'

with open(filename) as file_project:
    lines = file_project.readlines()
    for line in lines:
        print(line, end='')
