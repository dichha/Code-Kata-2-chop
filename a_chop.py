#type 1: while loop
def chop(item, alist):
    first = 0
    last = len(alist)-1
    found = False
    locT = -1
    
    while first<=last and not found:
        mid = (first+last)//2
        if (alist[mid] == item):
            found = True
            #loc = mid
            locT = mid
        
        else:
            if alist[mid] < item:
                first = mid + 1
                

            else:
                last = mid - 1
                
                
    #return (found, loc)
    return locT
