#Given a list of numbers, where every number shows up twice except for one number, find that one number.
#Input: [4, 3, 2, 4, 1, 3, 2]
#Output: 1

def single_number(nums):
    lookup = {}

    for n in nums:
        lookup[n] = 1 if n not in lookup else lookup[n] + 1

    keys = lookup.keys()

