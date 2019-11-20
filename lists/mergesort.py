def merge(head, tail):
    mergedList = []

    def mergePartial(shortList, longList):
        mergedList = []
        while shortList and longList:
            if shortList[0] < longList[0]:
                mergedList.append(shortList[0])
                shortList.pop(0)
            else:
                mergedList.append(longList[0])
                longList.pop(0)
        return mergedList + longList

    if len(head) < len(tail):
        mergedList = mergePartial(head, tail)
    else:
        mergedList = mergePartial(tail, head)

    return mergedList


def mergesort(list):

    head = list[len(list) // 2 :]
    tail = list[: len(list) // 2]
    if len(list) > 1:
        sortedHead = mergesort(head)
        sortedTail = mergesort(tail)
        return merge(sortedHead, sortedTail)
    else:
        return list
