#type 2: recursion
def chop(item, alist):
    first = 0
    last = len(alist) -1
    res = recursiveBinary(item, alist, first, last)
    return res

def recursiveBinary(item, alist, first, last):
    if (last < first):
        return -1
    else:
        mid = first + (last - first)//2
        if alist[mid] > item:
            return recursiveBinary(item, alist, first, mid-1)
        elif alist[mid] < item:
            return recursiveBinary(item, alist,  mid+1, last)
        else:
            return mid
            




