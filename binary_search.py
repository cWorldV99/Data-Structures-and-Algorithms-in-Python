from random import randint

def binarySearch(array, target):
    new_array = sorted(array[:])
    not_found = True
    count = 0
    while(not_found):
        count += 1
        print(new_array)
        print("Round", count)
        middle = len(new_array)//2
        if(new_array[middle] == target):
            not_found = False
            return "Found..."
        elif(len(new_array) == 1):
            return "Not Found"
            break
        elif(target > new_array[middle]):
            new_array = new_array[middle:]
            middle = middle // 2
        elif(target < new_array[middle]):
            new_array = new_array[:middle]
            middle = middle//2
        else:
            return "Something Went Wrong..."


my_arr = []
for x in range(1, 1000):
    my_arr.append(randint(1, 10000))
to_find = randint(1, 10000)
print(to_find)
print(binarySearch(my_arr, to_find))
