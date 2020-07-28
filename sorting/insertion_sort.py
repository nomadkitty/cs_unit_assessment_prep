def insertion_sort(input_list):
    pass
    # mark first item as sorted, separate first element?
    # (No code needed here, conceptual)

    # for every item starting at the second element
    for i in range(1, len(input_list)):
        # put current item in temp variable
        current_item = input_list[i]

        look_left_index = i - 1
        # look left, until we find where it belongs
        # if we are not at the beginning
        # and current item is less than sorted
        while look_left_index > 0 and current_item < input_list[look_left_index]:
            input_list[look_left_index + 1] = input_list[look_left_index]
            look_left_index -= 1
            # to find where it belongs
            # compare current item to sorted item
            # if sorted item is bigger,
            # shift sorted item rightward
        input_list[look_left_index] = current_item
        # if current item is greater than sorted
        # or we are at the begining of sorted
        # insert item
    return input_list
