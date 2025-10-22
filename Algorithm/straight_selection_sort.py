def find_max(lst,cur_idx,max_idx):
    if cur_idx < 0:
        return lst[max_idx],max_idx

    if lst[cur_idx] > lst[max_idx]:
        max_idx = cur_idx

    return find_max(lst,cur_idx - 1,max_idx)

def striaght_selection(lst,last):
    if last < 0:
        return
    
    _,biggest_i = find_max(lst,last,0)
    
    if lst[last] != lst[biggest_i]:
        lst[last],lst[biggest_i] = lst[biggest_i],lst[last] 
        print(f'swap {lst[biggest_i]} <-> {lst[last]} : {lst}')

    striaght_selection(lst,last - 1)

   
if __name__ == "__main__":
    lst = [5, 3, 6, 9, 1, 2, 7, 8, 4]
    striaght_selection(lst, len(lst) - 1)
    print(lst)
