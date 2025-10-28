def bubble_sort(lst):
    n = len(lst)
    for i in range(n - 1, 0, -1):
        for j in range(0 ,i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

    return lst

if __name__ == "__main__":
    lst = [8, 6, 7, 5, 9]
    print(f"sorted list {bubble_sort(lst)}")