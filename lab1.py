def max_list_iter(int_list):  # must use iteration not recursion
    # finds the max of a list of numbers and returns the value (not the index)
    #  If int_list is empty, returns None. If list is None, raises ValueError
    if int_list is None:
        raise ValueError
    if len(int_list) == 0:
        return None
    max_value = int_list[0]
    for i in range(len(int_list)):
        if max_value < int_list[i]:
            max_value = int_list[i]
    return max_value
    


def reverse_rec(int_list):  # must use recursion
    if int_list is None:
        raise ValueError
    if not int_list:
        return []
    if len(int_list) == 1:
        return int_list
    else:
        return reverse_rec(int_list[1:]) + [int_list[0]]
   


def bin_search(target, low, high, int_list):  # must use recursion
    # assume list is sorted from lowest to highest!!
    if int_list is None:
        raise ValueError
    if high >= low:
        # find our mid point for splitting the list
        # (high - low) needed in order to have an updated range
        # otherwise would always give the same mid
        mid = int(low + (high - low) / 2)
        # element is already in middle (otherwise we would skip over it)
        if int_list[mid] == target:
            return mid
        # case in which target is smaller than mid
        # sort through lower half of list
        elif int_list[mid] > target:
            return bin_search(target, low, mid - 1, int_list)
        # case in which target is larger than mid
        # sort through "higher" half of list
        else:
            return bin_search(target, mid + 1, high, int_list)
    # case in which target is not found
    else:
        return None



