def print_array_spiral(matrix, start_row, start_col, last_row, last_col):
    # columns => 
    # rows 
    # v
    # (0, 0) .. (0, len(matrix[0]) - 1)
    # ..
    
    # for c in col_limit:
    #     print(matrix[row][c])

    
    # if row == 0 and col == 0:
    #     print(matrix[row][col])
    #     print_array_spiral(matrix, row, col + 1, row_limit, col_limit)
    # # (len(matrix) - 1, 0).. (len(matrix) -1, len(matrix[n - 1]) - 1)
    # elif row == 0 and (col == len(matrix[row]) - 1):
    #     print(matrix[row][col])
    #     print_array_spiral(matrix, row + 1, col)
    # elif row == (len(matrix) - 1) and (col == len(matrix[row]) - 1):
    #     print(matrix[row][col])
    #     print_array_spiral(matrix, row , col -1 )
    
    # elif row == (len(matrix) - 1) and (col == 0):
    #     print(matrix[row][col])
    #     row -= 1
    #     print_array_spiral(matrix, row - 1 , col )
    # first cell 0,0 (increment the column)

    # 0, len(matrix[0]) - 1 increment the row

    # len(matrix - 1), len(matrix[n-1]) -1 decrement the column

    # len(matrix - 1), len(matrix[0]) - 1 decrement the row until 

    #  [ [2],[3,4]]

    # [[2, 3, 4], [1], [5, 6], [7, 8, 9, 10]]
    # 2, 3, 4, 1, 6, 10, 9, 8, 7, 5

    # row = 0 , col= 0, row_limit = 4, col_limit = 4 
    # col = 0, 1, 2, 3 ?? col_limit
    # row = 0, 1, 2, 3 ?? row_limit
    # col = 3, 2, 1, 0 ?? 
    # row = 3, 2, 1 ?? row_limit = 3
    # col = 0, 1, 2 col_limit = 3
    # row = 1, 2 row_limit = 2
    # col = 2, 1 col_limit = 2
    # [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    # 1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10 

    # [a] => a
    # [[a, b], [c, d]]
    # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    # [0, 0] => [0, col_limit - 1] => [row_limit - 1, ccol_limit - 1] => [row_limit - 1, 0] |=>| [1, 0] => [1, col_limit - 2] 
    # => [row_limit - 2, col_limit - 2] |=>| [row_limit - 2, col_limit - 3]


    # start with r=0,c=0, r_l = len(matrix), col_limit(len(matrix[0]))
    
    # when in bottom left decrement the c_l and r_l
    while start_col < last_col and start_row < last_row:

        for i in range(last_col):
            print(matrix[start_row][i])
        start_row += 1

        for i in range(start_row, last_row):
            print(matrix[i][last_col - 1])
        last_col -= 1

        if last_col > start_col :
            for i in range(last_col - 1, start_col, -1):
                print(matrix[last_row - 1][i])
            last_row -= 1
        
        if last_row > start_row:
            for i in range(last_row, start_row, -1):
                print(matrix[i][start_col])
            start_col += 1

print_array_spiral([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 0, 0, 3, 3)
