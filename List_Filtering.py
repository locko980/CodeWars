def filter_list(l):
    int_list = [l[i] for i in range(len(l)) if type(l[i]) is int]
    return int_list
