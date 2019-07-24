# Given a number n, calculate the number of ways I can express n as a sum of 1,3 and 4

def number_factor(n):
    if n < 0 :
        return 0
    if n == 0 or n == 1 or n == 2:
        return 1
    if n == 3:
        return 2
    return number_factor(n - 4) + number_factor(n - 3) + number_factor(n-1)

# print(number_factor(50))

def number_factor_top_down(n, mem):
    if n < 0 :
        mem[0] = 0
    if n == 0 or n == 1 or n == 2:
        mem[n] = 1
    if n == 3:
        mem[n] = 2
    if n not in mem:
        fours = number_factor_top_down(n-4, mem)
        threes = number_factor_top_down(n-3, mem)
        ones = number_factor_top_down(n-1, mem)
        mem[n] = ones + threes + fours
    return mem[n]

print(number_factor_top_down(50, {}))

def number_factor_bottom_up(n):
    mem = {}
    mem[0]= mem[1]= mem[2]= 1
    mem[3] = 2
    for i in range(4, n + 1):
        mem[i] = mem[i-4] + mem[i-3] + mem[i-1]
    return mem[n]

print(number_factor_bottom_up(50))