def longest_common_subsequence(s1, s2, i1, i2):
    if i1 >= len(s1) or i1 < 0 or i2 >= len(s2) or i2 < 0:
        return 0
    c3 = 0
    if s1[i1] == s2[i2]:
        c3 = 1 + longest_common_subsequence(s1, s2, i1 + 1, i2 + 1)
    c1 = 0 + longest_common_subsequence(s1, s2, i1 , i2 + 1)
    c2 = 0 + longest_common_subsequence(s1, s2, i1 + 1 , i2)
    return max(c1,c2,c3)

print(longest_common_subsequence('test', 'msk2', 0, 0))