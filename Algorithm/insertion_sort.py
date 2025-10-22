def insertion_sort(lst:list[int]):
    n = len(lst)
    if n <= 1:
        return lst

    for i in range(1, n):
        tmp = lst[i]
        for j in range(i, -1, -1):
            print(f"{lst[i]} ({i}) < {lst[j]} ({j})")
            if j > 0 and lst[j - 1] > tmp:
                lst[j] = lst[j - 1]
            else:
                lst[j] = tmp
                break
        print(lst)

    return lst


if __name__ == "__main__":
    lst = [8, 6, 7, 5, 9]
    print(f"sorted list {insertion_sort(lst)}")