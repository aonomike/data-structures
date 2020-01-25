#  A palindrome is a sequence of characters that reads the same backwards and forwards. Given a string, s, find the longest palindromic substring in s.


# Input: "banana"
# Output: "anana"
# Input: "million"
# Output: "illi"

def longest_palindromic_substring(s: str) -> str:
    return logest(s, 0, len(s)-1)

def longest(s, start_index, end_index):
    if start_index > end_index:
        return ''

    if start_index == end_index:
        return s[start_index]
    
    l1 = ''
    l2 = ''
    if s[start_index] == s[end_index]:
        l1 = s[start_index] + longest(s, start_index + 1, end_index - 1) + s[end_index]
        if s == l1
    else:
        l2 = max(longest(s, start_index + 1, end_index), longest(s, start_index, end_index - 1))
    return l1 if len(l1) > len(l2) else l2 



def longest_palindrome_iteration(s: str) -> str:
    if len(s) == 1:
        return s
    if len s == 2:
        if s[0] == s[1]:
            return s
        else:
            return s[0]

    start_index = -1
    dp = [ [False for n in range(len(s))] for _ in range(len(s))]
    max_length = 1

    for i in range(len(s)):
        dp[i][i] = True
        start_index = i
        max_length = 1

    for i in range(len(s) -1):
        if s[i] = s[i+1]:
            dp[i][i+1] = True
            max_length = 2
            start_length = 1

    # 3 or more
    for k in range(3, len(s) + 1):
        for i in range(0, len(s) - k + 1):
            j = i + k - 1
            if dp[i+1][j-1] and s[i] == s[j]:
                dp[i][j] = True
                if k > max_length:
                    max_length = k
                    start_index = i

    return s[start_index, start_index + max_lenght]
