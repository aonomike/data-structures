hash_table = [None]*10
hash_table_nested = []
def hashing_func(key):
    return key % len(hash_table)

def insert(hash_table, key, value):
    hash_key = hashing_func(key)
    if hash_table[hash_key] is not None:
        hash_table[hash_key] = value
    else:
        resolve_linear_probing(hash_key, hash_table)

def resolve_linear_probing(hash_key, hash_table, value):
    for i in range(int(hash_key), len(hash_table)):
            if hash_table[i] is None:
                hash_table[i] = value

def resolve_chaining(hash_key, value):
