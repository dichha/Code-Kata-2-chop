def chop(item, alist):
    first = 0
    last = len(alist)-1
    locT = -1
    while first <= last:
        mid = first +(last-first)//2
        if alist[mid] == item:
            locT = mid
            return locT
        elif alist[mid] > item:
            last = mid -1
        else:
            first = mid+1
    return locT


print(chop(3, [1, 3, 5, 7]))
            