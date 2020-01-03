# given 2 strings, write a method to decide if one is a permutation of the other

## Examples abc => abc, acb, bac, bca, cab, cba

## Question
# Check if strings are of same length, are return none incase not of the same length

# create all the permutations from string 

# does capitalization matter  "DOG" == dog? or with roman characters?
# what about white space " dog" == "dog"?


def check_permutation(s1, s2):
    if s1.sort() == s2.sort:
        return True
    return False

## use a hash or an array - check solutions for the best implementation
