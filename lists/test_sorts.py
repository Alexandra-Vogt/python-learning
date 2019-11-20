#!/usr/bin/env python3

# Import from python libraries
import random

# My file imports
from mergesort import mergesort
from quicksort import quicksort


def isSorted(numList):
    prevval = numList[0]
    isSorted = True
    for i in numList:
        if prevval > i:
            isSorted = False
            break
        else:
            prevval = i
    return isSorted


def testSort(sort):
    # Test edge cases
    assert sort([]) == []
    assert sort([0]) == [0]

    # Test list sorting
    testlist100 = [random.randrange(-1024, 1024) for i in range(100)]
    assert isSorted(sort(testlist100))

    testlist1000 = [random.randrange(-1024, 1024) for i in range(100)]
    assert isSorted(sort(testlist1000))

    testlist10000 = [random.randrange(-1024, 1024) for i in range(100)]
    assert isSorted(sort(testlist10000))


testSort(mergesort)
testSort(quicksort)
