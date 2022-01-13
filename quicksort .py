def Quicksort(alist,l,r):
    if (r-l)<=1:
        return
    (pivot,lower,upper)=(alist[l],l+1,l+1)
    for i in range(l+1,r):
        if alist[i]>pivot:
            upper+=1
        else:
            (alist[i],alist[lower])=(alist[lower],alist[i])
            (lower,upper)=(lower+1,upper+1)
    (alist[l],alist[lower-1])=(alist[lower-1],alist[l])
    lower-=1
    Quicksort(alist,l,lower)
    Quicksort(alist,lower+1,upper)
    return alist






if __name__=='__main__':
    alist = [54,26,93,17,77,31,44,55,20]
    print("sorted using Quicksort : ",Quicksort(alist,5,9)) 


        


