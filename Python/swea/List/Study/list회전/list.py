


def rotate_90(matrix):

    transpose = list(zip(*matrix))
    for row in transpose:
        print(row)
    rotate = [list(row)[::-1] for row in transpose]
    return rotate



array = [[1,2,3], [4,5,6], [7,8,9]]

for row in array:
    print(row)


rotate_arr = rotate_90(array)




for row in rotate_arr:
    print(row)