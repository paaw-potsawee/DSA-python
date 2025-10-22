def merge_sort(lst:list[int], left:int, right:int):
    center = (left + right) // 2
    if left < right:
        merge_sort(lst, center + 1, right)
        merge_sort(lst, left, center)
        merge(lst, left, right, center)
      
def merge(lst:list[int], left:int, right:int, center:int):
    i_left = left
    i_right = center + 1
    result = []
    while i_left <= center and i_right <= right:
        if lst[i_left] > lst[i_right]:
            result.append(lst[i_right])
            i_right += 1
        else:
            result.append(lst[i_left])
            i_left += 1

    while i_left <= center:
        result.append(lst[i_left])
        i_left += 1
    
    while i_right <= right:
        result.append(lst[i_right])
        i_right += 1

    for i in range(left, right + 1):
        lst[i] = result.pop(0)


if __name__ == "__main__":
    lst = [5, 3, 6, 9, 1, 2, 7, 8, 4]
    merge_sort(lst, 0, len(lst) - 1)
    print(lst)