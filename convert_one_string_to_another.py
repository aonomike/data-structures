def convert_strings(string_1, string_2, index_1, index_2):
    if len(string_1) == index_1:
        return len(string_2) - index_2
    if len(string_2) == index_2:
        return len(string_1) - index_1
    if(string_1[index_1] == string_2[index_2]):
        return convert_strings(string_1, string_2, index_1 + 1 , index_2 + 1)
    replace_count = 1 + convert_strings(string_1, string_2, index_1 + 1 , index_2 + 1)
    insert_count = 1 + convert_strings(string_1, string_2, index_1 + 1 , index_2)
    delete_count = 1 + convert_strings(string_1, string_2, index_1 , index_2 + 1)
    return min(replace_count, insert_count, delete_count)

print(convert_strings("mike", "mokeerer", 0, 0))
