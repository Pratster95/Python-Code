def selection_sort(L):
    suffixSt=0
    while suffixSt !=len(L):
        for i in range(suffixSt,len(L)):
            if L[i]<L[suffixSt]:
                L[suffixSt],L[i]=L[i],L[suffixSt]
        suffixSt += 1
    return L
print (selection_sort([5,2,8,0,1,7,6,2,8]))