'''
this is a binary search that search for a random number from a particular range.
if the search find the random number, it'll return a True.
'''

import random


def binary_search(low, high):
    # random number
    randNum = random.randint(low, high)
    found = False

    # logic
    while low <= high and not found:
        mid = (low + high) / 2
        if mid == randNum:
            found = True
        else:
            if randNum > mid:
                low = mid
            else :
                high = mid    
    return found


# test
print(binary_search(0, 100))
print(binary_search(0, 50))