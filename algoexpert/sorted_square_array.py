    """
    
  Write a function that takes in a non-empty array of integers that are sorted
  in ascending order and returns a new array of the same length with the squares
  of the original integers also sorted in ascending order.
    """
    
def sorted_squared_array(sorted_array):
    result = [None for _ in sorted_array]
    idx = end_idx = len(sorted_array) - 1
    start = 0
    
    while idx >= 0:
        start_value= abs(sorted[start])
        end_value = abs(sorted_array[end_idx])
        
        if start_value > end_value:
            result[idx] = start_value * start_value
            start += 1
        else:
            result[idx] = end_value * end_value
            end_idx -= 1
        
        idx -= 1
    
    return result