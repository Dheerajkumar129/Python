#1. Right-Angled Triangle
def right_angled_triangle(rows):
    for i in range(1, rows + 1):
        print('*' * i)

right_angled_triangle(5)

#2. Inverted Right-Angled Triangle
def inverted_right_angled_triangle(rows):
    for i in range(rows, 0, -1):
        print('*' * i)
        
inverted_right_angled_triangle(5)

#3. Full Pyramid
def full_pyramid(rows):
    for i in range(1, rows + 1):
        print(' ' * (rows - i) + '*' * (2 * i - 1))

full_pyramid(5)


#4. Inverted Pyramid
def inverted_pyramid(rows):
    for i in range(rows, 0, -1):
        print(' ' * (rows - i) + '*' * (2 * i - 1))

inverted_pyramid(5)


#5. Diamond Pattern
def diamond_pattern(rows):
    for i in range(1, rows + 1):
        print(' ' * (rows - i) + '*' * (2 * i - 1))
    for i in range(rows - 1, 0, -1):
        print(' ' * (rows - i) + '*' * (2 * i - 1))

diamond_pattern(5)


#6. X Pattern
def generate_x_pattern(size):
    for i in range(size):
        line = [' '] * size
        line[i] = '*'
        line[size - 1 - i] = '*'
        print(''.join(line))

if __name__ == '__main__':
    size = 5
    generate_x_pattern(size)