# for i in range (-1,2):
#     for j in range(-1,2):
#         print(i,j)


# Flags to remember if first row/col should be zeroed

matrix = [[1,0,3]]
first_row_zero = any(matrix[0][c] == 0 for c in range(len(matrix[0]))) #any() returns True if any element of the iterable is true. Here, it checks if any element in the first row is zero.
first_col_zero = any(matrix[r][0] == 0 for r in range(len(matrix)))
print(first_row_zero)
print(first_col_zero)
print((matrix[0][c] == 0 for c in range(len(matrix[0])))) # this is a generator expression, which creates an iterator that yields items one at a time. It will yield True for each element in the first row that is zero, and False for non-zero elements. The any() function will consume this generator to determine if any of the yielded values are True.
