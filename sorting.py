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
    for i in range(size):
        list.append(i+1)
    for i in range(10):
        pos = random.randint(0,size-1)
        item = random.randint(0,size-1)
        list.insert(pos, list.pop(item))
    return(list)

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
    working_offset = 1
    iterations = 0

    while not is_sorted(list):
        working_item = list.__len__() - working_offset
        for i in range(len(list) - working_offset + 1):
            iterations += 1
            #print(list)
            if list[i] > list[working_item]:
                print(f"{list}\n{list[working_item]} at {working_item} to {i}")
                list.insert(i, list.pop(working_item))
                print(list)
                break
            if i+1 == list.__len__():
                working_offset += 1
    print(f"List of size {list.__len__()} took {iterations} steps to sort.")
    return(list)
'''
instance of sort_3 not working
[4, 1, 6, 2, 3, 5]
5 at 5 to 2
[4, 1, 5, 6, 2, 3]
[4, 1, 5, 6, 2, 3]
3 at 5 to 0
[3, 4, 1, 5, 6, 2]
[3, 4, 1, 5, 6, 2]
2 at 5 to 0
[2, 3, 4, 1, 5, 6]
'''

if __name__ == "__main__":
    list = make_random_list(6)
    print(sort_3(list))