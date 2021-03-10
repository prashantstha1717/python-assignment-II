# 9. Write a binary search function. It should take a sorted sequence and the item it is looking for.
# It should return the index of the item if found.
# It should return -1 if the item is not found.

lis = [9, 18 , 16, 33, 55, 3, 69, 20]


def binary_search(sorted_list, n):
    low = 0
    high = len(sorted_list) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2
        if sorted_list[mid] < n:
            low = mid + 1
        elif sorted_list[mid] > n:
            high = mid - 1
        else:
            return mid
    return -1


sorted_list = sorted(lis)
print(sorted_list)
n = int(input('Input a number: '))

result = binary_search(sorted_list, n)
if result != -1:
    print(f'Element is present at index {result}')
else:
    print('-1')
