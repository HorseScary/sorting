unsorted_list = [4,2,6,8,1]
sorted_list = [1,2,3,4,5]

def is_sorted(list:list):
    for i in range(len(list)):
        for j in range (len(list)-i-1):
            if list[i] > list[i+j+1]:
                return(False)
    return(True)

def something_sort(list:list):
    while not is_sorted(list):
        for i in range(len(list)):
            print(list)
            try:
                if list[i] > list[i+1]:
                    list.insert(i,list.pop(i+1))
            except IndexError:
                pass
    return(list)

if __name__ == "__main__":
    print(something_sort(unsorted_list))