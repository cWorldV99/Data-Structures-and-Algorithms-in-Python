def popSort(arr):
    """
    This is Sorting Algorithm I have Developed to Sort any integer of the given array.
    Where the Minimum Value of the given array will be POPPed Out each time and
    Appended to the new array... Finally Creating one New Sorted Array...
    """
    new_array = []
    not_empty = True
    while(not_empty):
        min_val = min(arr)
        val_index = arr.index(min_val)
        new_array.append(arr.pop(val_index))
        if(len(arr) == 0):
            not_empty = False
    return new_array


arr = [56, 13, 98, 17, 82, 47, 81, 56, 38, 55, 71, 93, 88]
print(popSort(arr))
