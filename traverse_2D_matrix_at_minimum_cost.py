def traverse_2D_matrix_at_minimum_cost(matrix, start_row, start_col):
    if start_row >= len(matrix) or start_col >= len(matrix[0]) or start_col < 0 or start_col < 0:
        return 0
    if start_row == (len(matrix) - 1) and start_col == (len(matrix[0]) - 1) :
        return matrix[len(matrix) - 1][len(matrix[0]) - 1]
    c1 =  traverse_2D_matrix_at_minimum_cost(matrix, start_row + 1 , start_col)
    c2 =  traverse_2D_matrix_at_minimum_cost(matrix, start_row , start_col + 1)
    current_cost = matrix[start_row][start_col]
    return min(c1, c2) + current_cost
matrix = [[0, 1, 1, 4], [1,2,3,1]]
print(traverse_2D_matrix_at_minimum_cost(matrix, 0, 0))