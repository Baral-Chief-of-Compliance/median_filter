def median_filter(arr: list, len_window_for_arr: int):
    if len_window_for_arr % 2 == 0:

        return {
            "code_key": 0,
            "arr": arr,
            "descp": "чётное окно"
        }

    if len_window_for_arr >= len(arr):
        return {
            "code_key": 1,
            "arr": arr,
            "descp": "большое окно"
        }

    result = []
    next_index = 0

    for i in range(len(arr)):
        if i == next_index:
            sum_of_el_arr = 0
            for j in range(len_window_for_arr):
                try:
                    sum_of_el_arr += arr[i+j]
                except:
                    continue

            result.append(sum_of_el_arr / len_window_for_arr)
            next_index += len_window_for_arr

    return result


#print(median_filter([1,2,3,4,5,6,7,8,9,10,11,20], 5))

