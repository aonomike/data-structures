# Given a list of numbers with only 3 unique numbers (1, 2, 3), sort the list in O(n) time.
#Input: [3, 3, 2, 1, 3, 2, 1]
#Output: [1, 1, 2, 2, 3, 3, 3]
def sort_nums(nums):
    lookup = {}
    for n in nums:
        if n in lookup:
            print(n)
            lookup[n] = lookup[n].append(n)

        else:
            lookup[n] = [n]
    sorted(lookup)
    look = [ [].append(l) for l in lookup] 
    return look
sort_nums([3, 3, 2, 1, 3, 2, 1])
