def number_of_paths_at_cost(cost_matrix, row, col, cost):
    if row < 0 or col < 0 or row >= len(cost_matrix) or col >= len(cost_matrix[0]) or cost < 0:
        return 0
    if row == 0 and col == 0:
        return 0
    if row == len(cost_matrix) and col == len(cost_matrix[0]):
       if cost == cost_matrix[row][col]:
           return 1
       return 0
    if row == 0 and col == 0:
        if cost - cost_matrix[0][0] == 0:
            return 1
        return 0
        
    c1 = 0 +number_of_paths_at_cost(cost_matrix, row, col - 1, cost - cost_matrix[row][col])
    c2 = 0 + number_of_paths_at_cost(cost_matrix, row - 1, col, cost - cost_matrix[row][col])

    return c1 + c2