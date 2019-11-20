import random


def quicksort(mainlist):
    sorted_list = []
    if len(mainlist) > 1:
        pivot = mainlist[0]
        greater_list = []
        lesser_list = []
        equal_list = []
        for val in mainlist:
            if val == pivot:
                equal_list.append(val)
            elif val > pivot:
                greater_list.append(val)
            else:
                lesser_list.append(val)
        sorted_list = quicksort(lesser_list) + equal_list + quicksort(greater_list)
    else:
        sorted_list = mainlist
    return sorted_list
