"""
Write a function that takes in a non-empty array of distinct integers and an
integer representing a target sum. If any two numbers in the input array sum
up to the target sum, the function should return them in an array, in any
order. If no two numbers sum up to the target sum, the function should return
an empty array.
"""
    
    
def two_num_sum(arr, target_sum):
    """
    Brute-force 1: two for loops (0(n^2))
    not time optimal

    Args:
        arr (list): _description_
        target_sum (int): _description_
    """
    
    for i in range(len(arr)):
        
        for j in range(len(arr)):
            if i == j:
                continue
            current_sum = arr[j] + arr[i]
            if  current_sum == target_sum:
                return [arr[i], arr[j]]
    return []
    
def two_num_sum(arr, target_sum):
    """
    Brute-force 2: two for loops (0(n^2)) space o(1)
    not time optimal

    Args:
        arr (list): _description_
        target_sum (int): _description_
    """
    
    for i in range(len(arr)): # o(n) 
        diff = target_sum - arr[i]
        
        if diff in arr[:i] or diff in arr[i+1:]:# o(n) 
            return [arr[i], diff]
    return []
    
def two_num_sum(arr, target_sum):
        """
        Keep all the already seen items in a hash table
        Time complexity is o(n) as the array is iterated over once
        Difference stored in a hash 

        Args:
            arr (list): _description_
            target_sum (int): _description_
        """
        seen ={}
        for item in arr: # o(n)
            diff = target_sum - item# o(1)
            
            if diff in seen: # o(1) -> the key (diff) is hashed then checked in the hashtable
                return [item, diff] # o(1) 
            seen[diff] = True # o(1) 
        return [] # o(1) 
    

def two_num_sum(arr, target_sum):
    """
    Sort the array
    Add the first item in the array to the last item in the array while tracking their indices
    If the sum is larger than target sum, decrement the larger index
    if the sum is smaller than the target sum, increment the smaller index
    break when the indices are equal
    
    Time complexity(o(n))
    space complexity (o(1))

    Args:
        arr (list): _description_
        target_sum (int): _description_
    """
    arr.sort() #n log n
    start_index = 0
    end_index = len(arr) - 1
    
    while start_index < end_index: # o(n)
        current_sum = arr[start_index] + arr[end_index]
        
        if current_sum > target_sum:
            end_index -= 1
        elif current_sum < target_sum:
            start_index += 1
        
    return []