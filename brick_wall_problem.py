import itertools
import collections
def least_bricks(wall):
    """cut through a brick wall while crossing least nimber of bricks"""
    return len(wall) - max(collections.Counter([col for row in wall for col in itertools.accumulate(row[:-1])]).values(), default=0)

def least_bricks_2(wall):
    """use collections.Counter"""
    counter = collections.Counter()
    for row in wall:
        line_length = 0
        for idx, col in enumerate(row):
            if idx == len(row) - 1:
                 break
            line_length += col
            counter[line_length] += 1
    return len(wall) - max(counter.values())

def least_bricks_with_dict(wall):
    counter = dict()
    for row in wall:
        col_sum = 0
        for col in row:
            col_sum += col
            if col_sum == sum(row):
                break
            counter[col_sum] = counter.setdefault(col_sum, 0) + 1
    return len(wall) - max(counter.values() if counter else 0)

def least_bricks_default_dict(wall):
    counter = collections.defaultdict(int)
    for row in wall:
        sum_col = 0
        for col in row:
            sum_col += col
            if sum_col == sum(row):
                break
            counter[sum_col] += 1
    return len(wall) - max(counter.values(), default=0)

wall = [[1,2,2,1],
        [3,1,2],
        [1,3,2],
        [2,4],
        [3,1,2],
        [1,3,1,1]]


print('1 ', least_bricks(wall))
print('2 ', least_bricks_2(wall))
print('3 ', least_bricks_with_dict(wall))
print('4 ', least_bricks_default_dict(wall))