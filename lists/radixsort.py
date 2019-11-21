# base 16 radix sort
def radixsort(main_list):
    def get_digit(num, position):
        digit = 0
        if position == 0:
            digit = num % 16
        else:
            digit = val // (16 * position) % 16
        return digit

    def radix_subsort(input_list, step):
        sorted_list = []
        sublist_list = [None for _ in range(16)]
        for val in input_list:
            sublist_list[get_digit(val, position)].append(val)
        sorted_sublist_list = [radix_subsort(sublist) for sublist in sublist_list]
        for sorted_sublist in sorted_sublist_list:
            sorted_list += sorted_sublist
        return sorted_list

    sublist_list = [None for _ in range(16)]

    return [radixsort(sublist) for sublist in sublist_list].join()
