# TODO Make work
# base 16 radix sort
def radixsort(main_list):
    def get_digit(num, position):
        digit = 0
        if position == 0:
            digit = num % 16
        else:
            digit = num // (16 * position) % 16
        return digit

    def radix_subsort(input_list, position):
        sorted_list = []
        sublist_list = [[] for _ in range(16)]
        if len(input_list) > 0:
            for val in input_list:
                sublist_list[get_digit(val, position)].append(val)
                sorted_sublist_list = [sublist_list[0]] + [
                    radix_subsort(sublist, position + 1)
                    for sublist in sublist_list[1:-1]
                ]
            for sorted_sublist in sorted_sublist_list:
                sorted_list += sorted_sublist
        return sorted_list

    return radix_subsort(main_list, 0)
