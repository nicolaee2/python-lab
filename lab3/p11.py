def custom_sort(tuples_list):
    return sorted(tuples_list, key=lambda x: x[1][2])


tuples_list = [('abc', 'bcd'), ('abc', 'zza')]
print(custom_sort(tuples_list))
