
#URLify: Write a method to replace all spaces in a string with '%20: You may assume that the string has sufficient space at the end to hold the additional characters, and that you are given the "true" length of the string. (Note: If implementing in Java, please use a character array so that you can perform this operation in place.)
# "Mr John Smith    "
# "Mr%20John%20Smith"
def urilfy(s, true_length):
    whole_string_length = len(s) - 1
    for i in range(true_length - 1, 0):
        if s[i] != " ":
            s[whole_string_length] = s[i]
            whole_string_length -= 1
        else:
            s[whole_string_length]="0"
            s[whole_string_length - 1]="2"
            s[whole_string_length - 2 ]="%"
            whole_string_length -= 3
        if whole_string_length == i:
            break
        

