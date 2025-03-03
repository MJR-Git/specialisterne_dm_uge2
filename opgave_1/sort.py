def sort(list):
    sorted_alpha = sorted(list)
    sorted_len = sorted(sorted_alpha, key=len)
    return sorted_len