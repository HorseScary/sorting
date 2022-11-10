unsorted_list = [4,2,6,8,1]
sorted_list = [1,2,3,4,5]

def is_sorted(list:list):
    for i in range(len(list)):
        for j in range (len(list)-i-1):
            print(f"i:   {list[i]}\ni+j: {list[i+j+1]}")
            if list[i] > list[i+j+1]:
                return(False)

    return(True)


if __name__ == "__main__":
    print(is_sorted(sorted_list))