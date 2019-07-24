def longest_palindromic_substring(s1, start_index, end_index):
    if len(s1) < 0 or start_index >= len(s1) or end_index >= len(s1) or start_index < 0 or end_index < 0:
        return 0
    if start_index == end_index:
        return 1
    c1 = 0
    if s1[start_index] == s1[end_index]:
        remaining_length = end_index - (start_index + 1)
        if remaining_length == longest_palindromic_substring(s1, start_index + 1, end_index - 1 ):
            c1 = 2 + remaining_length

    c2 = 0 + longest_palindromic_substring(s1, start_index, end_index - 1 )
    c3 = 0 + longest_palindromic_substring(s1, start_index + 1, end_index  )
    return max(c1, c2, c3)

print(longest_palindromic_substring('sukuma', 0, len('sukuma') - 1))