def char_count(names):
    char_dict = {}
    for name in names:
        lc_name = name.lower()
        for char in lc_name:
            if char not in char_dict:
                char_dict[char] = 1
            char_dict[char] += 1
    return char_dict