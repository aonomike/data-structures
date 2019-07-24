def longest_palindromic_subsequence(s1, start_index, end_index):
    if len(s1) < 1 or start_index >= len(s1) or start_index > end_index:
        return 0
    if start_index == end_index:
        return 1
    
    count = 0
    if s1[start_index]  == s1[end_index]:
        count = 2 + longest_palindromic_subsequence(s1, start_index + 1, end_index - 1)
    c2 = longest_palindromic_subsequence(s1, start_index + 1, end_index)
    c3 = longest_palindromic_subsequence(s1, start_index, end_index - 1)
    return max(count, c2, c3)

print(longest_palindromic_subsequence('zoom', 0, 3))