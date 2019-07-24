
def knapsack_aux(profits: list, weights, capacity, current_index):
   
    if capacity <= 0 or current_index < 0 or current_index >= len(profits) or current_index >= len(weights) :
        return 0
    profit_1 = 0
    if weights[current_index] <= capacity:
        capacity = capacity - weights[current_index]
        profit_1 =  profits[current_index] + knapsack_aux(profits, weights, capacity, current_index + 1)
    profit_2 = knapsack_aux(profits, weights, capacity, current_index + 1)
    return max(profit_1, profit_2)

print(knapsack_aux([13,4,5,3,5], [2,3,2,6,6], 10, 0))