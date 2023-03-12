"""

Given two non-empty arrays of integers, write a function that determines
whether the second array is a subsequence of the first one.

A subsequence of an array is a set of numbers that aren't necessarily adjacent
in the array but that are in the same order as they appear in the array. For
instance, the numbers [1, 3, 4] form a subsequence of the array [1, 2, 3, 4] , and so do the numbers
[2, 4]. Note that a single number in an array and the array itself are both valid
  subsequences of the array.
  
"""

def current_sequence_index(arr, sequence):
    
    current_sequence_index = 0
    for i in arr:
        if current_sequence_index == len(sequence):
            break
        if i == sequence[current_sequence_index]:
            current_sequence_index += 1
        
    return current_sequence_index == len(sequence)
    
    
current_sequence_index([1,2,3], [1,3]) #true
current_sequence_index([1,2,3], [3,1]) #false
current_sequence_index([1,2,3], [4,1]) #false
