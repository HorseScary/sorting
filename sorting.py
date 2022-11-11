import random

unsorted_list = [4,2,5,3,1]
sorted_list = [1,2,3,4,5]

def is_sorted(list:list):
    for i in range(len(list)):
        for j in range (len(list)-i-1):
            if list[i] > list[i+j+1]:
                return(False)
    return(True)

def make_random_list(size):
    list = []

def sort_1(list:list):
    while not is_sorted(list):
        for i in range(len(list)):
            print(list)
            try:
                if list[i] > list[i+1]:
                    list.insert(i,list.pop(i+1))
            except IndexError:
                pass
    return(list)

# this one doesn't work
def sort_2 (list:list):
    while not is_sorted(list):
        for i in range(len(list)):
            try:
                if list[i] > list[i+1]:
                    for j in range(i):
                        print(list)
                        if list[i] < list[j]:
                            list.insert(j,list.pop(i))
            except IndexError:
                pass
    return(list)

def sort_3 (list:list):


if __name__ == "__main__":
    print(sort_3(unsorted_list))